import uuid
from django.db import models

from employees.definded_models.manager import CustomModelManager


class SubdivisionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512)
    description = models.TextField()
    parent = models.ForeignKey(
        to="employees.SubdivisionModel", name="parent", on_delete=models.CASCADE,
        blank=True, null=True
    )
    objects = CustomModelManager()

    class Meta:
        managed = True
        db_table = "subdivision"
        verbose_name_plural = "subdivisions"
        app_label = 'employees'
