from django.contrib import admin

from .models import Photo, Gallery


class PhotoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class GalleryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Photo, PhotoAdmin)
admin.site.register(Gallery, GalleryAdmin)
