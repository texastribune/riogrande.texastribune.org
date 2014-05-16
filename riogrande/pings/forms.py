from django import forms
from django.contrib.gis.geos import GEOSGeometry

from .widgets import LatLonWidget


class LatLonField(forms.MultiValueField):
    widget = LatLonWidget()

    def __init__(self, *args, **kwargs):
        _fields = (
            forms.DecimalField(),
            forms.DecimalField(),
        )
        super(LatLonField, self).__init__(_fields, *args, **kwargs)

    def compress(self, values):
        if values:
            return GEOSGeometry('POINT ({0} {1})'.format(values[1], values[0]))
        return None
