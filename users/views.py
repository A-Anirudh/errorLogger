from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from log.models import Log
from django.contrib.auth.models import User
from allauth.account.decorators import verified_email_required

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserRegisterForm (request.POST)
        if form.is_valid():
            human=True
            form.save()
            username = form.cleaned_data.get('username')
            message = messages.success(request, f'Account created for {username}. You are now able to Login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@verified_email_required
@login_required
def profile(request, username):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid and p_form.is_valid():
            u_form.save()
            p_form.save()
            message = messages.success(request, f'Your profile has been updated')
            return redirect('profile', username=username)

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    try:
        profile = User.objects.get(username=username)
    except User.DoesNotExist:
        message = messages.warning(request,f'Profile not found for {username}')

        return redirect('home')
        profile = ''

    print('profile name: ',profile.username)

    all_post_by_user = Log.objects.filter(author__username=username)
    print(all_post_by_user)
    context = {
        'u_form' : u_form,
        'p_form' : p_form,
        'profile' : profile, 
        'all_post_by_user' : all_post_by_user
    }

    return render(request, 'users/profile.html', context)
