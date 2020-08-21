from django.shortcuts import render
from .models import Product


# SQL INJECTION QUERY
# SELECT * FROM example2_product WHERE instr(name, '%s') 
# SELECT * FROM example2_product WHERE instr(name, 'asdf') OR 1=1 UNION SELECT 1,2,3,4 FROM example2_secret--')
# asdf%27)+UNION+SELECT+1,2,text,4,title+FROM+example2_secret-- ### TO DO URL
# asdf') UNION SELECT 1,2,text,4,title FROM example2_secret-- ### TO DO SZUKAJKI

# Create your views here.
def index(request):
    search = request.GET.get('search')
    if search:
        query = "SELECT * FROM example2_product \
            WHERE instr(name, '%s') AND is_secret=0" 
        products = Product.objects.raw(query % search) 
    else:
        products = Product.objects.filter(is_secret=False)

    context = {
        'products': products,
        'search': search
    }
    return render(request, 'example2/index.html', context)

def index_ok(request):
    search = request.GET.get('search')
    if search:
        products = Product.objects.filter(
            is_secret=False, 
            name__contains=search) 
    else:
        products = Product.objects.filter(is_secret=False)

    context = {
        'products': products,
        'search': search
    }
    return render(request, 'example2/index.html', context)

def product_detail_view(request, pk):
    #product = Product.objects.extra(where=("id=%s") %(pk) )
    product = Product.objects.raw('SELECT * FROM example2_product WHERE id=%s' %(pk))
    print(product)
    context = {'product': product[0]}
    return render(request, 'example2/details.html', context)

