# from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    response = Response('hello world!')
    print('response.data > ', response.data) # hello world!
    # print('response.status > ', response.status) Response does not have status field
    return response
