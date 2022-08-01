
from django.contrib import admin
from django.urls import path
from setup.escola import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('alunos/', views.alunos),
]
