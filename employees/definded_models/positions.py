import uuid
from django.db import models

from employees.definded_models.manager import CustomModelManager


class PositionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512, unique=True)
    description = models.TextField()
    objects = CustomModelManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = "position"
        verbose_name_plural = "positions"
        app_label = "employees"
