from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import GetMaterials, ProductMaterialsViewSet, MaterialViewSet, ProductViewSet, WarehouseViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'warehouses', WarehouseViewSet)
router.register(r'products-materials', ProductMaterialsViewSet)

urlpatterns = [
    path('app', include(router.urls)),
    path('app/get_materials/', GetMaterials.as_view(), name='get_materials'),
]
