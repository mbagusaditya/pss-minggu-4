from django.db import connection
from django.test.utils import CaptureQueriesContext

from catalog.models import Course

with CaptureQueriesContext(connection) as ctx:
    courses = (
        Course.objects.filter(code__startswith="PERF")
        .order_by("code")
        .prefetch_related("lessons")[:50]
    )
    for course in courses:
        titles = [lesson.title for lesson in course.lessons.all()]
    print("Jumlah query AFTER:", len(ctx.captured_queries))
