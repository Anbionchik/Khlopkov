from main.models import ListModel
from django.shortcuts import render, reverse, redirect
from main.forms import ListForm
from django.contrib.auth import logout


def main_view(request):
    """ Главная View """
    user = request.user

    try:
        lists = ListModel.objects.filter(
            user=user,
        ).order_by(
            'created'
        )
    except TypeError:
        lists = []

    context = {
        'lists': lists,
        'user': request.user.username
    }
    return render(request, 'index.html', context)


def edit_view(request, pk):
    pass


def new_list_view(request):

    form = ListForm()

    if request.method == "POST":
        name = request.POST.get('name')
        form = ListForm({
            'name': name,
            'user': request.user
        })
        success_url = reverse('main:main')
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, "new_list.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect('main:main')
