from rest_framework import serializers
from news.models import Post
from shop.models import Attributes


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class AttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Attributes
        fields = '__all__'