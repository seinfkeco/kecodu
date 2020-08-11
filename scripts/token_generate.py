# -*- coding: utf-8 -*-
__auther__ = '35942'
# from rest_framework.authtoken.models import Token
#
# token = Token.objects.create(user=''')  #填入的是user Obj
# print (token.key)


from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

for user in User.objects.all():
    token = Token.objects.get_or_create(user=user)
    print(token.key)