from django.core.management.base import BaseCommand
import random
import names

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
        root_node = SubdivisionModel(name="root_node", description="root_node")
        root_node.save()
        for i in range(1, 6):
            for j in range(4):
                SubdivisionModel(
                    name=f"child_node_number{j}_of_{i}_layer",
                    description="child_node",
                    parent=root_node
                ).save()
            root_node = SubdivisionModel(
                name=f"child_node_number{4}_of_{i}_layer",
                description="child_node",
                parent=root_node)
            root_node.save()

        self.stdout.write(f"Всего подразделений: {len(SubdivisionModel.objects.all())}")
        subdivisions_number = len(SubdivisionModel.objects.all())
        positions_number = len(PositionModel.objects.all())

        for i in range(50000):

            EmployeeModel(
                name=names.get_full_name(),
                salary=random.randint(1000, 10000),
                salary_currency="USD",
                position=PositionModel.objects.all()[random.randint(0, positions_number-1)],
                subdivision=SubdivisionModel.objects.all()[random.randint(0, subdivisions_number-1)],
            ).save()

        self.stdout.write("data population complete")

