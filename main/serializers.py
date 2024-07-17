from rest_framework import serializers
from .models import Kundalik


class KundalikSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kundalik
        fields = '__all__'