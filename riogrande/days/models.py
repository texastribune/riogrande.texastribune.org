from django.db import models


class Day(models.Model):
    """ One model to rule them all. """

    # publication fields
    date = models.DateTimeField()

    def __unicode__(self):
        return unicode(self.date.strftime('%m/%d/%Y'))
