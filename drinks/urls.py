from django.conf.urls.defaults import *
from django.contrib import admin
from mydrinks.models import Drink, Comment
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
admin.site.register(Drink)
admin.site.register(Comment)

DRINKS = {  'queryset': Drink.objects.all(),
            }

urlpatterns = patterns('',
  (r'^$', 'django.views.generic.list_detail.object_list', DRINKS),
  (r'^drink/(?P<object_id>.*)/$', 'django.views.generic.list_detail.object_detail', DRINKS),
  (r'^admin/doc/', include('django.contrib.admindocs.urls')),
  (r'^admin/', include(admin.site.urls)),
  (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT, 'show_indexes': True }),
)
