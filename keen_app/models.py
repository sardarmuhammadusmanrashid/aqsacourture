from typing import Iterable
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver


# Create your models here.
class Category(models.Model):
    cat_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,blank=True)
    def save(self,*args,**kwargs):
        self.slug=slugify(self.cat_name)
        return super(Category,self).save(*args,**kwargs)
    def __str__(self):
        return str(self.cat_name)
class ColorVariant(models.Model):
    c_name=models.CharField(max_length=100)
    c_color=models.CharField(max_length=100)
    def __str__(self):
        return str(self.c_name)
class SizeVariant(models.Model):
    s_size=models.CharField(max_length=100)
    def __str__(self):
            return str(self.s_size)

class Product(models.Model):
    category= models.CharField(max_length=100)
    color=models.CharField(max_length=100)
    size=models.CharField(max_length=100)
    p_name=models.CharField(max_length=100)
    price=models.IntegerField(default=10)
    def __str__(self):
        return str(self.p_name)
class ImageVarient(models.Model):
    img=models.ImageField(upload_to='images_') 
    p_product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='images')
class Buy_product(models.Model):
    location=models.CharField(max_length=100)
    product_name=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_buy=models.BooleanField(default=False)
    def __str__(self):
        return str(self.location)

# @receiver(pre_save, sender=SizeVariant)
# def update_stock(sender, **kwargs):
#     data=kwargs['instance']
#     print('........................',data,data.s_size)
#     if data.s_size=='Small':
#         print('yes')
#         data.s_size='Greater'
#     print(kwargs)

class Address(models.Model):
    number = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.number}, {self.city}, {self.state}, {self.address}"

class CartItem(models.Model):
    address = models.ForeignKey(Address, related_name='cart_items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name} - {self.price} x {self.quantity}"
