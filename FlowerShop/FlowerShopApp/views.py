from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Bouquet
def index(request):
    bouquets = Bouquet.objects.all()
    context = {'bouquet_list':bouquets, 'app_name':'FlowerShopApp'}
    return render(request, 'index.html', context)

@login_required
def product(request, id):
    try:
        bouquet = Bouquet.objects.get(id=id)
    except Bouquet.DoesNotExist:
        return index(request)
    data = {"bouquet" : bouquet}
    return render(request, "product.html", data)
