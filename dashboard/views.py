from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from item.models import Item


@login_required
# def index(request, user_name):
def index(request):
    item = Item.objects.filter(created_by=request.user)
    # user = get_object_or_404(User, username=user_name)
    template_name = 'dashboard.html'
    context = {
        'items': item,
    }
    return render(request, template_name, context)



