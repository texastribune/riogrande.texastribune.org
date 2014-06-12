from datetime import timedelta

from django.db import models
from django.utils.timezone import now

from .choices import PublicationStatus


class PublishedObjectsManager(models.Manager):
    def get_query_set(self):
        return (
            super(PublishedObjectsManager, self)
            .get_query_set()
            .filter(
                pub_status=PublicationStatus.Published,
                # add 1 second of slop for safety
                pub_date__lte=now() + timedelta(seconds=1)
            )
        )
