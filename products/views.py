from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from products.models import Product


def home(request):
    return render(request, 'products/home.html')


@login_required
def create(request):
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('body') and request.POST.get('url') \
                and request.FILES.get('icon') and request.FILES.get('image'):
            request_url = request.POST.get('url')

            product = Product()
            product.title = request.POST.get('title')
            product.body = request.POST.get('body')

            if request_url.startswith('http://') or request_url.startswith('https://'):
                product.url = request_url
            else:
                product.url = f'http://{request_url}'

            product.image = request.FILES.get('image')
            product.icon = request.FILES.get('icon')

            product.pub_date = timezone.datetime.now()
            product.hunter = request.user

            product.save()
            return redirect(f'/products/{product.id}')
        else:
            return render(request, 'products/create.html', {'error': 'All fields are required'})
    else:
        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})
