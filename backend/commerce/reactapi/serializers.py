from rest_framework import serializers
from .models import Pornstar


class PornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pornstar
        read_only_fileds = ['id']
        fields = ['id', 'name', 'alias']
