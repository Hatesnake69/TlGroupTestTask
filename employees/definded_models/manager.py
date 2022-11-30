from django.db import models


class CustomModelManager(models.Manager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)