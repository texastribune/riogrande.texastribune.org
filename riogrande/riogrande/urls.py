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
    url(r'^blog/(?P<year>\d{4})/(?P<month>[-\w]+)/(?P<day>\d+)/$',
        views.DayView.as_view(),
        name='day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>[-\w]+)/',
        views.StoryDetail.as_view(),
        name='story_detail'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^archive/', views.ArchiveView.as_view(), name='archive'),

    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
