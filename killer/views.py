from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    return render(request, "killer/index.html")

def view(request, pk):
    context = {
        "pk": pk,
    }

    return render(request, "killer/view.html", context)

def admin(request):
    return render(request, "killer/admin/index.html")

def add(request):
    return render(request, "killer/admin/add.html")
