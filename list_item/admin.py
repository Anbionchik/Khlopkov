from django.contrib import admin
from list_item.models import ListItemModel


class ListItemAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'is_done', 'listmodel_id', 'created', 'expiration_date']
    list_filter = ['id', 'created', 'name', 'is_done', 'expiration_date']
    search_fields = ['name', 'user']


admin.site.register(ListItemModel, ListItemAdmin)
