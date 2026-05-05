from django.contrib import admin
from django.utils.html import format_html
from .models import tecnologies


@admin.register(tecnologies)
class TecnologiesAdmin(admin.ModelAdmin):
    list_display = ("name", "image_preview")
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.img:
            return format_html('<img src="{}" style="height: 50px; width: auto;" />', obj.img.url)
        return "No image"

    image_preview.short_description = "Image"
