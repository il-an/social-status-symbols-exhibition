# Register your models here.
from django.contrib import admin
from main.models import Category, Item
from sorl.thumbnail.admin import AdminImageMixin


class ItemInline(AdminImageMixin, admin.TabularInline):
    model = Item
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "picture")
