from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
import datetime
from . import code2
from . import decorder


def home(request):
    if request.method == 'POST':
        try:
            code_input = request.POST['codeinput']
            codeout = decorder.main_code(code_input)
            return render(request, 'home.html', {'codeoutput': codeout})
        except:
            text_input = request.POST['textinput']
            textout = code2.main_code(text_input)
            return render(request, 'home.html', {'textoutput': textout})

    else:
        return render(request, 'home.html')


def sendHumkam(request):
    data = {
        "notification": {"body": "TODAY'S HUKAMNAMA FROM SRI DARBAR SAHIB, Sri Amritsar.", "title": "Hukamnama Sahib"},
        "priority": "high",
        "data": {
            "click_action": "FLUTTER_NOTIFICATION_CLICK",
            "hukam": 'true'
        },
        "to":"/topics/hukam",
    }

    headers = {
      'content-type': 'application/json',
      'Authorization': 'key=AAAAALKGjxw:APA91bGIQrURLECUCSy5dfFwDYers7dbK4WrqOL6ATPeMbiolIhOPuIUyCDAuMRQgnXctEOLL7tC9KspwJjaGOYByoq0fPbRSMar4ZgI76jmAk3uebv3QLO-3zbhvovh6Rz43cllJiTR'
    }

    res = requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers)

    return JsonResponse(res.text, safe=False)


def sendGurupurab(request):
    res = []

    with open('dates.json', encoding='utf-8') as f:
        json_data = json.load(f)

    today = datetime.datetime.now()
    for holiday in json_data[str(today.month)][str(today.day)]:
        data = {
            "notification": {"body": holiday['en'], "title": holiday['pa']},
            "priority": "high",
            "data": {
                "click_action": "FLUTTER_NOTIFICATION_CLICK",
            },
            "to":"/topics/gurupurab",
        }

        headers = {
        'content-type': 'application/json',
        'Authorization': 'key=AAAAALKGjxw:APA91bGIQrURLECUCSy5dfFwDYers7dbK4WrqOL6ATPeMbiolIhOPuIUyCDAuMRQgnXctEOLL7tC9KspwJjaGOYByoq0fPbRSMar4ZgI76jmAk3uebv3QLO-3zbhvovh6Rz43cllJiTR'
        }

        res += requests.post('https://fcm.googleapis.com/fcm/send', data=json.dumps(data), headers=headers).text

    return JsonResponse(res, safe=False)


def about(request):
    return render(request, 'about.html')