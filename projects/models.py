from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    img =models.ImageField(_("Image"), upload_to='projects/', height_field=None, width_field=None, max_length=None)
    live_link = models.URLField()
    github_link = models.URLField()
    start_date = models.DateField()
    end_date = models.DateField()
    technologies =ArrayField(base_field=models.CharField(default=list, max_length=50))

    def __str__(self):
        return self.name