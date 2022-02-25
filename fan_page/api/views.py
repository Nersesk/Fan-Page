from rest_framework import mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.generics import RetrieveUpdateAPIView,RetrieveAPIView,ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.permissions import IsAuthenticated
from shop.models import Attributes
from .permissions import AdminPermissons
from news.models import Post, Category
from .serializers import PostSerializer,AttributeSerializer

class AttributesPagination(PageNumberPagination):
    max_page_size = 100
    page_size = 5
    page_query_param = 'page_size'

class PostApiView(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    @action(methods=['get'],detail=True)
    def category(self,request,pk):
        cat=Category.objects.get(pk=pk)
        return Response({'category': f'{cat.name}'})
    permission_classes = (AdminPermissons,)


class AttributesApi(RetrieveUpdateAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributeSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class AttributesApiList(ListAPIView):
    queryset = Attributes.objects.all()
    serializer_class = AttributeSerializer
    pagination_class = AttributesPagination
