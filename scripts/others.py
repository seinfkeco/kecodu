# -*- coding: utf-8 -*-
__auther__ = '35942'

'''
# mixins,ViewSet和routers配合使用
minxis的类有5种  他们分别对应了对数据库的增查改删操作
CreateModelMixin
ListModelMixin
RetrieveModelMixin
UpdateModelMixin
DestroyModelMixin

ViewSet也有5种,分别是
ViewSetMixin
ViewSet
GenericViewSet
ReadOnlyModelViewSet
ModelViewSet


一般来说我们只需要用GenericViewSet就可以了.它继承了ViewSetMixin和generics.GenericAPIView,后者的功能大家都知道,有了它才能设置queryset和serializer_class属性.重点是ViewSetMixin.

#=======================================================认证===========================================================
如果你在生产中使用BasicAuthentication，那么你必须确保你的API仅在https中可用。你还应确保你的API客户端始终在登录时重新请求用户名和密码，并且不会将这些详细信息存储到持久存储中。
如果你在生产环境下使用TokenAuthentication认证，你必须确保你的API仅在https可用。
curl -X GET http://127.0.0.1:8000/api/example/ -H 'Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b'


#=========================================== 权限============================================================
AllowAny：允许无限制访问
IsAuthenticated ：允许访问任何经过身份验证的用户，并拒绝访问任何未经身份验证的用户
IsAdminUser：允许超级用户访问
IsAuthenticatedOrReadOnly：对经过身份验证的用户的允许完全访问，但对未经身份验证的用户的允许只读访问
'''


