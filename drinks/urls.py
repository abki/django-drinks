from django.conf.urls.defaults import *
from django.contrib import admin
from mydrinks.models import Drink, Comment

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()
admin.site.register(Drink)
admin.site.register(Comment)

urlpatterns = patterns('',
    # Example:
    # (r'^drinks/', include('drinks.foo.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
