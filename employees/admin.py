from django.contrib import admin

from employees.definded_models.employees import EmployeeModel
from employees.definded_models.positions import PositionModel
from employees.definded_models.subdivisions import SubdivisionModel

# Register your models here.


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = [
        "id",
        "name",
        "employment_date",
        "salary",
        "position",
        "subdivision",
    ]
    list_display = [
        "id",
        "name",
        "employment_date",
        "salary",
        "position",
        "subdivision",
    ]


@admin.register(PositionModel)
class PositionAdmin(admin.ModelAdmin):
    """Admin class for chats"""

    search_fields = [
        "id",
        "name",
        "description",
    ]
    list_display = [
        "id",
        "name",
        "description",
    ]


@admin.register(SubdivisionModel)
class SubdivisionAdmin(admin.ModelAdmin):
    """Admin class for chats"""

    search_fields = [
        "id",
        "name",
        "description",
    ]
    list_display = [
        "id",
        "name",
        "description",
    ]
