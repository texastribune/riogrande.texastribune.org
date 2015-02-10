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

        days = Day.objects.filter(post_for__isnull=False).order_by('date')

        most_recent_days = []

        for day in days:
            if day.has_published_content is True:
                most_recent_days.append(day)
            if len(most_recent_days) == 3:
                break

        context['most_recent_days'] = most_recent_days
        context['most_recent_story'] = Story.published.latest('pub_date')

        return context


class DayView(TemplateView):
    template_name = 'day.html'

    def get_next_day(self, **kwargs):
        try:
            next_day = kwargs['day'].get_next_by_date()
        except Day.DoesNotExist:
            return None

        while not next_day.has_published_content:
            try:
                next_day = next_day.get_next_by_date()
            except Day.DoesNotExist:
                return None

        return next_day

    def get_previous_day(self, **kwargs):
        try:
            previous_day = kwargs['day'].get_previous_by_date()
        except Day.DoesNotExist:
            return None

        while not previous_day.has_published_content:
            try:
                previous_day = previous_day.get_previous_by_date()
            except Day.DoesNotExist:
                return None

        return previous_day

    def get_context_data(self, **kwargs):
        context = super(DayView, self).get_context_data(**kwargs)
        date_format = '%Y__%m__%d'
        date_string = '__'.join((
            context['year'],
            context['month'],
            context['day']))
        date = datetime.datetime.strptime(date_string, date_format).date()
        context['day'] = get_object_or_404(Day, date__contains=date)
        context['next_day'] = self.get_next_day(day=context['day'])
        context['previous_day'] = self.get_previous_day(day=context['day'])
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
    queryset = Day.objects.order_by('date')
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
        } for p in Post.objects.filter(pub_status='P')]

    def get_context_data(self, **kwargs):
        context = super(ArchiveView, self).get_context_data(**kwargs)
        context['archive_post_list'] = self.get_all_posts()
        context['archive_ping_list'] = self.get_all_pings()

        return context
