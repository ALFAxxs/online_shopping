from django.shortcuts import render, redirect
from django.contrib.auth import logout

from item.models import Item, Category

from .forms import SignupForm


def index(request):
    items = Item.objects.filter(is_sold=False) #[0:6] boshlang'ich 6 ta element bilan cheklaydi ``SELECT * FROM Item WHERE is_sold = False LIMIT=6;``
    categories = Category.objects.all()

    template_name = 'index.html'
    context = {
        "items": items,
        "categories": categories
    }
    return render(request, template_name, context)


def contact(request):
    template_name = 'contact.html'
    context = None
    return render(request, template_name, context)


def SignupView(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    template_name = 'signup.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the login page
