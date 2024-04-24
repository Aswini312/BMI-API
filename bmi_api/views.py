from rest_framework import generics
from rest_framework.response import Response
from .models import BMIHistory
from .serializers import BMIHistorySerializer

class CalculateBMI(generics.CreateAPIView):
    serializer_class = BMIHistorySerializer

    def post(self, request, *args, **kwargs):
        height = float(request.data.get('height'))
        weight = float(request.data.get('weight'))
        bmi = weight / (height ** 2)
        
        # Determine BMI condition
        if bmi < 18.5:
            condition = 'Underweight'
        elif bmi < 24.9:
            condition = 'Normal weight'
        elif bmi < 29.9:
            condition = 'Overweight'
        else:
            condition = 'Obese'
        
        bmi_history = BMIHistory.objects.create(height=height, weight=weight, bmi_value=bmi, condition=condition)
        serializer = self.get_serializer(bmi_history)
        return Response(serializer.data)

class BMIHistoryList(generics.ListAPIView):
    queryset = BMIHistory.objects.all().order_by('-date')
    serializer_class = BMIHistorySerializer

class DeleteBMIHistory(generics.DestroyAPIView):
    queryset = BMIHistory.objects.all()
    serializer_class = BMIHistorySerializer

    def get(self, request, *args, **kwargs):
        bmi_history = self.get_object()
        serializer = self.get_serializer(bmi_history)
        return Response(serializer.data)
