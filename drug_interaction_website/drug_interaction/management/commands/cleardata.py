from django.core.management.base import BaseCommand

from drug_interaction.models import Drug, ATCCode, ProductName


class Command(BaseCommand):
    help = 'Clears all data from Drug, ATCCode, and ProductName'

    def handle(self, *args, **options):
        Drug.objects.all().delete()
        ATCCode.objects.all().delete()
        ProductName.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared data'))
