from django.core.management.base import BaseCommand

from catalog.models import Course
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        lecturer = User.objects.get(username="suprayogi")
        courses = [
            {
                "code": "PSS01",
                "title": "Pemrograman Sisi Server",
                "description": "Belajar backend development dengan Django.",
            },
            {
                "code": "PSS02",
                "title": "Django Framework",
                "description": "Mempelajari framework Django dan struktur project.",
            },
            {
                "code": "PSS03",
                "title": "Django ORM",
                "description": "Mempelajari database dan ORM menggunakan Django.",
            },
            {
                "code": "PSS04",
                "title": "REST API",
                "description": "Mempelajari pembuatan REST API dengan Django.",
            },
            {
                "code": "PSS05",
                "title": "Docker",
                "description": "Mempelajari containerisasi aplikasi Django.",
            },
        ]
        for data in courses:
            Course.objects.get_or_create(
                code=data["code"],
                defaults={
                    "title": data["title"],
                    "description": data["description"],
                    "lecturer": lecturer,
                },
            )
        self.stdout.write(self.style.SUCCESS("Sample courses berhasil dibuat"))
