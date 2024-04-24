from django.urls import path
from .views import CalculateBMI, BMIHistoryList, DeleteBMIHistory

urlpatterns = [
    path('calculate/', CalculateBMI.as_view(), name='calculate_bmi'),
    path('history/', BMIHistoryList.as_view(), name='bmi_history'),
    path('history/<int:pk>/', DeleteBMIHistory.as_view(), name='delete_bmi_history'),
]
