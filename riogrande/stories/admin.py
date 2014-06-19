from django import forms
from django.contrib import admin
from django.db import models

from .models import Story


class StoryAdmin(admin.ModelAdmin):
    exclude = ('day_pub_date', )

    formfield_overrides = {
        models.TextField: {
            'widget': forms.Textarea(attrs={
                'class':'ckeditor',
            })
        }
    }

    prepopulated_fields = {'slug': ('headline',)}

    class Media:
        js = ('ckeditor/ckeditor.js', )


admin.site.register(Story, StoryAdmin)
