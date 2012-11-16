from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dooraccess/HTML$', 'mobilelock.views.dooraccess'),
    url(r'^dooraccess/unlock/(?P<doorID>\w+)/(?P<token>\w+)/$', 'mobilelock.views.dooraccessunlock'),
    url(r'^dooraccess/status/(?P<doorID>\w+)/(?P<token>\w+)/$', 'mobilelock.views.dooraccessstatus'),
    url(r'^arduino/HTML$', 'mobilelock.views.arduino'),
    url(r'^arduino/JSON$', 'mobilelock.views.arduinoJSON'),
    url(r'^arduino/(?P<name>\d+)/$','mobilelock.views.arduinodetail'),
    url(r'^door/HTML$', 'mobilelock.views.door'),
    url(r'^door/JSON$', 'mobilelock.views.doorJSON'),
    url(r'^door/(?P<name>\d+)/$','mobilelock.views.doordetail'),
    url(r'^device/doors/(?P<udid>\w+)/$','mobilelock.views.doorsForADevice'),
    url(r'^device/HTML$', 'mobilelock.views.device'),
    url(r'^device/JSON$', 'mobilelock.views.deviceJSON'),
    url(r'^device/(?P<phoneNumber>\d+)/$','mobilelock.views.devicedetail'),
    url(r'^register/device/(?P<first>\w+)/(?P<last>\w+)/(?P<number>\d+)/(?P<udid>\w+)/$','mobilelock.views.registerdevice'),
    url(r'^device/registrationStatus/(?P<udid>\w+)/$','mobilelock.views.deviceRegistrationStatus'))
