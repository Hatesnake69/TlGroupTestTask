from django.core.management.base import BaseCommand
import random
import names

from employees.models import PositionModel, SubdivisionModel, EmployeeModel


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        self.stdout.write("data population begin")
        positions_set = {
            ("junior dev", "junior python backend developer"),
            ("middle dev", "middle python backend developer"),
            ("team lead", "senior python backend developer, team lead"),
            ("project manager", "project manager"),
            ("tech lead", "tech lead"),
        }
        for elem in positions_set:
            PositionModel(name=elem[0], description=elem[1]).save()
        root_node = SubdivisionModel(name="root division", description="description")
        root_node.save()
        for i in range(1, 6):
            for j in range(4):
                sub_root_node = SubdivisionModel(
                    name=f"child division number {j} of {i}layer",
                    description="description",
                    parent=root_node,
                )
                sub_root_node.save()
                for k in range(3):
                    SubdivisionModel(
                        name=f"child sub division number {k} of {j} division",
                        description="description",
                        parent=sub_root_node,
                    ).save()
            root_node = SubdivisionModel(
                name=f"child division number 4 of {i}layer",
                description="description",
                parent=root_node,
            )
            root_node.save()

        subdivisions_number = len(SubdivisionModel.objects.all())
        positions_number = len(PositionModel.objects.all())

        for i in range(50000):

            EmployeeModel(
                name=names.get_full_name(),
                salary=random.randint(1000, 10000),
                salary_currency="USD",
                position=PositionModel.objects.all()[
                    random.randint(0, positions_number - 1)
                ],
                subdivision=SubdivisionModel.objects.all()[
                    random.randint(0, subdivisions_number - 1)
                ],
            ).save()

        self.stdout.write("data population completed")
