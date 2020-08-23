from rest_framework import serializers
from .models import Product

# serializer를 활용하면 request로 받은 data를 역직렬화하여 DB에 반영하고
# response로 사용 될 data를 다시 직렬화아혀 json이나 xml 등으로 쉽게 변환 가능
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        # 모델 Product의 모든 field serializer함
        fields = '__all__' 