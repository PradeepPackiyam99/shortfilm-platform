from django.db import models

class Film(models.Model):

    title = models.CharField(max_length=200)
    description = models.TextField()
    video = models.FileField(upload_to='films/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
