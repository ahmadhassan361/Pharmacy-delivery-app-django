from rest_framework import serializers
from .models import Medicines, OrderMedicine, Orders, Slider,UploadPrescription

class MedicinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicines
        fields = '__all__'
class OrderMedicineSerializer(serializers.ModelSerializer):
    medicine = serializers.PrimaryKeyRelatedField(queryset=Medicines.objects.all())

    class Meta:
        model = OrderMedicine
        fields = ['medicine', 'quantity']

    def create(self, validated_data):
        medicine = validated_data['medicine']
        order_medicine = OrderMedicine.objects.create(medicine=medicine, **validated_data)
        return order_medicine

class OrdersSerializer(serializers.ModelSerializer):
    medicines = OrderMedicineSerializer(many=True)

    class Meta:
        model = Orders
        fields = ['name', 'phone', 'address', 'note', 'medicines', 'order_status','prescription']

    def create(self, validated_data):
        medicines_data = validated_data.pop('medicines')
        order = Orders.objects.create(**validated_data)

        for medicine_data in medicines_data:
            medicine = medicine_data.pop('medicine')
            order_medicine = OrderMedicine.objects.create(medicine=medicine, **medicine_data)
            order.medicines.add(order_medicine)

        return order
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPrescription
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'