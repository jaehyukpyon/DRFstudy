from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework import mixins
from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Todo
from .serializers import (
    TodoSimpleSerializer, 
    TodoDetailSerializer, 
    TodoCreateSerializer,
)

# Create your views here.

class TodosAPIView(APIView):
    
    def get(self, request):
        todos = Todo.objects.filter(complete=False)
        serializer = TodoSimpleSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(f'$$$ {serializer.data}') # $$$ {'title': 'DRF공부하기', 'description': '책 보며 DRF 공부하기', 'important': False}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class TodosAPIMixinView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    
    queryset = Todo.objects.all()
    serializer_class = TodoSimpleSerializer
    
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    
class TodoAPIView(APIView):
    """
    상세 조회용 View
    """
    def get(self, request, pk):
        todo = get_object_or_404(Todo, id=pk) # 만약 여기서 결과 값이 1개 초과라면 MultipleObjectsReturned 에러 발생
        print('### type(todo) > ', type(todo)) # <class 'todo.models.Todo'>
        print('### todo.description > ', todo.description)
        serializer = TodoDetailSerializer(todo) # 만약 many=True를 설정했으나, 만약 첫 번째 인자로 넘기는 값이 iterable하지 않다면 에러 발생
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        # title만 보내도 정상 작동.
        todo = get_object_or_404(Todo, id=pk)
        serializer = TodoCreateSerializer(todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    