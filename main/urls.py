from django.urls import path
from main.views import main_view, edit_view
from list_item.views import list_item_view
from new_list.views import new_list_view


app_name = 'main'

urlpatterns = [
    path('', main_view, name='main'),
    path('list/<int:pk>', list_item_view, name='list'),
    path('edit/<int:pk>', edit_view, name='edit'),
    path('create/', new_list_view, name='new_list'),
]