from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import OrderSerializer
from .models import Order

"""
    Django REST framework는 단일 클래스에 관련 있는 view들을 결합한 ViewSet 기능을 제공한다
    즉, ViewSet은 여러 가지 API의 기능을 통합해서 하나의 API Set로 제공한다 
"""

class OrderList(APIView):
    def get(self, request): # Show List
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = OrderSerializer(
            data = request.data
        ) # request.data는 사용자 입력 데이터

        if serializer.is_valid():
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class OrderDetail(APIView):
    def get_object(self, pk): # Order 객체 가져오기
        try:
            return Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None): # Order Detail 보기
        order = self.get_object(pk)
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None): # Order 삭제
        order = self.get_object(pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)