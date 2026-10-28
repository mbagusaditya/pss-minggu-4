from django.db import connection
from django.test.utils import CaptureQueriesContext

from catalog.models import Course

with CaptureQueriesContext(connection) as ctx:
    courses = Course.objects.filter(code__startswith="PERF").order_by("code")[:50]
    for course in courses:
        titles = [lesson.title for lesson in course.lessons.all()]
    print("Jumlah query BEFORE:", len(ctx.captured_queries))
