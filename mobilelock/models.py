from django.db import models
import datetime
from django.utils import timezone
from django.core.validators import RegexValidator

class Arduino(models.Model):
    def __unicode__(self):
        return self.name
    def date_added(self):
        return self.dateAdded
    name = models.CharField(max_length = 200)
    ip = models.CharField(max_length = 15)
    dateAdded = models.DateTimeField('date added')

class Door(models.Model):
    def __unicode__(self):
        return self.name
    def date_added(self):
        return self.dateAdded
    arduino = models.ForeignKey(Arduino)
    name = models.CharField(max_length = 200)
    streetNumber = models.IntegerField(max_length = 10)
    streetName = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    state = models.CharField(max_length = 2, validators=[RegexValidator(regex='^.{2}$', message='Length must be 2', code='nomatch')])
    zip = models.IntegerField(validators=[RegexValidator(regex='^.{5}$', message='Length must be 5', code='nomatch')])
    dateAdded = models.DateTimeField('date added')
    
class Device(models.Model):
    def __unicode__(self):
        return self.ownerLastName + ", " + self.ownerFirstName
    def date_added(self):
        return self.dateAdded
    ownerFirstName = models.CharField(max_length = 200)
    ownerLastName = models.CharField(max_length = 200)
    phoneNumber = models.BigIntegerField(max_length = 10, validators=[RegexValidator(regex='^.{10}$', message='Length must be 10', code='nomatch')])
    deviceToken = models.CharField(max_length = 32, validators=[RegexValidator(regex='^.{32}$', message='Length must be 32', code='nomatch')])
    dateAdded = models.DateTimeField('date added')
    STATUS_CODES = (('0', 'Disabled'), ('1', 'Pending'), ('2', 'Enabled'))
    status = models.CharField(max_length=2, choices=STATUS_CODES)
      
class DoorAccess(models.Model):
    def __unicode__(self):
        return self.arduino.name
    mobileDevice = models.ForeignKey(Device)
    arduino = models.ForeignKey(Arduino)
    door = models.ForeignKey(Door)
