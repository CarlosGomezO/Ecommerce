from django.contrib import admin
from api.models import *

# Register your models here.

admin.site.register(Data)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

