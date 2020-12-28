import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from stores import models as store_models
from filters import models as filter_models
from products import models as product_models


class Command(BaseCommand):

    help = "This command creates many products"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=1, type=int, help="How many users do you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        stores = store_models.Store.objects.all()
        filters = filter_models.Filter.objects.all()
        specs1 = product_models.Specs.objects.all()

        seeder.add_entity(
            product_models.Product,
            number,
            {
                "product_name": lambda x: seeder.faker.address(),
                "store": lambda x: random.choice(stores),
                "catogary": lambda x: random.choice(filters),
                "specs": lambda x: random.choice(specs1),
            },
        )

        created_photos = seeder.execute()
        created_clean = flatten(list(created_photos.values()))
        for pk in created_clean:
            product = product_models.Product.objects.get(pk=pk)
            for i in range(3, random.randint(10, 17)):
                product_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    product=product,
                    file=f"products/shoes{random.randint(1,31)}.jpg",
                )
        self.stdout.write(self.style.SUCCESS("users created"))