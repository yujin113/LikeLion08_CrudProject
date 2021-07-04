from django.db import models
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    writer = models.CharField(max_length=200)
    created_at = models.DateTimeField('작성시간', default = timezone.now)
    body = models.TextField()
    image = models.ImageField(upload_to='images/', default = "", null=True)

    def __str__(self):
        return self.writer
    
    def summary(self):
        return self.body[:100]