from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from soldier.forms import SoldierPersonalDataForm
from django.contrib.auth import authenticate, login
from .models import SoldierPersonalData
from django.http import HttpResponse


@login_required
def save_soldier_details(request):
    if request.method == 'POST':
        form = SoldierPersonalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soldier_list')
    else:
        form = SoldierPersonalDataForm()
    return render(request, 'soldier_detail.html', {'form': form})


@login_required
def user_page(request):
    personal_data = SoldierPersonalData.objects.all()
    return render(request, 'user_page.html', {'personal_data': personal_data})


@login_required
def soldier_list(request):
    personal_data = SoldierPersonalData.objects.all()
    return render(request, 'soldier_list.html', {'personal_data': personal_data})


@login_required
def soldier_detail(request):
    if request.method == 'POST':
        form = SoldierPersonalDataForm(request.POST)
        print("Form is valid:", form.is_valid())  # Print form validity
        if form.is_valid():
            form.save()
            return redirect('soldier_detail')  # Replace with your desired redirect URL
        else:
            print("Form errors:", form.errors)  # Print form errors for debugging
    else:
        form = SoldierPersonalDataForm()

    return render(request, 'soldier_detail.html', {'form': form})



@login_required
def view_list(request):
    return render(request, 'soldier_list.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_page')
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def homepage(request):
    return render(request, 'homepage.html')
