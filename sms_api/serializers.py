from rest_framework import serializers

from sms.models import OutgoingApi, OutgoingApiNew, OutgoingNew
from sms_api.models import BenardInbox


class OutgoingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutgoingNew
        fields = ['access_code', 'phone_number', 'text_message']


class BernardInboxSerializer(serializers.ModelSerializer):
    class Meta:
        model = BenardInbox
        fields = ['msisdn', 'offer_code', 'short_code', 'message', 'request_id', 'link_id']