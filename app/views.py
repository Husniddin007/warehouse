from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializers import ProductSerializer, MaterialSerializer, ProductMaterialsSerializer, WarehouseSerializer
from app.models import Product, ProductMaterials, Warehouse, Material


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


class ProductMaterialsViewSet(viewsets.ModelViewSet):
    queryset = ProductMaterials.objects.all()
    serializer_class = ProductMaterialsSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class GetMaterials(APIView):

    def post(self, request):
        productss = request.data.get('products', [])
        result = []

        for p in productss:
            product = Product.objects.get(name=p['product_name'])
            product_materials = ProductMaterials.objects.filter(product=product)
            materials = []

            for pm in product_materials:
                total = pm.quantity * p['qty']
                warehouse = Warehouse.objects.filter(material=pm.material).order_by('id')

                for w in warehouse:
                    if total <= 0:
                        break

                    if w.remainider > total:
                        materials.append({
                            'warehouse_id': w.id,
                            'material_name': pm.material.name,
                            'qty': w.remainder,
                            'price': w.price
                        })
                        total_needed = 0
                    else:
                        materials.append({
                            'warehouse_id': w.id,
                            'material_name': pm.material.name,
                            'qty': w.remainder,
                            'price': w.price
                        })
                        total -= w.remainder
                if total > 0:
                    materials.append({
                        'warehouse_id': None,
                        'material_name': pm.material.name,
                        'qty': total,
                        'price': None
                    })
            result.append({
                'product_name': product.name,
                'product_qty': p['qty'],
                'product_materials': materials,
            })
        return Response({'result': result})
