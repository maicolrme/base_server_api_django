from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

def home(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Django API</title>
  <style>
    *{margin:0;padding:0;box-sizing:border-box}body{font-family:system-ui,sans-serif;background:#0f172a;color:#e2e8f0;min-height:100vh;display:flex;flex-direction:column;align-items:center;justify-content:center}
    h1{font-size:2.5rem;font-weight:700;margin-bottom:.5rem;background:linear-gradient(135deg,#60a5fa,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
    p{color:#94a3b8;margin-bottom:2rem;font-size:1.1rem}
    .links{display:flex;gap:1rem;flex-wrap:wrap;justify-content:center}
    .links a{padding:.75rem 1.5rem;border-radius:8px;text-decoration:none;font-weight:600;transition:.2s}
    .btn-docs{background:#2563eb;color:#fff}.btn-docs:hover{background:#1d4ed8}
    .btn-health{background:#1e293b;color:#e2e8f0;border:1px solid #334155}.btn-health:hover{background:#334155}
    .btn-doc{background:#059669;color:#fff}.btn-doc:hover{background:#047857}
    .features{display:flex;gap:2rem;margin-top:3rem;flex-wrap:wrap;justify-content:center}
    .feature{background:#1e293b;padding:1.25rem 2rem;border-radius:12px;min-width:200px;border:1px solid #334155}
    .feature h3{font-size:1rem;color:#60a5fa;margin-bottom:.5rem}
    .feature span{font-size:.85rem;color:#94a3b8}
  </style>
</head>
<body>
  <h1>Django API Server</h1>
  <p>REST API — Django + DRF + PostgreSQL + JWT</p>
  <div class="links">
    <a href="/ui/" class="btn-docs">Swagger Docs</a>
    <a href="/doc/" class="btn-doc">OpenAPI JSON</a>
    <a href="/health/" class="btn-health">Health Check</a>
  </div>
  <div class="features">
    <div class="feature"><h3>Auth</h3><span>JWT Bearer</span></div>
    <div class="feature"><h3>Database</h3><span>PostgreSQL</span></div>
    <div class="feature"><h3>Docs</h3><span>OpenAPI + Swagger</span></div>
    <div class="feature"><h3>Push</h3><span>FCM Notifications</span></div>
  </div>
</body>
</html>""")

def health(request):
    from django.http import JsonResponse
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path("", home, name="home"),
    path("health/", health, name="health"),
    path("admin/", admin.site.urls),
    path("auth/", include("app.authentication.urls")),
    path("items/", include("app.items.urls")),
    path("users/", include("app.users.urls")),
    path("notifications/", include("app.notifications.urls")),
    path("doc/", SpectacularAPIView.as_view(), name="schema"),
    path("ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger"),
]
