from datetime import timedelta

from django.contrib.gis.db import models
from django.utils.timezone import now

from .choices import PublicationStatus


class PublishedObjectsManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedObjectsManager, self)
            .get_queryset()
            .filter(
                pub_status=PublicationStatus.Published,
                # add 1 second of slop for safety
                pub_date__date__lte=now() + timedelta(seconds=1)
            )
        )


class PublishedObjectsStoryManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedObjectsStoryManager, self)
            .get_queryset()
            .filter(
                pub_status=PublicationStatus.Published,
                # add 1 second of slop for safety
                day_pub_date__date__lte=now() + timedelta(seconds=1)
            )
        )


class PublishedObjectsGeoManager(models.GeoManager):
    def get_queryset(self):
        return (
            super(PublishedObjectsGeoManager, self)
            .get_queryset()
            .filter(
                pub_status=PublicationStatus.Published,
                # add 1 second of slop for safety
                pub_date__date__lte=now() + timedelta(seconds=1)
            )
        )


class PublishedObjectsPhotoManager(models.Manager):
    def get_queryset(self):
        return (
            super(PublishedObjectsPhotoManager, self)
            .get_queryset()
            .filter(
                pub_status=PublicationStatus.Published,
                # add 1 second of slop for safety
                pub_date__lte=now() + timedelta(seconds=1)
            )
        )
