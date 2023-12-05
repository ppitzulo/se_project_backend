from django.db import models
from django.conf import settings
import eyed3

# Create your models here.
class AudioFile(models.Model):
    url = models.FileField(upload_to='audio/')
    title = models.CharField(max_length=255, default="Untitled")
    runtime = models.CharField(max_length=10, default="0:00")
    artist = models.CharField(max_length=255, default="Unknown")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
       
        if self.url:

            self.title = self.url.name.split('.mp3')[0]
        super().save(*args, **kwargs)
        
        # Get the file path
        file_path = self.url.path
        print(file_path)
        audio = eyed3.load(file_path)

        if audio.info is not None:
            # Extract metadata from the audio file using the file path
            self.runtime = self.format_runtime(int(audio.info.time_secs))
            if audio.tag.artist is not None:
                self.artist = audio.tag.artist

            super().save(*args, **kwargs)
            
    def format_runtime(self, runtime):
        # Takes runtime in seconds and converts to H:M:S or M:S if less than an hour
        
        hours, remainder = divmod(runtime, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(minutes)

        if hours > 0:
            return f'{hours}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}'
        else:
            return f'{minutes}:{str(seconds).zfill(2)}'