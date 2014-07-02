import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import DateDetailView, ListView, TemplateView

from days.models import Day
from stories.models import Story


class LandingView(TemplateView):
    template_name = 'landing.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)

        context['most_recent_days'] = Day.objects.all()[:3]
        context['most_recent_story'] = Story.published.latest('pub_date')

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
        context['most_recent_story'] = Story.published.latest('pub_date')

        return context


class StoryDetail(DateDetailView):
    date_field = 'pub_date'
    model = Story
    month_format = '%m'
    template_name = 'story.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class ArchiveView(ListView):
    model = Day
    template_name = 'archive.html'
