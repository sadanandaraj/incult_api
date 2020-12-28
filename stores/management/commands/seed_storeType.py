from django.core.management.base import BaseCommand
from stores.models import StoreType


class Command(BaseCommand):

    help = "This command creates store types"

    def handle(self, *args, **options):
        storeType = [
            "Fashion and accessories",
            "CE or Electro",
            "Jewellery and watches",
            "FMCG and grocery",
            "Leisure and hobby",
            "Office and stationary",
            "Living and furnishing",
            "Health and wellness",
            "DIY and garden",
            "Hotels and bekaries",
        ]
        for s in storeType:
            StoreType.objects.create(name=s)
        self.stdout.write(self.style.SUCCESS("Store Types created"))