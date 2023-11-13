from rest_framework import serializers
from .models import AudioFile

class AudioUploadSerializer(serializers.ModelSerializer):

    thumbnail = serializers.SerializerMethodField('get_thumbnail_url')
    # thumbnail = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = AudioFile
        fields = ['id', 'url', 'title', 'runtime', 'thumbnail', 'artist']
    
    def get_thumbnail_url(self, obj):
        request = self.context.get("request")

        try:
            return request.build_absolute_uri(obj.thumbnail.url)
        except ValueError:
            return None