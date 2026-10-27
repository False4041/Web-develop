from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'in_stock', 'created_at')
    list_display_links = ('id', 'name')
    list_editable = ('price', 'quantity', 'in_stock')
    search_fields = ('name', 'description')
    list_filter = ('in_stock', 'created_at')
    readonly_fields = ('created_at',)
    date_hierarchy = 'created_at'
    save_on_top = True


admin.site.site_header = 'Управление каталогом'
admin.site.site_title = 'Каталог товаров'
admin.site.index_title = 'Администрирование'
