from rest_framework import serializers
from .models import Product

"""
    serialization(직렬화)은 컴퓨터 과학의 데이터 스토리지 문맥에서 
    데이터 구조나 오브젝트 상태를 동일하거나 다른 컴퓨터 환경에 저장하고 
    나중에 재구성할 수 있는 포맷으로 변환하는 과정이다
        
    즉, 어떤 모델 클래스에서 이 클래스 인스턴스가 어떻게 json 형태로 바뀌는지, 
    그리고 json 데이터는 어떻게 다시 클래스 인스턴스로 바뀌는지 정의를 하는 것이다
"""

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
