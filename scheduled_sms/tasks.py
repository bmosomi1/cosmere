from django.utils import timezone
# from sms_api.views import send_usage
from sms.models import Customer
import logging
import django
from .models import *
from celery.task import task


@task()
def store_scheduled_sms(customer_id, total_message_cost, to_be_sent, trackingcode, time):
    logging.error("Sms store got here")
    customer = Customer.objects.filter(id=customer_id).first()
    new_credit = customer.credit - total_message_cost
    customer.credit = new_credit
    customer.save()

    # messages = []
    for a, b in to_be_sent.items():
        outgoing_new, created = ScheduledMessage.objects.update_or_create(
            customer=customer,
            sender_name=customer.access_code,
            phone_number=a,
            text_message=b,
            track_code=trackingcode,
            scheduled_time=time,
            usage_status=True,
            sender_type=customer.sender_type
        )
    return 'completed insertion'