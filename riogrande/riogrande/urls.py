from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

from . import views

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'riogrande.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.LandingView.as_view(), name='landing'),
    url(r'^(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d+)/$',
        views.DayView.as_view(),
        name='day'
    ),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
