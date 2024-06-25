from django.db import models

# Create your models here.
class User(models.Model):
    govt_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    Gender=models.CharField(max_length=50)
    total_cases=models.IntegerField()
    cases_names=models.CharField(max_length=100)
    case_durations=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
