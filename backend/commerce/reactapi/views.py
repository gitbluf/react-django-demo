from django.shortcuts import render

from rest_framework import viewsets
from .serializers import PornSerializer
from .models import Pornstar

class PornViewSet(viewsets.ModelViewSet):
    queryset = Pornstar.objects.all().order_by('name')
    serializer_class = PornSerializer
