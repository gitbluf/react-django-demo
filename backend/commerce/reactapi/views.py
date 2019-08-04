from django.shortcuts import render
from rest_framework.response import Response
from .serializers import PornSerializer
from .models import Pornstar
from rest_framework import generics

class PornList(generics.ListCreateAPIView):
    queryset = Pornstar.objects.all().order_by('id')
    serializer_class = PornSerializer

class PornDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pornstar.objects.all()
    serializer_class = PornSerializer
