# Django imports
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.middleware.csrf import get_token
from django.views import View

# Rest Framework imports
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView

# Local imports
from .models import AudioFile
from .serializers import AudioUploadSerializer

# External library imports
import io
from pydub import AudioSegment


class AudioSegmentView(View):
    def get(self, song_id, duration):
        audio_file = AudioFile.objects.get(pk=song_id)
        audio_path = audio_file.url.path

        full_audio = AudioSegment.from_file(audio_path)

        start_time = 0
        end_time = int(duration) * 1000
        audio_segment = full_audio[start_time:end_time]

        output = io.BytesIO()
        audio_segment.export(output, format="mp3")

        response = HttpResponse(output.getvalue(), content_type="audio/mpeg")
        return response

class AudioAPIView(APIView):
    def get(self, request):
        queryset = AudioFile.objects.all()
        paginator = Paginator(queryset, 20)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        if page_number and int(page_number) > paginator.num_pages:
            return Response([])

        serializer = AudioUploadSerializer(page_obj, many=True, context={'request': request})

        return Response(serializer.data)

class AudioAPITest(APIView):
    def get(self, song_id):

        song = AudioFile.objects.get(id=song_id)
        song_data = song.url.path
        with open(song_data, "rb") as file:
            response = HttpResponse(file.read(), content_type="audio/mpeg")
        return response
        

class CSRFTokenAPIView(APIView):
    def get(self, request):
        token = get_token(request)
        return Response({'csrfToken': token})