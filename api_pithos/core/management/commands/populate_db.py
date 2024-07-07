from django.core.management import BaseCommand
from django.db import transaction
from faker import Faker

from api_pithos.core.models import Employee
from api_pithos.core.models import Lead


class Command(BaseCommand):
    help = "Populate the database with some initial data"

    def add_arguments(self, parser):
        parser.add_argument(
            "--size",
            type=int,
            default=10,
            help="Number of leads to create",
        )

    def handle(self, *args, **options):
        fake = Faker()
        size = options["size"]

        with transaction.atomic():
            for _index in range(size):
                lead = Lead.objects.create(
                    linkedin_url=fake.url(),
                    is_demo_lead=fake.boolean(),
                    description=fake.text(),
                    n_employee=fake.random_int(min=1, max=100),
                    raw_json={
                        "key": fake.word(),
                        "value": fake.word(),
                    },
                    company_name_linkedin=fake.company(),
                    url=fake.url(),
                    urn=fake.uuid4(),
                    campaign_id=fake.uuid4(),
                )

                for _ in range(size):
                    Employee.objects.create(
                        lead=lead,
                        first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        urn=fake.uuid4(),
                        raw_json={
                            "key": fake.word(),
                            "value": fake.word(),
                        },
                    )
