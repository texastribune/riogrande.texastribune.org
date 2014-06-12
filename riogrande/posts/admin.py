from django import forms
from django.contrib import admin
from django.contrib.gis.db import models

from .models import Post
from pings.widgets import LatLonWidget


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={
                'class':'ckeditor',
            })
        },
        models.PointField: {'widget': LatLonWidget}
    }

    prepopulated_fields = {'slug': ('headline',)}

    class Media:
        js = ('ckeditor/ckeditor.js', )


admin.site.register(Post, PostAdmin)
