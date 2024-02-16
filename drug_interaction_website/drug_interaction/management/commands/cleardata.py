from django.core.management.base import BaseCommand

from drug_interaction.models import Drug, Interaction


class Command(BaseCommand):
    help = 'Clears all data from Drug and Interaction models in the database'

    def handle(self, *args, **options):
        Drug.objects.all().delete()
        Interaction.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared data'))
