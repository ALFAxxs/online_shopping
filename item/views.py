from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import NewItemForm, EditItemForm
from .models import Item, Category


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    categories = Category.objects.all()
    items = Item.objects.filter(is_sold=False)

    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    template_name = 'items.html'
    context = {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': category_id
    }
    return render(request, template_name, context)

def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)

    template_name = 'detail.html'
    context = {
        'item': item,
        'related_items': related_items
    }
    return render(request, template_name, context)

@login_required
def NewItemView(request):
    if request.method == 'POST':                        #so'rov turi tekshirladi
        form = NewItemForm(request.POST, request.FILES) #so'rov turi to'g'ri kelgandan keyin , Formaga so'rov keladi
        if form.is_valid():                             #agar malumot bo'lsa
            item = form.save(commit=False)              #commit = False bu yerda jo'natilgan malumotlarni darhol malumotlar bazasiga saqlmasligni oldini oladi
            item.created_by = request.user              #malumotni kim jo'natilgan malumot egasi aniqlanib uni malumotga qoshib qoyiladi
            item.save()                                 #malumot saqlanadi
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()

    template_name = 'form.html'
    context = {
        'form': form,
        'title': 'New Item',
    }
    return render(request, template_name, context)


@login_required
def DeletItemsView(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    return redirect('dashboard:dashboard')


@login_required
def EditItemView(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)

    template_name = 'form.html'
    context = {
        'form': form,
        'title': 'Edit Item',
    }
    return render(request, template_name, context)
