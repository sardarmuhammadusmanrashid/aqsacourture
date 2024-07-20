from django.contrib import admin
from .models import Product,Buy_product,ImageVarient,SizeVariant,Category,ColorVariant,Address,CartItem
# Register your models here.
admin.site.register(Product)
admin.site.register(Buy_product)
admin.site.register(Category)
admin.site.register(ImageVarient)
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(Address)
admin.site.register(CartItem)