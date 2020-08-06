from django.shortcuts import HttpResponse

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from keco.api.serializers import UserSerializer, GroupSerializer
# def api_first(request):
#     return HttpResponse({'msg': 'ok', 'code': '99999', 'data': None})



class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer