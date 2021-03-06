from datetime import datetime

from django.contrib.syndication.views import Feed

from days.models import Day
from posts.models import Post


class DayFeed(Feed):
    title = 'Disappearing Rio Grande - All daily updates'
    link = '/'
    description = 'Daily updates on Colin\'s progress on the Rio Grande.'
    description_template = 'feeds/day_description.html'

    def items(self):
        return Day.objects.order_by('-date')[:20]

    def item_title(self, day):
        try:
            post_headline = day.post_for.headline
            return u'{0} - {1}'.format(post_headline, day)
        except Post.DoesNotExist:
            return day

    def item_pubdate(self, day):
        return datetime.combine(day.date, datetime.min.time())
