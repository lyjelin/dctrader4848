from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import OrderList, OrderDetail

urlpatterns = [
    path('order/', OrderList.as_view()),
    path('order/<int:pk>/', OrderDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
