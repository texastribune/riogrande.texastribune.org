import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from days.models import Day
from measurements.models import Measurement
from photos.models import Gallery
from pings.models import Ping
from posts.models import Post


class LandingView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        context['most_recent_days'] = Day.objects.all()[:3]

        return context


class DayView(TemplateView):
    template_name = 'day.html'

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data(**kwargs)
        date_format = '%Y__%m__%d'
        date_string = '__'.join((
            context['year'],
            context['month'],
            context['day']))
        date = datetime.datetime.strptime(date_string, date_format).date()
        context['day'] = get_object_or_404(Day, date__contains=date)

        return context
