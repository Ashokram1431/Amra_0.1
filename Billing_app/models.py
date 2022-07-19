from django.db import models

# Create your models here.

UNIT_VALUE=(
('nos','NOS'),('ml','ML'),
)

class Medicine(models.Model):
    drug_code=models.IntegerField()
    medicine_name=models.CharField(max_length=100)
    unit_size=models.IntegerField()
    unit_value=models.CharField(max_length=5, choices=UNIT_VALUE, default='nos')
    mrp=models.FloatField()
