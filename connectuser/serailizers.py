from .models import CurrentUser, Pdf
from rest_framework import serializers


class ConnectUserSeriailizer(serializers.ModelSerializer):

    class Meta:
        model = CurrentUser
        fields = '__all__'


class PdfSeriailizer(serializers.ModelSerializer):

    class Meta:
        model = Pdf
        fields = '__all__'