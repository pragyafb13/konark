from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from soldier.forms import SoldierPersonalDataForm
from django.contrib.auth import authenticate, login , logout
from .models import SoldierPersonalData
from django.http import HttpResponse


@login_required
def edit_soldier(request, soldier_id):
    soldier = get_object_or_404(SoldierPersonalData, id=soldier_id)

    if request.method == 'POST':
        form = SoldierPersonalDataForm(request.POST, instance=soldier)
        if form.is_valid():
            form.save()
            return redirect('soldier_list')
    else:
        form = SoldierPersonalDataForm(instance=soldier)

    return render(request, 'edit_soldier.html', {'form': form, 'soldier': soldier})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def delete_soldier(request, soldier_id):
    soldier = get_object_or_404(SoldierPersonalData, id=soldier_id)

    if request.method == 'POST':
        soldier.delete()
        return redirect('soldier_list')

    return render(request, 'delete_soldier.html', {'soldier': soldier})

@login_required
def add_soldier(request):
    if request.method == 'POST':
        form = SoldierPersonalDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('soldier_list')
    else:
        form = SoldierPersonalDataForm()

    return render(request, 'add_soldier.html', {'form': form})


@login_required
def user_page(request):
    personal_data = SoldierPersonalData.objects.all()
    return render(request, 'user_page.html', {'personal_data': personal_data})


def soldier_list(request):
    personal_data = SoldierPersonalData.objects.all()
    print('pragya', personal_data)
    return render(request, 'soldier_list.html', {'personal_data': personal_data})


@login_required
def soldier_detail(request):
    if request.method == 'POST':
        print('pragya@@', request)
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

def view_list(request):
    print('pragyaraj', request)
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
