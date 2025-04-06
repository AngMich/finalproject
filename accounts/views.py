from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django.contrib.admin.views.decorators import staff_member_required
from catalogue.forms import ComicBookForm
from catalogue.models import ComicBook



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    
    form.helper = FormHelper()
    form.helper.form_method = 'POST'
    form.helper.layout = Layout(
        'username',
        'password1',
        'password2',
        Submit('register', 'Register')
    )

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def logout_user(request):
    return render(request, 'accounts/logout.html')

@staff_member_required
def employee_panel(request):
    return render(request, 'accounts/employee_panel.html')

@staff_member_required
def employee_panel(request, comic_id=None):
    message = ""
    if comic_id:
        comic = get_object_or_404(ComicBook, id=comic_id)
        form = ComicBookForm(request.POST or None, request.FILES or None, instance=comic)
        if request.method == 'POST' and form.is_valid():
            form.save()
            message = "Comic updated successfully!"
    else:
        form = ComicBookForm(request.POST or None, request.FILES or None)
        if request.method == 'POST' and form.is_valid():
            form.save()
            message = "Comic added successfully!"

    comics = ComicBook.objects.all()
    return render(request, 'accounts/employee_panel.html', {
        'form': form,
        'comics': comics,
        'message': message,
        'editing': comic_id is not None
    })