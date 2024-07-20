from django.shortcuts import render,get_object_or_404
from .models import ImageVarient,Product,Address,CartItem
import json
import time
from django.shortcuts import redirect
from django.contrib import messages
# Create your views here.
def home(request):
    products = Product.objects.prefetch_related('images').all()
    products_data = []
    
    for product in products:
        first_image_url = product.images.first().img.url if product.images.exists() else None
        products_data.append({
            'product': product,
            'first_image_url': first_image_url
        })
    print(products_data)
    return render(request,'newCourture.html',{'products': products_data})


def old(request):
    products = Product.objects.prefetch_related('images').all().order_by('-price')
    products_data = []
    
    for product in products:
        first_image_url = product.images.first().img.url if product.images.exists() else None
        products_data.append({
            'product': product,
            'first_image_url': first_image_url
        })
    print(products_data)
    return render(request,'newCourture.html',{'products': products_data})


def details(request,id):
    products_data=get_object_or_404(Product,id=id)
    images = products_data.images.all()  
    first_image = products_data.images.first()
    # Access related images
    context = {
        'product': products_data,
        'images': images,
        'first_image':first_image
    }
    added_item = request.GET.get('added')
    if added_item:
        messages.success(request, f'{added_item[:10]}..has been added to your cart!')
   
    return render(request,'oneCourture.html',context)
def cart(request):
    if request.method == 'POST':
        number = request.POST.get('number')
        city = request.POST.get('city')
        state = request.POST.get('state')
        address = request.POST.get('address')
        cart_items = request.POST.get('cart_items')  # Get the cart items
         # Create and save the Address
        address = Address.objects.create(
            number=number,
            city=city,
            state=state,
            address=address
        )

        # Convert cart_items from JSON string to Python list
        if cart_items:
            try:
                cart_items_list = json.loads(cart_items)
                # Save each cart item
                for item in cart_items_list:
                    CartItem.objects.create(
                        address=address,
                        name=item['name'],
                        price=item['price'],
                        quantity=item.get('quantity', 1)  # Default quantity to 1 if not provided
                    )
            except json.JSONDecodeError:
                pass
    added_item = request.GET.get('added')
    print(added_item,'====================')
    if added_item:
        messages.success(request, f'Your Order Has been Booked')
       
    return render(request,'cart.html')
