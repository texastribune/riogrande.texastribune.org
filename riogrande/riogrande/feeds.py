from django.contrib.syndication.views import Feed

from days.models import Day
from posts.models import Post


class DayFeed(Feed):
    title = 'All daily updates'
    link = '/'
    description = 'Daily updates on Colin\'s progress on the Rio Grande.'
    description_template = 'feeds/day_description.html'

    def items(self):
        return Day.objects.order_by('-date')[:10]

    def item_title(self, day):
        try:
            post_headline = day.post_for.headline
            return u'{0} - {1}'.format(post_headline, day)
        except Post.DoesNotExist:
            return day
