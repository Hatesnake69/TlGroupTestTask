from django.shortcuts import render
from employees.models import EmployeeModel, SubdivisionModel
from django.shortcuts import redirect


def index(request):
    root = SubdivisionModel.objects.get(parent_id=None)
    viewed_subdivisions = SubdivisionModel.objects.filter(parent_id=root.id)
    viewed_employees = EmployeeModel.objects.filter(subdivision_id=root.id)
    return render(
        request,
        "employees/index.html",
        {
            "root": root,
            "viewed_subdivisions": viewed_subdivisions,
            "viewed_employees": viewed_employees,
        },
    )


def list_all_subdivision_elements(request, subdivision_id):

    root = SubdivisionModel.objects.get(pk=subdivision_id)
    viewed_subdivisions = SubdivisionModel.objects.filter(parent_id=root.id)
    viewed_employees = EmployeeModel.objects.filter(subdivision_id=subdivision_id)
    return render(
        request,
        "employees/index.html",
        {
            "root": root,
            "viewed_subdivisions": viewed_subdivisions,
            "viewed_employees": viewed_employees,
        },
    )


def redirect_view(request):
    response = redirect("/subdivision/")
    return response
