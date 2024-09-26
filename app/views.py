from django.http import JsonResponse
from app.models import Product, ProductMaterials, Warehouse


def get_materials(request):
    products_to_produce = [
        {'product_name': 'SHim', 'qty': 30},
        {'product_name': 'Ko`ylak', 'qty': 30}
    ]
    result = []

    for product_data in products_to_produce:
        product = Product.objects.get(product_name=product_data['product_name'])
        product_materials = ProductMaterials.objects.filter(product=product)
        materials_needed = []

        for pm in product_materials:
            total_needed = pm.quantity * product_data['qty']
            warehouse_batches = Warehouse.objects.filter(material=pm.material).order_by('id')

            for batch in warehouse_batches:
                if total_needed <= 0:
                    break

                if batch.remaining_quantity > total_needed:
                    materials_needed.append({
                        'warehouse_id': batch.id,
                        'material_name': pm.material.material_name,
                        'qty': batch.remaining_quantity,
                        'price': batch.price
                    })
                    total_needed = 0
                else:
                    materials_needed.append({
                        'warehouse_id': batch.id,
                        'material_name': pm.material.material_name,
                        'qty': batch.remaining_quantity,
                        'price': batch.price
                    })
                    total_needed -= batch.remaining_quantity
            if total_needed > 0:
                materials_needed.append({
                    'warehouse_id': None,
                    'material_name': pm.material.material_name,
                    'qty': batch.remaining_quantity,
                    'price': None
                })
        result.append({
            'product_name': product.product_name,
            'product_qty': product_data['qty'],
            'product_materials': materials_needed,
        })
    return JsonResponse({'result': result})
