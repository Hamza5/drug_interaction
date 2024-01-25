import csv
from argparse import FileType

from django.core.management.base import BaseCommand
from django.conf import settings
from tqdm import tqdm

from drug_interaction.models import Drug, ATCCode, ProductName


class Command(BaseCommand):
    help = 'Imports data from ATC_AGENT_CSV, ATC_PRODUCTNAME_CSV, and AGENT_PRODUCTNAME_CSV'
    requires_migrations_checks = True

    def add_arguments(self, parser):
        parser.add_argument(
            '--atc_productname_csv', type=FileType('r'), help='Path to ATC_PRODUCTNAME_CSV',
            default=settings.ATC_PRODUCTNAME_CSV
        )
        parser.add_argument(
            '--atc_agent_csv', type=FileType('r'), help='Path to ATC_AGENT_CSV',
            default=settings.ATC_AGENT_CSV
        )
        parser.add_argument(
            '--agent_productname_csv', type=FileType('r'), help='Path to AGENT_PRODUCTNAME_CSV',
            default=settings.AGENT_PRODUCTNAME_CSV
        )
        parser.add_argument(
            '--max_lines', type=int, help='Maximum number of lines to read from CSV files',
            default=settings.MAX_LINES
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.NOTICE(f'Importing data from {options["atc_productname_csv"]}'))
        reader = csv.reader(options['atc_productname_csv'])
        for row, _ in zip(tqdm(reader), range(options['max_lines'])):
            atc_code, product_name = row
            atc_code_obj, _ = ATCCode.objects.get_or_create(code=atc_code)
            product_name_obj, _ = ProductName.objects.get_or_create(name=product_name)
            product_name_obj.save()
            atc_code_obj.save()
        self.stdout.write(self.style.NOTICE(f'Importing data from {options["atc_agent_csv"]}'))
        reader = csv.reader(options['atc_agent_csv'])
        for row, _ in zip(tqdm(reader), range(options['max_lines'])):
            atc_code, agent_name = row
            atc_code_obj, _ = ATCCode.objects.get_or_create(code=atc_code)
            agent_name_obj, _ = Drug.objects.get_or_create(name=agent_name)
            agent_name_obj.atc_codes.add(atc_code_obj)
            agent_name_obj.save()
            atc_code_obj.save()
        self.stdout.write(self.style.NOTICE(f'Importing data from {options["agent_productname_csv"]}'))
        reader = csv.reader(options['agent_productname_csv'])
        for row, _ in zip(tqdm(reader), range(options['max_lines'])):
            agent_name, product_name = row
            agent_name_obj, _ = Drug.objects.get_or_create(name=agent_name)
            product_name_obj, _ = ProductName.objects.get_or_create(name=product_name)
            agent_name_obj.product_names.add(product_name_obj)
            agent_name_obj.save()
            product_name_obj.save()
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))
