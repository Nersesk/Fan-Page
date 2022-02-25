from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from .views import PostApiView,AttributesApi,AttributesApiList

router=routers.SimpleRouter()
router.register(r'posts',PostApiView,basename='post')

urlpatterns=[
    path('v1/',include(router.urls)),
    path('rest/auth/',include('rest_framework.urls')),
    path(r'auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('v1/shop_list/',AttributesApiList.as_view()),
    path('v1/shop_attributes/<int:pk>',AttributesApi.as_view()),

]