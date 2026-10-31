from catalog.models import Course

# EXPLAIN Sebelum Index
qs_before = Course.objects.filter(code="PERF05000")
print("EXPLAIN Code Unique:")
print(qs_before.explain())

# EXPLAIN Setelah Menambahkan Indexes pada models.py
qs_after = Course.objects.filter(is_active=True, title="Performance Course 5000")
print("EXPLAIN Composite Index (is_active, title):")
print(qs_after.explain())
