from django.http import HttpResponse
from django.shortcuts import render, redirect

from products.forms import ProductCreate
from products.models import Product

def index(request):
    products = Product.objects.all
    return render(request, "index.html", {'products': products})

def upload(request):
    form = ProductCreate()

    if request.method == 'POST':
      form = ProductCreate(request.POST)
      if form.is_valid():
        form.save()
        return redirect('index')
      else:
        return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
      return render(request, "product_form.html", {'form': form})
    
def delete(request, id):
    product_id = int(id)

    try:
      product = Product.objects.get(id = product_id)
    except Product.DoesNotExist:
      return redirect('index')
    product.delete()

    return redirect('index')