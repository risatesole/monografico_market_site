from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product, AddProductRequest, SellProductRequest, ProductBatch


def provider_view(request):
    if request.method == 'POST':
        form_type = request.POST.get('form_type')

        if form_type == 'create_product':
            name = request.POST.get('name')
            description = request.POST.get('description')
            photo = request.FILES.get('photo')
            category_id = request.POST.get('category')
            category = Category.objects.get(id=category_id)
            product = Product()
            product.name = name
            product.description = description
            product.photo = photo
            product.category = category
            product.save()
            return redirect('/provider')

        if form_type == 'request_category':
            name = request.POST.get('name')
            description = request.POST.get('description')
            add_request = AddProductRequest()
            add_request.name = name
            add_request.description = description
            add_request.status = 'pending'
            add_request.save()
            return redirect('/provider')

        if form_type == 'sell_product':
            provider_name = request.POST.get('provider_name')
            product_id = request.POST.get('product')
            quantity = request.POST.get('quantity')
            product = Product.objects.get(id=product_id)
            sell_request = SellProductRequest()
            sell_request.provider_name = provider_name
            sell_request.product = product
            sell_request.quantity = quantity
            sell_request.status = 'pending'
            sell_request.save()
            return redirect('/provider')

    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'provider.html', context)


def employee_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'accept_add_request':
            request_id = request.POST.get('request_id')
            add_request = get_object_or_404(AddProductRequest, id=request_id)
            add_request.status = 'accepted'
            add_request.save()
            new_category = Category()
            new_category.name = add_request.name
            new_category.save()
            return redirect('/employee')

        if action == 'reject_add_request':
            request_id = request.POST.get('request_id')
            add_request = get_object_or_404(AddProductRequest, id=request_id)
            add_request.status = 'rejected'
            add_request.save()
            return redirect('/employee')

        if action == 'accept_sell_request':
            request_id = request.POST.get('request_id')
            sell_request = get_object_or_404(SellProductRequest, id=request_id)
            sell_request.status = 'accepted'
            sell_request.save()
            batch = ProductBatch()
            batch.product = sell_request.product
            batch.quantity = sell_request.quantity
            batch.save()
            return redirect('/employee')

        if action == 'reject_sell_request':
            request_id = request.POST.get('request_id')
            sell_request = get_object_or_404(SellProductRequest, id=request_id)
            sell_request.status = 'rejected'
            sell_request.save()
            return redirect('/employee')

    pending_add_requests = AddProductRequest.objects.filter(status='pending')
    pending_sell_requests = SellProductRequest.objects.filter(status='pending')
    context = {
        'pending_add_requests': pending_add_requests,
        'pending_sell_requests': pending_sell_requests,
    }
    return render(request, 'employee.html', context)