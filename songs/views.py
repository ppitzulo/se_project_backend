# Django imports
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.shortcuts import get_object_or_404

# Rest Framework imports
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import *
from .serializers import AudioUploadSerializer

# External library imports
import io
from pydub import AudioSegment

class AudioUploadAPIView(APIView):
    def post(self, request):
        if request.method == 'POST':
            files = request.FILES.getlist('files')
            if len(files) == 0:
                return JsonResponse({'error': 'No file was submitted'})
            
            for file in files:
                instance = Song(url=file)
                instance.save()

            return JsonResponse({'message': 'Files uploaded successfully'})
        return JsonResponse({'error': 'Invalid request method'})
    
class AudioSegmentView(View):
    def get(self, request, song_id, duration, *args, **kwargs):
        audio_file = Song.objects.get(pk=song_id)
        audio_path = audio_file.url.path

        full_audio = AudioSegment.from_file(audio_path)

        start_time = 0
        end_time = int(duration) * 1000
        audio_segment = full_audio[start_time:end_time]

        output = io.BytesIO()
        audio_segment.export(output, format="mp3")

        response = HttpResponse(output.getvalue(), content_type="audio/mpeg")
        return response

class SongAPIView(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, id=song_id)
        title = song.title
        url = "/songs/audio/"
        url += str(song_id) + "/"

        data = {
            'title': title,
            'url': url,
        }

        response = JsonResponse(data)
        return response

class AudioAPIView(APIView):
    def get(self, request):
        queryset = Song.objects.all()
        serializer = AudioUploadSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
    
class playlistAPIView(APIView):
    def get(self, request, playlist_name):
        playlist = get_object_or_404(PlayList, name=playlist_name)
        songs = playlist.songs.all()

        song_list = []

        for song in songs:
            song_data = {
                'title': song.title,
                'id': song.id,
                'artist': song.artist,
                'runtime': song.runtime,
            }
            song_list.append(song_data)
    
        return JsonResponse({"songs": song_list})