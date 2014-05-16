from django.db import models


class Post(models.Model):

    # publication fields
    pub_date = models.DateTimeField()
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    # content fields
    text = models.TextField()

    objects = models.Manager()

    def __unicode__(self):
        return self.headline
