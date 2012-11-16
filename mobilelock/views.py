from django.template import Context, loader
from mobilelock.models import DoorAccess
from mobilelock.models import Arduino
from mobilelock.models import Door
from mobilelock.models import Device
from django.http import HttpResponse
import json
import urllib2
from datetime import date


def index(request):
    return HttpResponse("Hello, world. You're at the mobile door lock index.")

def dooraccess(request):
    latest_dooraccess_list = DoorAccess.objects.all()
    t = loader.get_template('dooraccess/index.html')
    c = Context({
                 'latest_access_list': latest_dooraccess_list,
    })
    return HttpResponse(t.render(c))

def dooraccessstatus(request,doorID,token):
    status = 0
    for da in DoorAccess.objects.all():
        if str(da.door.id) == doorID and da.mobileDevice.deviceToken == token:
            address = "http://" + str(da.arduino.ip) + "/statusCheck/0"
            request = urllib2.urlopen(address)
            status = request.getcode()
            break   
    if(status != 200):
        return HttpResponse("{\"response\":\"error\",\"code\":\"" + str(status) + "\"}",mimetype="application/json")
    return HttpResponse("{\"response\":\"success\"}",mimetype="application/json")

def dooraccessunlock(request,doorID,token):
    status = 0
    for da in DoorAccess.objects.all():
        if str(da.door.id) == doorID and da.mobileDevice.deviceToken == token:
            address = "http://" + str(da.arduino.ip) + "/doorUnlock/8"
            request = urllib2.urlopen(address)
            status = request.getcode()
            break   
    if(status != 200):
        return HttpResponse("{\"response\":\"error\",\"code\":\"" + str(status) + "\"}",mimetype="application/json")
    return HttpResponse("{\"result\":\"success\"}")
    
def arduino(request):
    latest_arduino_list = Arduino.objects.all().order_by('dateAdded')[:5]
    t = loader.get_template('arduino/index.html')
    c = Context({
                 'latest_arduino_list': latest_arduino_list,
    })
    return HttpResponse(t.render(c))

def arduinoJSON(request):
    req = {}
    i = 0
    for a in Arduino.objects.all():
        req[i] = {}
        req[i]['id'] = a.id
        req[i]['name'] = a.name
        req[i]['ip'] = a.ip
        i = i + 1
    response = json.dumps(req)
    return HttpResponse(response, mimetype="application/json")

def arduinodetail(request,name):
    return HttpResponse("Your are looking at %s." % name)

def door(request):
    latest_door_list = Door.objects.all().order_by('dateAdded')[:14]
    t = loader.get_template('door/index.html')
    c = Context({
                 'latest_door_list': latest_door_list,
    })
    return HttpResponse(t.render(c))

def doorJSON(request):
    req = {}
    i = 0
    for d in Door.objects.all():
        req[i] = {}
        req[i]['id'] = d.id
        req[i]['name'] = d.name
        req[i]['streetNumber'] = d.streetNumber
        req[i]['streetName'] = d.streetName
        req[i]['city'] = d.city
        req[i]['state'] = d.state
        req[i]['zip'] = d.zip
        i = i + 1
    response = json.dumps(req)
    return HttpResponse(response, mimetype="application/json")

def doorsForADevice(request,udid):
    req = {}
    i = 0
    for da in DoorAccess.objects.all():
        if da.mobileDevice.deviceToken == udid:
            req[i] = {}
            req[i]['id'] = da.door.id
            req[i]['name'] = da.door.name
            req[i]['streetNumber'] = da.door.streetNumber
            req[i]['streetName'] = da.door.streetName
            req[i]['city'] = da.door.city
            req[i]['state'] = da.door.state
            req[i]['zip'] = da.door.zip
            i = i + 1
    response = json.dumps(req)
    return HttpResponse(response, mimetype="application/json")

def doordetail(request,name):
    return HttpResponse("Your are looking at %s." % name)

def device(request):
    latest_device_list = Device.objects.all().order_by('dateAdded')[:15]
    t = loader.get_template('device/index.html')
    c = Context({
                 'latest_device_list': latest_device_list,
    })
    return HttpResponse(t.render(c))

def deviceJSON(request):
    req = {}
    i = 0
    for d in Device.objects.all():
        req[i] = {}
        req[i]['id'] = d.id
        req[i]['ownerFirstName'] = d.ownerFirstName
        req[i]['ownerLastName'] = d.ownerLastName
        req[i]['phoneNumber'] = d.phoneNumber
        req[i]['deviceToken'] = d.deviceToken
        req[i]['status'] = d.status
        i = i + 1
    response = json.dumps(req)
    return HttpResponse(response, mimetype="application/json")

def devicedetail(request,phoneNumber):
    return HttpResponse("Your are looking at %s." % phoneNumber)

def registerdevice(request,first,last,number,udid):
    req = {}
    req[0] = {}
    req[0]['ownerFirstName'] = first
    req[0]['ownerLastName'] = last
    req[0]['phoneNumber'] = number
    req[0]['deviceToken'] = udid
    req[0]['status'] = 1
    d = Device(ownerFirstName=first, ownerLastName=last, phoneNumber=number, deviceToken=udid, status=1, dateAdded=date.today())
    d.save()
    req = {}
    req['result'] = 'pending'
    response = json.dumps(req)
    return HttpResponse(response)

def deviceRegistrationStatus(request,udid):
    status = -1
    for d in Device.objects.all():
        if d.deviceToken == udid:
            status = d.status
            break
    req = {}
    req['status'] = status
    response = json.dumps(req)
    return HttpResponse(response)
            

def randomTest(request):
    callback = request.GET.get('callback', '')
    req = {}
    req ['title'] = 'This is a constant result.'
    response = json.dumps(req)
    response = callback + '(' + response + ');'
    return HttpResponse(response, mimetype="application/json")