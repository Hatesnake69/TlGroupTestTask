import uuid
from djmoney.models.fields import MoneyField
from django.db import models

from employees.definded_models.manager import CustomModelManager


class EmployeeModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512)
    employment_date = models.DateTimeField(auto_now_add=True, editable=False)
    salary = MoneyField(max_digits=14, decimal_places=2, default_currency='USD')
    position = models.ForeignKey(
        to="employees.PositionModel", name="position", on_delete=models.CASCADE
    )
    subdivision = models.ForeignKey(
        to="employees.SubdivisionModel", name="subdivision", on_delete=models.CASCADE
    )
    objects = CustomModelManager()


    class Meta:
        managed = True
        db_table = "employee"
        verbose_name_plural = "Employees"
        app_label = 'employees'
