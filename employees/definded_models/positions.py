import uuid

from django.db import models


class PositionModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=512)
    description = models.TextField()

    class Meta:
        managed = True
        db_table = "position"
        verbose_name_plural = "positions"
        app_label = 'employees'
