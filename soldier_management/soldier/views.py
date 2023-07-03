from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from soldier.forms import SoldierPersonalDataForm
from django.contrib.auth import authenticate, login , logout
from .models import SoldierPersonalData, BtyChamp
from django.http import HttpResponse
from .forms import BtyChampForm
from .models import SoldierBtyChamp
from django.contrib.auth.decorators import user_passes_test

def update_scores(request):
    if not request.user.is_authenticated:
        return redirect('login')  # Redirect to login page if user is not authenticated

    if request.method == 'POST':
        event = request.POST.get('event')
        p_bty = request.POST.get('p_bty')
        q_bty = request.POST.get('q_bty')
        r_bty = request.POST.get('r_bty')
        s_bty = request.POST.get('s_bty')

        # Update the scores in the database only if the fields are not empty
        if p_bty:
            SoldierBtyChamp.objects.filter(events=event).update(P_bty=p_bty)
        if q_bty:
            SoldierBtyChamp.objects.filter(events=event).update(Q_bty=q_bty)
        if r_bty:
            SoldierBtyChamp.objects.filter(events=event).update(R_bty=r_bty)
        if s_bty:
            SoldierBtyChamp.objects.filter(events=event).update(S_bty=s_bty)

        return redirect('soldier_btychamp')  # Redirect to a success page or scores listing

    # Get the list of events from the database
    events = SoldierBtyChamp.objects.values_list('events', flat=True)
    return render(request, 'update_scores.html', {'events': events})



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
def edit_soldier(request, soldier_id):
    soldier = get_object_or_404(SoldierPersonalData, id=soldier_id)

    if request.method == 'POST':
        form = SoldierPersonalDataForm(request.POST, instance=soldier)
        if form.is_valid():
            form.save()
            return redirect('soldier_list')
    else:
        form = SoldierPersonalDataForm(instance=soldier)

    return render(request, 'edit_soldier.html', {'form': form, 'soldier_id': soldier_id})



@login_required
@user_passes_test(lambda u: u.is_superuser and u.username == 'p_bty_user')
def p_bty_view(request):
    # Implement the logic for the P bty page
    return render(request, 'p_bty.html')


@login_required
@user_passes_test(lambda u: u.is_superuser and u.username == 'q_bty_user')
def p_bty_view(request):
    # Implement the logic for the Q bty page
    return render(request, 'q_bty.html')


@login_required
@user_passes_test(lambda u: u.is_superuser and u.username == 'r_bty_user')
def r_bty_view(request):
    # Implement the logic for the R bty page
    return render(request, 'r_bty.html')

@login_required
@user_passes_test(lambda u: u.is_superuser and u.username == 's_bty_user')
def s_bty_view(request):
    # Implement the logic for the S bty page
    return render(request, 's_bty.html')



from django.db.models import Sum

@login_required
def soldier_btychamp_view(request):
    if request.user.is_superuser and request.user.username == 'pragya':
        soldier_btychamp = SoldierBtyChamp.objects.all()
        total_scores = soldier_btychamp.aggregate(
            total_P_bty=Sum('P_bty'),
            total_Q_bty=Sum('Q_bty'),
            total_R_bty=Sum('R_bty'),
            total_S_bty=Sum('S_bty')
        )
        data = zip(soldier_btychamp, [row.P_bty + row.Q_bty + row.R_bty + row.S_bty for row in soldier_btychamp])
        return render(request, 'soldier_btychamp.html', {'data': data, 'total_scores': total_scores})
    elif request.user.username == 'p_bty_user':
        return redirect('p_bty_view')  # Redirect to the 'p_bty_view' if the user is 'p_bty_user'
    elif request.user.username == 'q_bty_user':
        return redirect('q_bty_view')  # Redirect to the 'q_bty_view' if the user is 'q_bty_user'
    elif request.user.username == 'r_bty_user':
        return redirect('r_bty_view')  # Redirect to the 'r_bty_view' if the user is 'r_bty_user'
    elif request.user.username == 's_bty_user':
        return redirect('s_bty_view')  # Redirect to the 's_bty_view' if the user is 's_bty_user'
    else:
        return redirect('user_page')  # Redirect to the user page for any other user

@login_required
@user_passes_test(lambda u: u.username == 'p_bty_user')
def p_bty_view(request):
    events = SoldierBtyChamp.objects.values_list('events', flat=True).distinct()
    soldier_btychamp = SoldierBtyChamp.objects.filter(events__in=events)
    total_scores = soldier_btychamp.aggregate(total_P_bty=Sum('P_bty'))

    return render(request, 'p_bty.html', {'soldier_btychamp': soldier_btychamp, 'total_scores': total_scores, 'events': events})


@login_required
@user_passes_test(lambda u: u.username == 'q_bty_user')
def q_bty_view(request):
    return render(request, 'q_bty.html')

@login_required
@user_passes_test(lambda u: u.username == 'r_bty_user')
def r_bty_view(request):
    return render(request, 'r_bty.html')
@login_required
@user_passes_test(lambda u: u.username == 's_bty_user')
def s_bty_view(request):
    return render(request, 's_bty.html')


@login_required
def bty_champ_view(request):
    bty_champ = BtyChamp.objects.all()
    form = BtyChampForm()
    context = {
        'bty_champ': bty_champ,
        'form': form
    }
    return render(request, 'bty_champ.html', context)


@login_required
def save_bty_champ_view(request):
    if request.method == 'POST':
        form = BtyChampForm(request.POST)
        if form.is_valid():
            bty_champ_id = form.cleaned_data['id']
            bty_champ = get_object_or_404(BtyChamp, id=bty_champ_id)
            if request.user.is_authenticated:
                bty_champ.P_bty = form.cleaned_data['P_bty']
                bty_champ.Q_bty = form.cleaned_data['Q_bty']
                bty_champ.R_bty = form.cleaned_data['R_bty']
                bty_champ.S_bty = form.cleaned_data['S_bty']
                bty_champ.save()
                return redirect('bty_champ')

    return redirect('bty_champ')



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
def user_page(request):
    personal_data = SoldierPersonalData.objects.all()
    return render(request, 'user_page.html', {'personal_data': personal_data})


def soldier_list(request):
    personal_data = SoldierPersonalData.objects.all()
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
