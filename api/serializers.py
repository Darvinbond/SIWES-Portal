from django.db.models import fields
from rest_framework import serializers
from .models import *


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class OrganizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = organization
        fields = '__all__'


class SupSerializers(serializers.ModelSerializer):
    class Meta:
        model = supervisor
        fields = '__all__'


class ReportSerializers(serializers.ModelSerializer):
    class Meta:
        model = report
        fields = '__all__'


class MessageSerializers(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'


class MessageCountSerializers(serializers.ModelSerializer):
    class Meta:
        model = message_count
        fields = '__all__'
