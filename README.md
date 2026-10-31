# Simple LMS Backend

Proyek backend Simple LMS berbasis Python, Django, PostgreSQL, dan Docker.

## Cara Menjalankan Proyek

### 1. Jalankan Container

Jalankan service Django (`app`) dan PostgreSQL (`db`) di latar belakang (_detached mode_):

```bash
docker compose up -d
```

### 2. Jalankan Migrasi Database

Buat skema dan tabel-tabel awal pada database PostgreSQL:

```bash
docker compose exec app python manage.py migrate
```

### 3. (Opsional) Buat Superuser / Admin

Untuk mengakses Django Admin dashboard:

```bash
docker compose exec app python manage.py createsuperuser
```

### 4. Membuka Aplikasi

Aplikasi dapat diakses melalui browser atau API client di:

- **Web App:** [http://localhost:8000](http://localhost:8000)
- **Django Admin:** [http://localhost:8000/admin](http://localhost:8000/admin)

---

## Perintah Penting Lainnya

- **Melihat status container:**

```bash
docker compose ps
```

- **Masuk ke Django Interactive Shell:**

```bash
docker compose exec app python manage.py shell
```

- **Menghentikan container:**

```bash
docker compose down
```
