from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-expense/', views.add_expense, name='add_expense'),
     path('expenses/', views.expense_list, name='expense_list'),
     path('expense/edit/<int:id>/', views.edit_expense, name='edit_expense'),
    path('expense/delete/<int:id>/', views.delete_expense, name='delete_expense'),
    path('add-salary/', views.add_salary, name='add_salary'),

    
]