from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import models


class Day(models.Model):
    """ One model to rule them all. """

    # publication fields
    date = models.DateField(unique=True)

    class Meta:
        ordering = ('-date', )

    def __unicode__(self):
        return unicode(self.date.strftime('%m/%d/%Y'))

    @property
    def get_pings_list(self):
        if self.pings.count():
            return 'hello'

    def get_absolute_url(self):
        pub_date = self.date

        return reverse('day', kwargs={
            'year': pub_date.strftime('%Y'),
            'month': pub_date.strftime('%m'),
            'day': pub_date.strftime('%d'),
        })

    def get_share_url(self):
        pub_date = self.date

        return 'http://riogrande.texastribune.org' + reverse('day', kwargs={
            'year': pub_date.strftime('%Y'),
            'month': pub_date.strftime('%m'),
            'day': pub_date.strftime('%d'),
        })

    @property
    def has_published_content(self):
        try:
            post_status = self.post_for.pub_status == 'P'
        except ObjectDoesNotExist:
            post_status = False

        try:
            gallery_status = self.gallery_for.pub_status == 'P'
        except ObjectDoesNotExist:
            gallery_status = False

        try:
            measurement_status = self.measurement_for.pub_status == 'P'
        except ObjectDoesNotExist:
            measurement_status = False

        return any([post_status, gallery_status, measurement_status])
