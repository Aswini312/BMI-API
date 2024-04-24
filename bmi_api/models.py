from django.db import models

class BMIHistory(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    bmi_value = models.FloatField()
    condition = models.CharField(max_length=20, default='Unknown')  # Providing a default value
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'BMI: {self.bmi_value} | Height: {self.height}m | Weight: {self.weight}kg | Condition: {self.condition} | Date: {self.date}'
