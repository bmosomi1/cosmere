import base64
import datetime
import json
import random
import requests
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny

from integrations.credentials import mpesa_access_token, Miwama, GreenNote, Parklands, RealBoutique1, RealBoutique2, \
    RealBoutique3, Parklands2, Boresha, Roberms, Perezu, Nope, Perezu2, CleanShiftCredentials, GreenNote2Credentials, \
    OlemaxCredentials, AquaNovaCredentials
from integrations.models import MiwamaMpesa, RealBoutiqueMpesa, PerezuMpesa, NopeMpesa, CleanShift, GreenNoteMpesa, \
    OlemaxMpesa, AquaNovaMpesa
import logging

from mpesa_api.models import GathuMpesa, Mpesa
from sms.models import Contact, Outgoing, OutgoingNew, Customer, Sms_TopUp
from sms.utils import calculate_message_cost

logging.basicConfig(filename="test.log", level=logging.DEBUG)


@method_decorator(csrf_exempt, name='dispatch')
class MiwamaMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(Miwama.CONSUMER_KEY, Miwama.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "7335205",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/miwama/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/miwama/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))


@csrf_exempt
def miwama_confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)

    logging.debug(f"Miwama {mpesa_payment}")

    MiwamaMpesa.objects.create(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        type=mpesa_payment['TransactionType'],
        account_number=mpesa_payment['BusinessShortCode'],
        organization_balance=mpesa_payment['OrgAccountBalance']
    )
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class GreenNoteMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(GreenNote.CONSUMER_KEY, GreenNote.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "929063",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/greennote/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/greennote/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))


@csrf_exempt
def greennote_confirmation(request):
    mpesa_body = request.body.decode('utf-8')
    mpesa_payment = json.loads(mpesa_body)

    logging.debug(f"GreenNote {mpesa_payment}")

    GathuMpesa.objects.create(
        first_name=mpesa_payment['FirstName'],
        last_name=mpesa_payment['MiddleName'],
        description=mpesa_payment['TransID'],
        phone_number=mpesa_payment['MSISDN'],
        amount=mpesa_payment['TransAmount'],
        reference=mpesa_payment['BillRefNumber'],
        type=mpesa_payment['TransactionType'],
        account_number=mpesa_payment['BusinessShortCode'],
        organization_balance=mpesa_payment['OrgAccountBalance']
    )
    context = {
        "ResultCode": 0,
        "ResultDesc": "Accepted"
    }
    return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class ParkLandsMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(Parklands.CONSUMER_KEY, Parklands.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "5030453",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/parklands/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/parklands/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        GathuMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )

        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class ParkLands2MpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(Parklands2.CONSUMER_KEY, Parklands2.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "788530",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/parklands2/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/parklands2/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        GathuMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )

        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class RealBoutiqueMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register/4016345')
    def register_urls(self, request):
        access_token = mpesa_access_token(RealBoutique1.CONSUMER_KEY, RealBoutique1.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4016345",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/real/boutique/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/real/boutique/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='register/461923')
    def register_urls_2(self, request):
        access_token = mpesa_access_token(RealBoutique2.CONSUMER_KEY, RealBoutique2.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "461923",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/real/boutique/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/real/boutique/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='register/461113')
    def register_urls_3(self, request):
        access_token = mpesa_access_token(RealBoutique3.CONSUMER_KEY, RealBoutique3.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "461113",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/real/boutique/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/real/boutique/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        RealBoutiqueMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )

        customer = Customer.objects.filter(user_ptr_id=564).first()
        customer_code = f"{datetime.datetime.today().date()}{customer.id}"
        message = f"Dear {mpesa_payment['FirstName']} {mpesa_payment['MiddleName']}, Kshs {mpesa_payment['TransAmount']} has been received. Thank You for shopping at LiQizo Apparels. " \
                  f"We are so grateful for the pleasure of serving You. Please send us your feedback on " \
                  f"+254723876628 or Follow Us on social media @liqizoapparels."
        message_cost = calculate_message_cost(message)

        if float(message_cost) <= float(customer.credit):
            OutgoingNew.objects.create(
                phone_number=mpesa_payment['MSISDN'],
                text_message=message,
                access_code="LIQIZO",
                customer_id=customer.id,
                track_code=customer_code.replace('-', ''),
                request_identifier=customer_code.replace('-', ''),
                sender_type=customer.sender_type,
                sent_time=datetime.datetime.today()
            )
            customer.credit = float(customer.credit) - float(message_cost)
            customer.save()

        group_id = None
        if mpesa_payment['BusinessShortCode'] == '4016345':
            group_id = 7194
        elif mpesa_payment['BusinessShortCode'] == '461923':
            group_id = 7195
        elif mpesa_payment['BusinessShortCode'] == '461113':
            group_id = 7196

        if group_id:
            Contact.objects.update_or_create(
                name=f"{mpesa_payment['FirstName']} {mpesa_payment['MiddleName']}",
                phone_number=mpesa_payment['MSISDN'],
                email=mpesa_payment['MSISDN'],
                group_id=group_id
            )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class BoreshaMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(Boresha.CONSUMER_KEY, Boresha.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4043927",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/boresha/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/boresha/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        GathuMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['MiddleName'],
            description=mpesa_payment['TransID'],
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )

        customer = Customer.objects.filter(user_ptr_id=571).first()
        customer_code = f"{datetime.datetime.today().date()}{customer.id}"
        message = f"Dear {mpesa_payment['FirstName']} {mpesa_payment['MiddleName']}, your payment of " \
                  f"Kshs {mpesa_payment['TransAmount']}  has been received. For orders contact us on 0701743594."
        message_cost = calculate_message_cost(message)

        if float(message_cost) <= float(customer.credit):
            OutgoingNew.objects.create(
                phone_number=mpesa_payment['MSISDN'],
                text_message=message,
                access_code="Boreshoney",
                customer_id=customer.id,
                track_code=customer_code.replace('-', ''),
                request_identifier=customer_code.replace('-', ''),
                sender_type=customer.sender_type,
                sent_time=datetime.datetime.today()
            )
            customer.credit = float(customer.credit) - float(message_cost)
            customer.save()

        group_id = 7204
        if group_id:
            Contact.objects.update_or_create(
                name=f"{mpesa_payment['FirstName']} {mpesa_payment['MiddleName']}",
                phone_number=mpesa_payment['MSISDN'],
                email=mpesa_payment['MSISDN'],
                group_id=group_id
            )

        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class RobermsMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        print('got here')
        access_token = mpesa_access_token(Roberms.CONSUMER_KEY, Roberms.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "7690604",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/roberms/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/roberms/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        Mpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )

        tracking_code = random.randint(1, 9999999)
        while Sms_TopUp.objects.filter(verifycode=tracking_code, verified=0):
            tracking_code = random.randint(1, 9999999)

        customer = Customer.objects.filter().first()
        # phone_number = mpesa_payment['MSISDN'].rsplit(" ", 1)[1]
        phone_number = mpesa_payment['MSISDN'][-3:]
        customer_id = Sms_TopUp.objects.filter(
            user_phone__endswith=phone_number,
            f_name=mpesa_payment['FirstName']).first()

        if customer_id is not None:
            Sms_TopUp.objects.create(
                user_phone=customer_id.user_phone,
                transaction_ref=mpesa_payment['TransID'],
                amount=mpesa_payment['TransAmount'],
                till_number=mpesa_payment['BusinessShortCode'],
                f_name=mpesa_payment['FirstName'],
                l_name=mpesa_payment['FirstName'],
                signature=mpesa_payment['TransID'],
                account_no='TILL NUMBER',
                transaction_type=mpesa_payment['TransactionType'],
                verifycode=tracking_code,
                user_id=0,
                timestamp=mpesa_payment['TransTime'],
            )

            message = f"Thank you {mpesa_payment['FirstName']} for paying for Roberms Holdings SMS service. " \
                      f"To automatically load the credit into your account, " \
                      f"use this code to verify your payment. \n Verification code: {tracking_code}"

            OutgoingNew.objects.create(
                phone_number=customer_id.user_phone,
                text_message=message,
                access_code="ROBERMS_LTD",
                customer_id=customer.id,
                track_code=tracking_code,
                request_identifier=tracking_code
            )
        else:
            Sms_TopUp.objects.create(
                user_phone=mpesa_payment['MSISDN'],
                transaction_ref=mpesa_payment['TransID'],
                amount=mpesa_payment['TransAmount'],
                till_number=mpesa_payment['BusinessShortCode'],
                f_name=mpesa_payment['FirstName'],
                l_name=mpesa_payment['FirstName'],
                signature=mpesa_payment['TransID'],
                account_no='TILL NUMBER',
                transaction_type=mpesa_payment['TransactionType'],
                verifycode=tracking_code,
                user_id=0,
                timestamp=mpesa_payment['TransTime'],
            )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='stk-push/confirmation/(?P<phone_number>\d+)')
    def stk_confirmation(self, request, phone_number):
        logging.info(f"{request.body}")
        logging.info(f"{request}")

        try:
            mpesa_body = request.body.decode('utf-8')
            mpesa_payment = json.loads(mpesa_body)

            Mpesa.objects.create(
                first_name=mpesa_payment['FirstName'],
                last_name=mpesa_payment['FirstName'],
                description=mpesa_payment,
                phone_number=phone_number,
                amount=mpesa_payment['TransAmount'],
                reference=mpesa_payment['BillRefNumber'],
                type=mpesa_payment['TransactionType'],
                account_number=mpesa_payment['BusinessShortCode'],
                organization_balance=mpesa_payment['OrgAccountBalance']
            )

            tracking_code = random.randint(1, 100000)
            while Sms_TopUp.objects.filter(verifycode=tracking_code, verified=0):
                tracking_code = random.randint(1, 100000)

            customer = Customer.objects.filter().first()

            Sms_TopUp.objects.create(
                user_phone=phone_number,
                transaction_ref=mpesa_payment['TransID'],
                amount=mpesa_payment['TransAmount'],
                till_number=mpesa_payment['BusinessShortCode'],
                f_name=mpesa_payment['FirstName'],
                l_name=mpesa_payment['FirstName'],
                signature=mpesa_payment['TransID'],
                account_no='TILL NUMBER',
                transaction_type=mpesa_payment['TransactionType'],
                verifycode=tracking_code,
                user_id=0,
                timestamp=mpesa_payment['TransTime'],
            )

            message = f"Thank you {mpesa_payment['FirstName']} for paying for Roberms Holdings SMS service. " \
                      f"To automatically load the credit into your account, " \
                      f"use this code to verify your payment. \n Verification code: {tracking_code}"

            OutgoingNew.objects.create(
                phone_number=phone_number,
                text_message=message,
                access_code="ROBERMS_LTD",
                customer_id=customer.id,
                track_code=tracking_code,
                request_identifier=tracking_code
            )
            context = {
                "ResultCode": 0,
                "ResultDesc": "Accepted"
            }
            return JsonResponse(dict(context))
        except Exception as e:
            logging.info(f'{e}')
            context = {
                "ResultCode": 0,
                "ResultDesc": "Accepted"
            }
            return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class PerezuMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        print('got here')
        access_token = mpesa_access_token(Perezu.CONSUMER_KEY, Perezu.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "544697",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/perezu/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/perezu/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        PerezuMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class PerezuMpesaViewSet2(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(Perezu2.CONSUMER_KEY, Perezu2.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "367788",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/perezu2/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/perezu2/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        PerezuMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class NopeMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        print('got here')
        access_token = mpesa_access_token(Nope.CONSUMER_KEY, Nope.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4091515",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/nope/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/nope/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        NopeMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class CleanShiftMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(CleanShiftCredentials.CONSUMER_KEY, CleanShiftCredentials.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4096639",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/cleanshift/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/cleanshift/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        CleanShift.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class GreenNote2MpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(GreenNote2Credentials.CONSUMER_KEY, GreenNote2Credentials.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4108579",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/greennote2/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/greennote2/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        GreenNoteMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class OlemaxMpesaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(OlemaxCredentials.CONSUMER_KEY, OlemaxCredentials.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "499086",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/olemax/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/olemax/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        OlemaxMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))


@method_decorator(csrf_exempt, name='dispatch')
class AquaNovaViewSet(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    @action(methods=['get'], detail=False, url_path='register')
    def register_urls(self, request):
        access_token = mpesa_access_token(AquaNovaCredentials.CONSUMER_KEY, AquaNovaCredentials.CONSUMER_PASSWORD)
        api_url = "https://api.safaricom.co.ke/mpesa/c2b/v2/registerurl"
        headers = {"Authorization": "Bearer %s" % access_token}
        options = {"ShortCode": "4108623",
                   "ResponseType": "Completed",
                   "ConfirmationURL": "https://roberms.co.ke/integrations/aquanova/confirmation/",
                   "ValidationURL": "https://roberms.co.ke/integrations/aquanova/validation/"}
        response = requests.post(api_url, json=options, headers=headers)
        return HttpResponse(response.text)

    @action(methods=['get'], detail=False, url_path='validation')
    def validation(self, request):
        context = {
            "ResultCode": 0,
            "ResultDesc": "Completed"
        }
        return JsonResponse(dict(context))

    @action(methods=['post'], detail=False, url_path='confirmation')
    def confirmation(self, request):
        mpesa_body = request.body.decode('utf-8')
        mpesa_payment = json.loads(mpesa_body)

        AquaNovaMpesa.objects.create(
            first_name=mpesa_payment['FirstName'],
            last_name=mpesa_payment['FirstName'],
            description=mpesa_payment,
            phone_number=mpesa_payment['MSISDN'],
            amount=mpesa_payment['TransAmount'],
            reference=mpesa_payment['BillRefNumber'],
            type=mpesa_payment['TransactionType'],
            account_number=mpesa_payment['BusinessShortCode'],
            organization_balance=mpesa_payment['OrgAccountBalance']
        )
        context = {
            "ResultCode": 0,
            "ResultDesc": "Accepted"
        }
        return JsonResponse(dict(context))