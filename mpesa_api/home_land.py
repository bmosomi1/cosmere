import json
import logging

import requests
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from requests.auth import HTTPBasicAuth

from mpesa_api.models import Mpesa
from sms.models import *

logging.basicConfig(filename="home_land.log", level=logging.DEBUG)
pass_key = "839379054e176e543745d325c5b6ab76dda9f38ad76bca47c638fd70d9205788"


def get_mpesa_access_token():
    consumer_key = "Q6K7iz5aF530m9pU7xfYQZXQvn4AUiQO"
    consumer_secret = "gSztAKumyZdGGvcw"
    api_URL = "https://api.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return validated_mpesa_access_token


@csrf_exempt
def register_urls(request):
    access_token = get_mpesa_access_token()
    print(access_token)
    api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    headers = {"Authorization": "Bearer %s" % access_token}
    options = {"ShortCode": "863893",
               "ResponseType": "Completed",
               "ConfirmationURL": "https://roberms.co.ke/api/v1/c2b/homeland/863893/confirmation",
               "ValidationURL": "https://roberms.co.ke/api/v1/c2b/homeland/863893/validation"}
    response = requests.post(api_url, json=options, headers=headers)
    return HttpResponse(response.text)


@csrf_exempt
def validation(request):
    context = {
        "ResultCode": 1,
        "ResultDesc": "Failed",
        "ThirdPartyTransID": 0
    }
    return JsonResponse(dict(context))


@csrf_exempt
def confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)
    Mpesa.objects.create(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        email="homeland@roberms.com",
        type=mpesa_payment['TransactionType'],
        created_at=timezone.now(),
        organization_balance=mpesa_payment['OrgAccountBalance']
    )

    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }

    till_number = mpesa_payment['BusinessShortCode']
    groups = Group.objects.filter(name__contains=str(till_number))
    for group in groups:
        if group is not None:
            if Contact.objects.filter(group=group, phone_number=mpesa_payment['MSISDN']).count() < 1:
                Contact.objects.create(
                    group=group,
                    email="homeland@roberms.com",
                    phone_number=mpesa_payment['MSISDN'],
                    name=f"{mpesa_payment['FirstName']} {mpesa_payment['MiddleName']}"
                )
    return JsonResponse(dict(context))