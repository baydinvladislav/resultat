import os
import csv
from config.settings import BASE_DIR
from .models import Table


PATH = 'media/'


def import_data(file_name, file_id):
    with open(os.path.join(BASE_DIR, PATH + file_name)) as f:
        reader = csv.reader(f)
        for row in reader:
            obj, created = Table.objects.get_or_create(
                document_id=file_id,
                number=row[0],
                date=row[1],
                project=row[2],
                price=row[3],
                available_numbers=row[4],
                used=row[4],
                remainder=row[5],
                source=row[6],
                how_collected=row[7],
                responsible=row[8],
                link=row[9],
                status=row[10],
                comment=row[11],
                price_per_number=row[12],
            )
