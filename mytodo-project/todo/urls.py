from django.urls import path
from .views import TodosAPIView, TodosAPIMixinView, TodoAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
    path('mixin/todo/', TodosAPIMixinView.as_view()),
    path('todo/<int:pk>/', TodoAPIView.as_view()),
]
