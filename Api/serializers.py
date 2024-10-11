from rest_framework import serializers
from pvariants.models import Product, Product_Variant

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProductVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Variant
        fields = '__all__'
        
    def create(self, validated_data):
        variants_data = validated_data.pop('variants')
        product = Product.objects.create(**validated_data)
        for variant_data in variants_data:
            Product_Variant.objects.create(product=product, **variant_data)
        return product

