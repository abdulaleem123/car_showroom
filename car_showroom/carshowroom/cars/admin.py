from django.contrib import admin
from .models import Car, Customer, Salesperson, Sale, Financing, Inventory, Supplier, Order,ContactUs

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('car_id', 'make', 'model', 'year', 'price', 'acceleration', 'top_speed', 'fuel_type')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'email', 'phone_number')

@admin.register(Salesperson)
class SalespersonAdmin(admin.ModelAdmin):
    list_display = ('salesperson_id', 'name', 'contact_information', 'commission_rate')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('sale_id', 'car', 'customer', 'salesperson', 'date_of_sale', 'sale_price')

@admin.register(Financing)
class FinancingAdmin(admin.ModelAdmin):
    list_display = ('financing_id', 'customer', 'terms', 'amount', 'interest_rate')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('inventory_id', 'car', 'quantity', 'location')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('supplier_id', 'name', 'contact_information', 'address')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'supplier', 'car', 'quantity', 'order_date', 'delivery_date')
from .models import ContactUs
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('customer_id', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'message')

    def customer_id(self, obj):
        return obj.customer_id

    customer_id.short_description = 'Customer ID'