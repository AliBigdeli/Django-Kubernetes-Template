import time
from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    help = "check if database is online to proceed"

    def handle(self, *args, **kwargs):
        print("Start checking for database...")
        PGDB_conn = None
        while not PGDB_conn:
            try:
                PGDB_conn = connections["default"]
            except OperationalError:
                print("Database unavailable, waiting 1 second...")
                time.sleep(1)

        print("Database Available!")
