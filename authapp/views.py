from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileImageForm, UpdateForm


def registration(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f"Пользователь {username} был успешно зарегистрирован")
            return redirect('/')
    else:
        form = RegisterForm()

    return render(
        request,
        'authapp/registration.html',
        {'form': form}
    )


@login_required
def profile(request):
    if request.method == 'POST':
        profileImageForm = ProfileImageForm(
            request.POST, request.FILES, instance=request.user.profile
        )
        updateUserForm = UpdateForm(request.POST, instance=request.user)

        if profileImageForm.is_valid() and updateUserForm.is_valid():
            updateUserForm.save()
            profileImageForm.save()
            messages.success(
                request, f"Пользователь {request.user.username} ваш профиль был успешно обновлен"
            )
            return redirect('profile')

    else:
        profileImageForm = ProfileImageForm(instance=request.user.profile)
        updateUserForm = UpdateForm(instance=request.user)

    data = {
        'profileImageForm': profileImageForm,
        'updateUserForm': updateUserForm
    }

    return render(
        request,
        'authapp/profile.html',
        data
    )


# def exit(request):
#     return render(request)
