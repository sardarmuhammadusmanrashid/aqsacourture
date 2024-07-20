from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from keen_app.models import Product
def home(request):
    return render(request,'index.html')
def success(request):
    return render(request,'success.html')
def cancel(request):
    return render(request,'cancel.html')

def landing(request,id):
    data=Product.objects.get(id=id)
    return render(request,'landing_page.html',{"data":data})



