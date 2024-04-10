from django.db import models
from datetime import datetime
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    is_resolved = models.BooleanField(default=False)
    contacted_at = models.DateTimeField(default=datetime.now)


    class Meta:
        verbose_name = ('Contact')
        verbose_name_plural = ('contacts')

    def __str__(self) :
        return self.email