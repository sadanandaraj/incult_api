import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from stores import models as store_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        store_types = store_models.StoreType.objects.all()

        seeder.add_entity(
            store_models.Store,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "owner": lambda x: random.choice(all_users),
                "storeType": lambda x: random.choice(store_types),
                "logo": f"store_logo/{random.randint(1,25)}.png",
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS("users created"))