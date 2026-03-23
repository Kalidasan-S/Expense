from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from .models import Expense, Category,Salary
from django.db.models.functions import TruncMonth


from datetime import date




# Create your views here.

def dashboard(request):
    return render(request,'tracker/dashboard.html')


@login_required
def add_expense(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        amount = request.POST.get('amount')
        category_id = request.POST.get('category')
        note = request.POST.get('note')

        Expense.objects.create(
            user=request.user,
            category_id=category_id,
            amount=amount,
            date=date.today(),
            note=note
        )

        return redirect('dashboard')

    return render(request, 'tracker/add_expense.html', {
        'categories': categories
    })

    
@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user).order_by('-date')
    return render(request, 'tracker/expense_list.html', {
        'expenses': expenses
    })

@login_required
def dashboard(request):
    data = (
        Expense.objects
        .filter(user=request.user)
        .values('category__name')
        .annotate(total=Sum('amount'))
    )

    labels = [d['category__name'] for d in data]
    values = [float(d['total']) for d in data]

    return render(request, 'tracker/dashboard.html', {
        'labels': labels,
        'values': values
    })

@login_required
def add_expense(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        amount = request.POST.get('amount')
        category_id = request.POST.get('category')
        note = request.POST.get('note')

        Expense.objects.create(
            user=request.user,
            category_id=category_id,   # 🔥 IMPORTANT
            amount=amount,
            date=date.today(),
            note=note
        )
        return redirect('dashboard')

    return render(request, 'tracker/add_expense.html', {
        'categories': categories
    })

@login_required
def edit_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    categories = Category.objects.all()

    if request.method == 'POST':
        expense.amount = request.POST.get('amount')
        expense.category_id = request.POST.get('category')
        expense.note = request.POST.get('note')
        expense.date = date.today()
        expense.save()

        return redirect('expense_list')

    return render(request, 'tracker/edit_expense.html', {
        'expense': expense,
        'categories': categories
    })
@login_required
def delete_expense(request, id):
    expense = get_object_or_404(Expense, id=id, user=request.user)
    expense.delete()
    return redirect('expense_list')


@login_required
def add_salary(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        amount = request.POST.get('amount')

        # one salary per user (latest overwrite)
        Salary.objects.update_or_create(
            user=request.user,
            defaults={
                'month': month,
                'amount': amount
            }
        )
        return redirect('dashboard')

    return render(request, 'tracker/add_salary.html')


@login_required
def dashboard(request):
    # SALARY
    salary_obj = Salary.objects.filter(user=request.user).first()
    salary = salary_obj.amount if salary_obj else 0

    # TOTAL EXPENSE
    total_expense = (
        Expense.objects
        .filter(user=request.user)
        .aggregate(total=Sum('amount'))['total'] or 0
    )

    balance = salary - total_expense

    # -------- PIE CHART (CATEGORY) --------
    category_data = (
        Expense.objects
        .filter(user=request.user)
        .values('category')
        .annotate(total=Sum('amount'))
    )

    labels = [Category.objects.get(id=c['category']).name for c in category_data]
    
    values = [float(c['total']) for c in category_data]
    return render(request,"tracker/dashboard.html", {
        'salary': salary,  
        'total_expense': total_expense,
        'balance': balance,
        'labels': labels,
        'values': values,
    })

   