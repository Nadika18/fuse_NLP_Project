from django.db import models




class TextComplaint(models.Model):
    complaint=models.CharField(max_length=100)
    complaint_time=models.DateTimeField(auto_now_add=True)
    predicted_class = models.CharField(max_length=100, blank=True, null=True)


class AudioRecording(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='audio/',null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    converted_text=models.CharField(max_length=100,null=True,default='None')

    def __str__(self):
        return self.title
