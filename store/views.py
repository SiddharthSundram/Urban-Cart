from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Product, Category, OrderRequest


def clean_param(value):
    """Safely clean GET inputs: remove spaces, handle empty or invalid values."""
    if value is None:
        return None
    value = value.strip()
    return value if value != "" else None


def home(request):

    # Start with ALL products, ordered (fixes paginator warning)
    products_qs = Product.objects.all().order_by("-id")

    # Clean input params
    q = clean_param(request.GET.get("q"))
    category_id = clean_param(request.GET.get("category"))
    min_price = clean_param(request.GET.get("min"))
    max_price = clean_param(request.GET.get("max"))
    sort_by = clean_param(request.GET.get("sort"))
    page_num = clean_param(request.GET.get("page"))

    # -------------------------
    # APPLY FILTERS CLEANLY
    # -------------------------

    # 1. Search (name + description)
    if q:
        products_qs = products_qs.filter(
            Q(name__icontains=q) | Q(description__icontains=q)
        )

    # 2. Category Filter (SAFE conversion)
    if category_id:
        try:
            products_qs = products_qs.filter(category_id=int(category_id))
        except ValueError:
            pass  # ignore invalid values (Amazon-style fallback)

    # 3. Min Price
    if min_price:
        try:
            products_qs = products_qs.filter(price__gte=float(min_price))
        except ValueError:
            pass

    # 4. Max Price
    if max_price:
        try:
            products_qs = products_qs.filter(price__lte=float(max_price))
        except ValueError:
            pass

    # 5. Sorting
    if sort_by == "low":
        products_qs = products_qs.order_by("price")
    elif sort_by == "high":
        products_qs = products_qs.order_by("-price")

    # -------------------------
    # PAGINATION (ERROR-PROOF)
    # -------------------------

    paginator = Paginator(products_qs, 8)

    try:
        products = paginator.get_page(page_num)
    except:
        products = paginator.get_page(1)

    # -------------------------
    # SEND CONTEXT
    # -------------------------

    return render(request, "store/home.html", {
        "products": products,
        "categories": Category.objects.all(),

        # return cleaned params so UI stays consistent
        "q": q or "",
        "selected_category": category_id or "",
        "min_price": min_price or "",
        "max_price": max_price or "",
        "sort": sort_by or "",
    })


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        if name and phone and address:
            OrderRequest.objects.create(
                customer_name=name,
                customer_phone=phone,
                customer_address=address,
                product=product
            )
            return render(request, 'store/success.html')
            
    return render(request, 'store/product_detail.html', {'product': product})