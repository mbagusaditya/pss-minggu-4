from django.db import connection
from django.test.utils import CaptureQueriesContext

from catalog.models import Course

with CaptureQueriesContext(connection) as ctx:
    rows = list(Course.objects.all())
    print("Jumlah Course:", len(rows))
    print("Jumlah query SQL:", len(ctx.captured_queries))
