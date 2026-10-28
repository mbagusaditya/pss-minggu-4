from django.db.models import Count

from catalog.models import Course, Enrollment

# Percobaan A: exists()
course = Course.objects.get(code="PERF00001")
ada_mahasiswa = Enrollment.objects.filter(course=course).exists()
print("Ada mahasiswa terdaftar:", ada_mahasiswa)

# Percobaan B: count()
jumlah_course = Course.objects.filter(code__startswith="PERF").count()
print("Jumlah Course simulasi:", jumlah_course)

# Percobaan C: values()
courses_val = Course.objects.filter(code__startswith="PERF").values("code", "title")[:5]
for c in courses_val:
    print(c)

# Percobaan D: annotate()
courses_ann = (
    Course.objects.filter(code__startswith="PERF")
    .annotate(jumlah_mahasiswa=Count("enrollments"))
    .order_by("code")[:5]
)
for c in courses_ann:
    print(c.code, c.jumlah_mahasiswa)
