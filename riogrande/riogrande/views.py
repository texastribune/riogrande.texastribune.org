from datetime import date

from django.views.generic import TemplateView

from measurements.models import Measurement
from photos.models import Gallery
from pings.models import Ping
from posts.models import Post


class LandingView(TemplateView):
    template_name = 'landing.html'


class DayView(TemplateView):
    template_name = 'day.html'

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data(**kwargs)
        page_date = date(
            int(context['year']),
            int(context['month']),
            int(context['day']))

        context['pings'] = Ping.objects.filter(
            pub_date__contains=page_date)

        try:
            context['post'] = Post.objects.get(
                pub_date__contains=page_date)
        except Post.DoesNotExist:
            pass

        try:
            context['gallery'] = Gallery.objects.get(
                date_added__contains=page_date)
        except Gallery.DoesNotExist:
            pass

        try:
            context['measurement'] = Measurement.objects.get(
                pub_date__contains=page_date)
        except Measurement.DoesNotExist:
            pass

        return context
