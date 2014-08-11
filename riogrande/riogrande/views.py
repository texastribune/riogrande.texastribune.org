import datetime

from django.shortcuts import get_object_or_404
from django.views.generic import DateDetailView, ListView, TemplateView

from days.models import Day
from pings.models import Ping
from posts.models import Post
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

    def get_all_pings(self):
        return [{
            'lat': p.location.y,
            'lng': p.location.x,
            'date': p.pub_date.date.strftime('%b. %d, %Y')
        } for p in Ping.objects.all()]

    def get_all_posts(self):
        return [{
            'lat': p.location.y,
            'lng': p.location.x,
            'date': p.pub_date.date.strftime('%b. %d, %Y'),
            'headline': str(p.headline),
            'slug': p.pub_date.get_absolute_url()
        } for p in Post.objects.all()]

    def get_context_data(self, **kwargs):
      context = super(ArchiveView, self).get_context_data(**kwargs)
      context['archive_post_list'] = self.get_all_posts()
      context['archive_ping_list'] = self.get_all_pings()

      return context
