from django.core.management.base import BaseCommand
from employees.models import PositionModel, SubdivisionModel, EmployeeModel


class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        positions_set = {
            ("junior dev", "junior python backend developer"),
            ("middle_dev", "middle python backend developer"),
            ("team_lead", "senior python backend developer, team lead"),
            ("project_manager", "project manager"),
            ("tech_lead", "tech lead"),
        }
        for elem in positions_set:
            PositionModel(name=elem[0], description=elem[1]).save()
        subdivisions_set = {
            ("junior dev", "junior python backend developer"),
            ("middle_dev", "middle python backend developer"),
            ("team_lead", "senior python backend developer, team lead"),
            ("project_manager", "project manager"),
            ("tech_lead", "tech lead"),
        }

        self.stdout.write("data population complete")

