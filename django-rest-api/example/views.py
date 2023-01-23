# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework import mixins
from .models import Book
from .serializers import BookSerializer


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    response = Response('hello world!')
    print('response.data > ', response.data)  # hello world!
    # print('response.status > ', response.status) Response does not have status field
    return response


@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET':
        books = Book.objects.all()
        # <class 'django.db.models.query.QuerySet'>
        print('### type(books) > ', type(books))
        serializer = BookSerializer(books, many=True)
        # <class 'rest_framework.utils.serializer_helpers.ReturnList'>
        print('### type(serializer.data) > ', type(serializer.data))
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = BookSerializer()
        print('### repr(serializer) > ', repr(serializer))
        serializer = BookSerializer(data=request.data)
        # <class 'django.http.request.QueryDict'>
        print('### type(request.data) > ', type(request.data))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 잘못된 요청
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bookAPI(request, bid):
    book = get_object_or_404(Book, bid=bid)
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


class BooksAPI(APIView):

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()
            print('### type(result) > ', type(result))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPI(APIView):

    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BooksAPIMixins(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView
):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs) # mixins.ListModelMixin과 연결

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs) # mixins.CreateModelMixin과 연결


class BookAPIMixins(
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs) # mixins.RetrieveModelMixin과 연결
