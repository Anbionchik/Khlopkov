from django.shortcuts import render, reverse, redirect
from new_list.forms import ListForm


def new_list_view(request):

    form = ListForm()

    if request.method == "POST":
        form = ListForm(data=request.POST)
        success_url = reverse('main:main')
        if form.is_valid():
            form.save()
            return redirect(success_url)

    return render(request, "new_list.html", {'form': form})
