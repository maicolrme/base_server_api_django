# Django REST API

API REST con **Django** + **DRF** + **PostgreSQL** + **JWT**, desplegable en Vercel.

➡️ **Producción:** [https://base-server-api-django.vercel.app](https://base-server-api-django.vercel.app)  
📖 **Swagger:** [https://base-server-api-django.vercel.app/ui/](https://base-server-api-django.vercel.app/ui/)  
🩺 **Health:** [https://base-server-api-django.vercel.app/health/](https://base-server-api-django.vercel.app/health/)

## Stack

| Capa | Tecnología |
|------|-----------|
| Framework | Django 5 |
| API | Django REST Framework |
| Auth | SimpleJWT (Bearer) |
| Docs | drf-spectacular (Swagger) |
| DB | PostgreSQL (Supabase) |
| Deploy | Vercel (Python Runtime) |

## Estructura

```
app/
├── auth/           Auth: register, login, me
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── items/          Items CRUD
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   └── urls.py
├── users/          Users CRUD
│   ├── views.py
│   └── urls.py
└── notifications/  FCM push
    ├── views.py
    └── urls.py
api/
├── settings.py
├── urls.py
├── wsgi.py
manage.py
vercel.json
```

## Instalación local

```bash
pip install uv
uv sync
uv run python manage.py runserver
```

## Deploy (Vercel)

1. Crear cuenta en [Vercel](https://vercel.com)
2. Conectar el repo de GitHub
3. Agregar env vars en Vercel Dashboard:
   - `DATABASE_URL`
   - `DJANGO_SECRET_KEY`
   - `JWT_SECRET`
   - `ALLOWED_HOSTS` = `*`
4. Deploy automático con cada push

## API Endpoints

| Método | Ruta | Auth | Descripción |
|--------|------|------|-------------|
| POST | `/auth/register` | No | Registrar |
| POST | `/auth/login` | No | Login |
| GET | `/auth/me` | Sí | Usuario actual |
| GET | `/items/` | No | Listar items |
| GET | `/items/{id}/` | Sí | Ver item |
| POST | `/items/` | Sí | Crear item |
| PUT | `/items/{id}/` | Sí | Actualizar |
| DELETE | `/items/{id}/` | Sí | Eliminar |
| GET | `/users/` | Sí | Listar usuarios |
| GET | `/users/{id}/` | Sí | Ver usuario |
| POST | `/users/` | Sí | Crear usuario |
| PUT | `/users/{id}/` | Sí | Actualizar |
| DELETE | `/users/{id}/` | Sí | Eliminar |
| POST | `/notifications/send` | Sí | Enviar push |
| POST | `/notifications/test` | Sí | Test push |
| POST | `/notifications/register-token` | Sí | Registrar token |
| GET | `/ui/` | No | Swagger UI |
