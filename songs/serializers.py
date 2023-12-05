from rest_framework import serializers
from .models import Song

class AudioUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'url', 'title', 'runtime', 'artist']