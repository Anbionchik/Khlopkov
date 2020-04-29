from django.shortcuts import render
from main.models import ListModel
from list_item.models import ListItemModel
from django.http import Http404


def list_item_view(request, pk):

    user = request.user

    lists = ListItemModel.objects.filter(
        listmodel_id=pk
    ).order_by(
        'created'
    )

    header = ListModel.objects.filter(
        id=pk,
    ).values_list(
        'name',
        flat=True
    ).first()

    user_verification = lists.values_list('listmodel_id__user_id__username', flat=True).first()

    if user_verification != str(user) and user_verification:
        raise Http404

    context = {
        'lists': lists,
        'header': header,
    }
    return render(request, 'list.html', context)


def edit_view(request, pk):
    pass
