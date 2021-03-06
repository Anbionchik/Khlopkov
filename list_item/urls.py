from django.urls import path
from list_item.views import list_item_view, edit_view, new_list_item_view


app_name = 'list_item'

urlpatterns = [
    path('', list_item_view, name='list_item'),
    path('create_list/<int:pk>', new_list_item_view, name='new_list_item'),
    path('edit/<int:pk>', edit_view, name='edit'),
]