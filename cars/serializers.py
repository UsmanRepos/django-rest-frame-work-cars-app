from rest_framework import serializers
from .models import Car, CarPlan

class CarPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarPlan
        fields = ['id', 'name', 'description', 'price', 'features']


def validate_length_of_brand(value):
    if len(value) > 15:
        raise serializers.ValidationError("Length of brand should be less than 15 characters")
    return value

def validate_length_of_model(value):
    if len(value) > 15:
        raise serializers.ValidationError("Length of model should be less than 15 characters")
    return value

class CarSerializer(serializers.ModelSerializer):
    plan = CarPlanSerializer()
    class Meta:
        model = Car
        fields = ['id', 'plan', 'brand', 'model', 'production_year', 'engine_type', 'car_body']
        extra_kwargs = {
            'brand': {'validators': [validate_length_of_brand]},
            'model': {'validators': [validate_length_of_model]}
        }
        # depth = 1

    def create(self, validated_data):
        plan = validated_data.pop('plan')
        validated_data['plan'] = CarPlan.objects.get(name=plan.get('name'))
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        plan = validated_data.pop('plan')
        validated_data['plan'] = CarPlan.objects.get(name=plan.get('name'))
        return super().update(instance, validated_data)





