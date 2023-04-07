import calendar
import json
import random
from pprint import pprint

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.db.models import Count, Func, Sum
from django.shortcuts import render, redirect
# Create your views here.
from django.template.loader import render_to_string
from django.utils.crypto import get_random_string

from roberms_admin.models import Appointment, Company
from salesperson.forms import CompanyForm
from sms.models import *
from sms.utils import SDP, subtract_months


class Month(Func):
    function = 'EXTRACT'
    template = '%(function)s(MONTH from %(expressions)s)'
    output_field = models.IntegerField()


def get_last_n_months(n):
    months = []
    i = 0
    # today = datetime.datetime.today()
    # months.append(today)
    while i < n + 1:
        date = subtract_months(datetime.datetime.today(), i)
        months.append(date)
        i += 1
    return months


def dashboard(request):
    sales_person = SalesPerson.objects.get(user_ptr_id=request.user.id)
    customer_ids = []
    months = get_last_n_months(6)
    data = {}

    manager_top_ups = ManagerTopUp.objects.filter(
        user_id__in=Sale.objects.filter(
            sales_person_id=sales_person.id).only('customer_id').values('customer_id').distinct(),
        commission_paid=False
    )
    print(manager_top_ups)
    for month in months:
        # monthly_top_up = 0
        s = manager_top_ups.filter(
            created_at__month=month.month, created_at__year=month.year
        ).aggregate(monthly_total=Sum('amount'))
        # for t in manager_top_ups:
        #     actual_date = datetime.datetime.strptime(t.timestamp, '%Y-%m-%d %H:%M:%S.%f')
        #     if actual_date.month == month.month:
        #         monthly_top_up += float(t.amount)
        if s['monthly_total'] is not None:
            data[calendar.month_name[month.month]] = s['monthly_total']
        else:
            data[calendar.month_name[month.month]] = 0


    context = {
        'data': data
    }
    print( data)
    return render(request, 'salesperson/dashboard.html', context)


def clients(request):
    sales_person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
    sales = Sale.objects.filter(sales_person=sales_person)

    customer_ids = []
    for sale in sales:
        customer_ids.append(sale.customer.id)
    clients = Customer.objects.filter(id__in=customer_ids)
    context = {
        'sales': sales,
        'clients': clients
    }
    return render(request, 'salesperson/my_clients.html', context)


def client_top_ups(request, client_id):
    top_ups = ManagerTopUp.objects.filter(user_id=client_id)
    context = {
        'top_ups': top_ups
    }
    return render(request, 'salesperson/client_top_ups.html', context)


def all_top_ups(request):
    sales_person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
    client_ids = []
    sales = Sale.objects.filter(sales_person_id=sales_person.id)
    for sale in sales:
        client_ids.append(sale.customer_id)
    top_ups = ManagerTopUp.objects.filter(user_id__in=list(set(client_ids))).order_by('-created_at')
    context = {
        'top_ups': top_ups
    }
    return render(request, 'salesperson/all_top_ups.html', context)


@login_required
def account_usage(request):
    sales_person = SalesPerson.objects.get(user_ptr_id=request.user.id)
    context = {
        'customers': sales_person.customers()
    }
    return render(request, 'salesperson/credit_usage.html', context)


@login_required()
def my_companies(request):
    sales_person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
    companies = Company.objects.filter(sales_person_id=sales_person.id)
    context = {
        'sales_person': sales_person,
        'companies': companies
    }
    return render(request, 'company/my_companies.html', context)


@login_required()
def company_appointments(request, company_id):
    appointments = Appointment.objects.filter(company_id=company_id)

    context = {
        'appointments': appointments
    }
    return render(request, 'company/company_appointments.html', context)


@login_required()
def add_company(request):
    person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
    r = request.POST.copy()
    r['sales_person'] = person.id
    if request.method == 'POST':
        form = CompanyForm(r)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company added successfully')
            return redirect('salesperson:my_companies')
        else:
            context = {
                'form': form
            }
            print(form)
            messages.success(request, 'Error adding company')
            return render(request, 'company/add_company.html', context)
    return render(request, 'company/add_company.html')


@login_required()
def edit_company(request, company_id):
    company = Company.objects.get(id=company_id)
    person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
    r = request.POST.copy()
    r['sales_person'] = person.id
    if request.method == 'POST':
        form = CompanyForm(r, instance=company)
        if form.is_valid():
            form.save()
            messages.success(request, 'Company information updated successfully')
            return redirect('')
        else:
            context = {
                'form': form
            }
            messages.success(request, 'Error updating company information')
            return render(request, '', context)
    context = {
        'company': company
    }
    return render(request, 'company/edit_company.html', context)


@login_required()
def appointment_list(request, company_id):
    appointments = Appointment.objects.filter(company_id=company_id)
    context = {
        'appointments': appointments,
        'company': Company.objects.get(id=company_id)
    }
    return render(request, 'company/company_appointments.html', context)


@login_required()
def add_appointment(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        new_date = f'{request.POST["appointment_date"]} {datetime.datetime.time(timezone.now())}'
        new_date = datetime.datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S.%f')
        print(new_date)
        Appointment.objects.create(
            description=request.POST['description'],
            date_visited=new_date,
            company_id=company.id
        )
        messages.success(request, 'Appointment added successfully')
        return redirect('salesperson:company_appointments', company_id)

    context = {
        'company': company
    }
    return render(request, 'company/add_appointment.html', context)


@login_required()
def edit_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    if request.method == 'POST':
        new_date = f'{request.POST["appointment_date"]} {datetime.datetime.time(timezone.now())}'
        new_date = datetime.datetime.strptime(new_date, '%Y-%m-%d %H:%M:%S.%f')
        appointment.description = request.POST['description']
        appointment.date_visited = new_date
        # appointment.date_visited = timezone.now()
        appointment.save()
        messages.success(request, 'Appointment updated successfully')
        return redirect('salesperson:company_appointments', appointment.company_id)

    context = {
        'appointment': appointment
    }
    return render(request, 'company/edit_appointment.html', context)


@login_required()
def mark_visited_not_visited(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    company = appointment.company
    if appointment.status_visited == True:
        appointment.status_visited = False
        appointment.save()
        messages.success(request, 'Marked as not visited')
        return redirect('salesperson:company_appointments', company.id)
    else:
        appointment.status_visited = True
        appointment.save()
        messages.success(request, 'Marked as visited')
        return redirect('salesperson:company_appointments', company.id)


@login_required()
def sales_logout(request):
    logout(request)
    messages.success(request, 'You have logged out successfully')
    return redirect('sms:sms-home')

#
# def add_client(request):
#     if request.method == 'POST':
#         sales_person = SalesPerson.objects.filter(user_ptr_id=request.user.id).first()
#         customer_code = random.randint(10000, 99999)
#         while Customer.objects.filter(customer_code=customer_code).count() > 0:
#             customer_code = random.randint(10000, 99999)
#
#         email = request.POST['email']
#         password = get_random_string(length=8)
#         phone_number = request.POST['phone_number']
#         if User.objects.filter(username=email).count() < 1:
#             p = f"{254}{phone_number.replace(' ', '')[-9:]}"
#             customer, created = Customer.objects.update_or_create(
#                 username=email,
#                 email=email,
#                 password=password,
#                 phone_number=p,
#                 customer_code=customer_code,
#                 is_active=False
#             )
#             Sale.objects.create(
#                 sales_person=sales_person,
#                 customer=customer
#             )
#             messages.success(request, 'Client Added Successfully')
#             return redirect("salesperson:clients")
#         else:
#             messages.error(request, 'User exists')
#             return render(request, 'salesperson/add_client.html')
#
#     return render(request, 'salesperson/add_client.html')