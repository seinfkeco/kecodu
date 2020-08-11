from django.shortcuts import HttpResponse

# Create your views here.

import traceback

from django.contrib.auth.models import User, Group
from rest_framework import viewsets,mixins
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, throttle_classes,permission_classes,authentication_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny
from keco.api.serializers import UserSerializer, GroupSerializer
from rest_framework.authtoken.models import Token

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


"""
如果通用视图不适合你的API的需求，你可以选择使用常规 APIView 类，或重用通用视图使用的mixins和基类来组成你自己的一组可重用的通用视图。
"""
class ListUsers(APIView):
    """
    列出系统中的所有用户的视图。
    * 需要token认证
    * 只有管理员用户可以访问这个视图。
    """
    authentication_classes = (SessionAuthentication, BasicAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        data = dict()
        usernames = [user.username for user in User.objects.all()]
        emails = [user.email for user in User.objects.all()]
        data["username"] = usernames
        data["emails"] = emails
        return Response(data)

    def post(self, request, format=None):
        """
        :param request:
        :param format:
        :return:
        """


# =====================================================================================================================

class OncePerDayUserThrottle(UserRateThrottle):  #用户一天访问一次
    rate = '1/day'


@api_view(['GET', 'POST'])
@authentication_classes((SessionAuthentication, BasicAuthentication,TokenAuthentication))
@permission_classes((IsAuthenticated,))  # 认证后才能访问
@throttle_classes([OncePerDayUserThrottle])
def users_list(request, format=None):
    """
     Return a list of all users.
    """
    if request.method == "GET":
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames, status=status.HTTP_200_OK)
    elif request.method == "POST":
        """"""
        #TODO

"""
@renderer_classes(...)
@parser_classes(...)
@authentication_classes(...)
@throttle_classes(...)
@permission_classes(...)
这些装饰器中的每一个都接受一个参数，这个参数必须是类的列表或元组。
"""

class UserTokenView(APIView):
    """
    用户认证, token生成
    """
    authentication_classes = (BasicAuthentication,)
    permission_classes = (AllowAny,)  #允许无限制访问
    def post(self, request, *args, **kwargs):
        """
        用户token不存在创建，存在返回token值
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        user = request.data.get("username")
        data = {"msg": "", "code": "99999", "data": None}
        msg = ""
        try:
            obj = User.objects.filter(username=user).first()
            if not obj:
                msg = "用户不存在"
            user_id = obj.id
            user_token_obj = Token.objects.filter(user_id=user_id).first()
            if not user_token_obj:
                token = Token.objects.create(user=obj)
                tkey = token.key
            else:
                tkey = user_token_obj.key
            data["data"] = {"token": tkey}
            msg = "success"
        except:
            traceback.print_exc()
            msg = "failed"
        data["msg"] = msg
        return Response(data)



