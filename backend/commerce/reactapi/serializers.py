from rest_framework import serializers
from .models import Pornstar


class PornSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pornstar
        fields = ('name', 'alias')
