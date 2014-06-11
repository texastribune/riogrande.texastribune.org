import json
from os import environ
import urllib2

from django.core.management.base import BaseCommand
from django.utils import dateparse

from django.contrib.gis.geos import Point

from pings.models import Ping

FEED_API = ('https://api.findmespot.com/spot-main-web/consumer/rest-api'
            '/2.0/public/feed/{0}/message.json')


class Command(BaseCommand):
    help = 'Grabs the GPS feed and creates models to store the point.'

    def handle(self, *args, **kwargs):
        findmespot_id = environ['FINDMESPOT_ID']

        response = urllib2.urlopen(FEED_API.format(findmespot_id))
        response = json.load(response)

        messages = response['response']['feedMessageResponse']['messages']['message']

        for r in messages:
            ping, created = Ping.objects.get_or_create(
                location=Point(r['longitude'], r['latitude']),
                pub_date=dateparse.parse_datetime(r['dateTime']),
                api_id=r['id'],
            )
