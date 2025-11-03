from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('estudantes', EstudanteViewSet, basename='Estudantes')
router.register('cursos', CursoViewSet, basename='Cursos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
