from django.db import models
from django.utils.translation import gettext_lazy as _
class tecnologies(models.Model):
    name = models.CharField(max_length=255)
    img=models.ImageField(_("tecnologies"), upload_to='tecnologies/', height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return f"{self.name} - {self.img}"

    class Meta:
        verbose_name = _("tecnologies")
        verbose_name_plural = _("tecnologies")
