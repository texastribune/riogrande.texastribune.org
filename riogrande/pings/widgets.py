from django.forms import widgets
from django.contrib.gis.geos import Point


class LatLonWidget(widgets.MultiWidget):

    def __init__(self, attrs=None):
        _widgets = (
            widgets.TextInput(),
            widgets.TextInput(),
        )

        super(LatLonWidget, self).__init__(_widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.y, value.x]
        return [None, None]

    def format_output(self, rendered_widgets):
        return (u'<p class="datetime">Latitude: {0}<br>'
                'Longitude: {1}</p>').format(
                    rendered_widgets[0],
                    rendered_widgets[1])

    def value_from_datadict(self, data, files, name):
        try:
            p = Point(
                float(data['location_1']),
                float(data['location_0']),
            )
        except ValueError:
            return ''
        else:
            return p
