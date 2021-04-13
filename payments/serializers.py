from rest_framework import serializers
from payments.models import Transactions


class TansactionIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ("id",)

class TansactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = "__all__"