from django.db import models
from sms.models import Customer


class DeliveryUrl(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    delivery_url = models.CharField(max_length=250)


class BenardInbox(models.Model):
    msisdn = models.CharField(max_length=500)
    offer_code = models.CharField(max_length=500)
    short_code = models.CharField(max_length=500)
    message = models.TextField()
    request_id = models.CharField(max_length=1000)
    link_id = models.CharField(max_length=1000)
    delivery_status = models.CharField(max_length=500, null=True)
    oc = models.CharField(max_length=500, null=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
