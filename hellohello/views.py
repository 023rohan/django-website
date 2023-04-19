from django.shortcuts import render
from .models import Product,Contact,Order,Updateorder
from math import ceil
import json

# Create your views here.
from django.http import HttpResponse

def index(request):
   

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

  
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def searchMatch(query,item):
    if query in item.desc.lower() or query in item.name.lower() or query in item.category.lower():
        return True
    else:
        return False



def search(request):
    allProds = []
    query  = request.GET.get('search')
    print(query)
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prodtemp = Product.objects.filter(category=cat)
        prod = [item for item in prodtemp if searchMatch(query,item)]
        n = len(prodtemp)
        
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        print(len(prod))
        if len(prod) != 0:
            allProds.append([prod, range(1, nSlides), nSlides])

  
    params = {'allProds':allProds}
    if len(allProds) == 0 or len(query)<3:
        params = {'Msg':'PLease Enter relevant search query'}
    return render(request, 'shop/search.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    if request.method =="POST":
        print(request)
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name,email=email,phone=phone,desc=desc)
        contact.save()


    return render(request,'shop/contact.html')
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Order.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = Updateorder.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.update_time})
                    response = json.dumps([updates,order[0].item_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{}')
        except Exception as e:
            return HttpResponse(f"Exception{e}")

    return render(request, 'shop/tracker.html')



def productView(request,myid):
    #fetching the id of the product
    product = Product.objects.filter(id=myid)
    print(product)
    return render(request,'shop/prodview.html',{'product': product[0]})

def checkout(request):
    if request.method == "POST":
        item_json = request.POST.get('itemsJson','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','') +" " + request.POST.get('address1','')
        state = request.POST.get('state','')
        city = request.POST.get('city','')
        zip_code = request.POST.get('zip_code','')
        phone = request.POST.get('phone','')
       
        order = Order(item_json=item_json,name=name,email=email,address=address,state=state,city=city,zip_code=zip_code,phone=phone)
        order.save()
        update = Updateorder(order_id=order.order_id,update_desc=item_json)
        update.save()
        thank = True
        id = order.order_id
        return render(request,'shop/checkout.html',{'Thank':thank,'id':id})
    return render(request,'shop/checkout.html')