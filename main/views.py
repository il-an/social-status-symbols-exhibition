from django.shortcuts import render, get_object_or_404
from .models import Item


def index(request):
    return render(request, "main/index.html")


def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'exhibition/item_detail.html', {'item': item})

def home_view(request):
    items = Item.objects.all()  # Получаем все предметы из базы данных
    return render(request, 'main/home.html', {'items': items})