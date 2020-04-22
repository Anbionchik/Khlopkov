from django.contrib import admin
from main.models import ListModel


class ListAdmin(admin.ModelAdmin):

    list_display = ['id', 'name', 'is_done', 'user', 'created']
    list_filter = ['id', 'created', 'name', 'is_done']
    search_fields = ['name', 'user']


admin.site.register(ListModel, ListAdmin)
