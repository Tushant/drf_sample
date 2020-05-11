import datetime

from django.db import models

# will later have queryset to filter published notes

class PublishableModel(models.Model):
    publication_date = models.DateField(blank=True, null=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        abstract = True

    @property
    def is_visible(self):
        return self.is_published and (
            self.publication_date is None
            or self.publication_date < datetime.date.today()
        )


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True