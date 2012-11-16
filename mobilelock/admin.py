from django.contrib import admin
from mobilelock.models import DoorAccess
from mobilelock.models import Arduino
from mobilelock.models import Door
from mobilelock.models import Device

admin.site.register(DoorAccess)
admin.site.register(Arduino)
admin.site.register(Door)
admin.site.register(Device)
