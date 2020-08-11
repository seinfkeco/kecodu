from django.shortcuts import HttpResponse

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser,AllowAny

from keco.dudu.serializers import WfinfoSerializer
from keco.dudu.models import SG_CON_PLANT_B
# class WfViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
#     """
#         基础信息表
#     """
#
#     queryset = SG_CON_PLANT_B.objects.all()  #TODO  这里问题
#     serializer_class = WfinfoSerializer

class WfInfoView(APIView):
    """
        列出系统中的电场信息。
        * 不需要token认证
    """
    permission_classes = (AllowAny,)  # 允许无限制访问

    def get(self, request):
        serialize = WfinfoSerializer(SG_CON_PLANT_B.objects.all(), many=True)
        return Response(serialize.data)

