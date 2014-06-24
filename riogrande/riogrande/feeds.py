from django.contrib.syndication.views import Feed

from days.models import Day


class DayFeed(Feed):
    title = 'Daily updates'
    link = '/blog/'
    description = 'Daily updates on Colin\'s progress on the Rio Grande.'

    def items(self):
        return Day.objects.order_by('-day')[:5]

