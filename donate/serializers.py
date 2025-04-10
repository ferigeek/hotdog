from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = '__all__'

    def validate(self, data):
        if data['amount'] <= 0:
            raise serializers.ValidationError("Donation amount must be greater than zero.")
        return data