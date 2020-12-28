import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from stores import models as store_models
from filters import models as filter_models


class Command(BaseCommand):

    help = "This command creates many filters"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        stores = store_models.Store.objects.all()

        seeder.add_entity(
            filter_models.Filter,
            number,
            {
                "filter_name": lambda x: seeder.faker.address(),
                "store": lambda x: random.choice(stores),
                "image": f"filter_photo/{random.randint(1,30)}.png",
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS("users created"))