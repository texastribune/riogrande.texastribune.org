from django import forms
from django.contrib import admin
from django.db import models

from .models import Post


class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={
                'class':'ckeditor',
            })
        }
    }

    class Media:
        js = ('ckeditor/ckeditor.js', )


admin.site.register(Post, PostAdmin)
