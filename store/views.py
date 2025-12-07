from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, OrderRequest
from django.core.paginator import Paginator
from .models import Category


def home(request):
    q = request.GET.get('q', '')
    category_id = request.GET.get('category', '')
    sort = request.GET.get('sort', '')
    min_price = request.GET.get('min', '')
    max_price = request.GET.get('max', '')

    product_list = Product.objects.filter(name__icontains=q)

    if category_id:
        product_list = product_list.filter(category_id=category_id)

    # PRICE FILTER
    if min_price:
        product_list = product_list.filter(price__gte=min_price)

    if max_price:
        product_list = product_list.filter(price__lte=max_price)

    # SORTING
    if sort == 'low':
        product_list = product_list.order_by('price')
    elif sort == 'high':
        product_list = product_list.order_by('-price')

    paginator = Paginator(product_list, 8)
    page = request.GET.get('page')
    products = paginator.get_page(page)

    categories = Category.objects.all()

    return render(request, 'store/home.html', {
        'products': products,
        'query': q,
        'categories': categories
    })





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
