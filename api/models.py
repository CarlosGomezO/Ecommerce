from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Data(models.Model):
    
    def __str__(self):
        return f"Nombre: {self.name} - Email: {self.email} - Dni: {self.dni} "
    
    
    name = models.CharField(max_length=60)
    email = models.EmailField()
    dni = models.IntegerField()


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null= True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    

class Product(models.Model):
    name= models.CharField(max_length=200)
    price= models.FloatField()
    digital= models.BooleanField(default=False, null=True, blank= True)
    image=models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.name
    
    @property  # Allows me to run even and image is not on Product
    def imageURL(self):
        try:
            url= self.image.url
        except: 
            url = ''
        return url
    
    
class Order(models.Model):
    customer = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.SET_NULL)
    date_ordered = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self): # Get the total $ of an Order
        orderitem = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitem])
        return total
    @property
    def get_cart_items(self): # Get the total items from an Order
        orderitem = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitem])
        return total
    
class OrderItem(models.Model):
    product= models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity= models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    
    @property
    def get_total(self): 
        total= self.product.price * self.quantity
        return total
    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,null=True, blank=True, on_delete=models.SET_NULL)
    order= models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null= False)
    city = models.CharField(max_length=200, null= False)
    state = models.CharField(max_length=200, null= False)
    zipcode = models.CharField(max_length=200, null= False)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
