from django import forms

from scheduled_sms.models import SchedulePerMonth


class SchedulePerMonthForm(forms.ModelForm):
    class Meta:
        model = SchedulePerMonth
        fields = [
            "customer", "text_message", "send_on", "sender_name", "phone_number", "is_active"
        ]