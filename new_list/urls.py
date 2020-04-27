from django.urls import path
from new_list.views import new_list_view


app_name = 'new_list'

urlpatterns = [
    path('', new_list_view, name='new_list'),
]