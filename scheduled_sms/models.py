from statistics import mode
from django.db import models
from sms.models import Customer, Group


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ScheduledMessage(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50, default='ROBERMS_LTD')
    text_message = models.TextField(max_length=600, null=True)
    track_code = models.CharField(max_length=50, null=True)
    scheduled_time = models.DateTimeField()
    sender_type = models.IntegerField(choices=Customer.SENDER_TYPE_CHOICES, default=Customer.PROMOTIONAL)
    active = models.BooleanField(default=True)
    # group = models.ForeignKey(Group, on_delete=models.CASCADE)
    is_sent = models.BooleanField(default=False)
    # extra_status = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=200)
    usage_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'ScheduledMessage'
        verbose_name_plural = 'ScheduledMessage'


class SchedulePerMonth(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    sender_name = models.CharField(max_length=50, default='ROBERMS_LTD')
    text_message = models.TextField(max_length=3000)
    phone_number = models.CharField(max_length=500)
    send_on = models.IntegerField() # the day of the month when the sms should be sent
    is_active = models.BooleanField(default=False)
    last_sent = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)