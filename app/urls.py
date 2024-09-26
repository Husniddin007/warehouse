from django.urls import path
from app.views import get_materials

urlpatterns = [
    path('app/get_materials/', get_materials,name='get_materials'),
]



