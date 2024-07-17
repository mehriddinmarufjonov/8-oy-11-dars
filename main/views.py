from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Kundalik
from .serializers import KundalikSerializer


class KundalikView(ModelViewSet):
    queryset = Kundalik.objects.all()
    serializer_class = KundalikSerializer