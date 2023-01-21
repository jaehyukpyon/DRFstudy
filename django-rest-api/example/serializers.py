from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.Serializer):
    bid = serializers.IntegerField()
    title = serializers.CharField(max_length=50)
    author = serializers.CharField(max_length=50)
    category = serializers.CharField(max_length=50)
    pages = serializers.IntegerField()
    price = serializers.IntegerField()
    published_date = serializers.DateField()
    description = serializers.TextField()
    
    def create(self, validated_data):
        print('BookSerializer.create method called...')
        print('BookSerializer.create validated_data > ', validated_data)
        return Book.objects.create(**validated_data)
    
        
