from rest_framework import serializers
from .models import BMIHistory

class BMIHistorySerializer(serializers.ModelSerializer):
    condition = serializers.CharField()

    class Meta:
        model = BMIHistory
        fields = ['id', 'height', 'weight', 'bmi_value', 'condition', 'date']
