from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Salary, Expense

admin.site.register(Category)
admin.site.register(Salary)
admin.site.register(Expense)