from django.shortcuts import render, reverse, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Item,Account
from .forms import ItemForm, AccountForm

# Create your views here.
def main(request):
    return render(request, 'item/layout.html')

def item_delete(request, pk):
    item = Item.objects.get(id=pk)
    item.delete()

    return redirect(reverse('item:item_list'))

def account_delete(request, pk):
    account = Account.objects.get(id=pk)
    account.delete()

    return redirect(reverse('item:account_list'))

item_list = ListView.as_view(model=Item)
item_detail = DetailView.as_view(model=Item)

item_create = CreateView.as_view(model=Item, form_class=ItemForm)
item_edit = UpdateView.as_view(model=Item, form_class=ItemForm)

account_list = ListView.as_view(model=Account)
account_detail = DetailView.as_view(model=Account)

account_create = CreateView.as_view(model=Account, form_class=AccountForm)
account_edit = UpdateView.as_view(model=Account, form_class=AccountForm)