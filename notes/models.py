from django.db import models

from core.models import PublishableModel, TimeStampModel

class Note(PublishableModel, TimeStampModel):
    title = models.CharField(max_length=180)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Note'
        verbose_name_plural = 'Notes'
    
    def __str__(self):
        return str(self.pk)
