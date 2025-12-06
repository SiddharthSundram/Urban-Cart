from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderRequest

def home(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        address = request.POST['address']

        OrderRequest.objects.create(
            customer_name=name,
            customer_phone=phone,
            customer_address=address,
            product=product
        )
        return render(request, 'store/success.html')

    return render(request, 'store/product_detail.html', {'product': product})
