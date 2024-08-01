from django.db import models

class AudioRecording(models.Model):
    audio = models.FileField(upload_to='audio/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def delete(self, *args, **kwargs):
        self.audio.delete()
        super().delete(*args, **kwargs)