from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.AutoField(primary_key=True)
    make = models.CharField(max_length=255, default="")
    model = models.CharField(max_length=255, default="")
    year = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    acceleration = models.CharField(max_length=255, default="")  # Add acceleration field
    top_speed = models.CharField(max_length=255, default="")     # Add top_speed field
    fuel_type = models.CharField(max_length=255, default="")     # Add fuel_type field
    image = models.ImageField(upload_to="cars/images", default="")

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255, default="")
    last_name = models.CharField(max_length=255, default="")
    email = models.EmailField(default="")
    phone_number = models.CharField(max_length=20, default="")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    contact_information = models.TextField(default="")
    commission_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return self.name

class Sale(models.Model):
    sale_id = models.AutoField(primary_key=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    salesperson = models.ForeignKey('Salesperson', on_delete=models.SET_NULL, null=True, default=None)
    date_of_sale = models.DateField(default=None)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"Sale of {self.car} to {self.customer} on {self.date_of_sale}"

class Financing(models.Model):
    financing_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    terms = models.CharField(max_length=255, default="")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    def __str__(self):
        return f"Financing for {self.customer}"

class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    car = models.OneToOneField('Car', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    location = models.CharField(max_length=255, default="")

    def __str__(self):
        return f"Inventory item: {self.car}"

class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, default="")
    contact_information = models.TextField(default="")
    address = models.TextField(default="")

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order_date = models.DateField(default=None)
    delivery_date = models.DateField(default=None)

    def __str__(self):
        return f"Order for {self.quantity} {self.car} from {self.supplier} on {self.order_date}"
    



class ContactUs(models.Model):
    customer_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    message = models.TextField()

    def __str__(self):
        return f"Contact request from {self.first_name} {self.last_name} ({self.email})"
