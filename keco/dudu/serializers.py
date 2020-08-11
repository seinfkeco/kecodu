# -*- coding: utf-8 -*-
__auther__ = '35942'
from django.contrib.auth.models import User, Group
from keco.dudu.models import SG_CON_PLANT_B
from rest_framework import serializers


class WfinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SG_CON_PLANT_B
        fields = '__all__'
