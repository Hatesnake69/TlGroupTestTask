import uuid
from django.db import models

from employees.definded_models.manager import CustomModelManager


class SubdivisionModel(models.Model):
    name = models.CharField(max_length=512)
    description = models.TextField()
    parent = models.ForeignKey(
        to="employees.SubdivisionModel",
        name="parent",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    objects = CustomModelManager()

    def __str__(self):
        return str(self.name)

    class Meta:
        managed = True
        db_table = "subdivision"
        verbose_name_plural = "subdivisions"
        app_label = "employees"
