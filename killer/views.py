from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Killer, Participant


@login_required
def index(request):
    context = {
        "history": Killer.objects.filter(registration_start_date__lte=timezone.now()).order_by("-game_start_date"),
    }

    return render(request, "killer/index.html", context)

def view(request, pk):
    context = {
        "pk": pk,
    }

    return render(request, "killer/view.html", context)

def admin(request):
    return render(request, "killer/admin/index.html")

def add(request):
    return render(request, "killer/admin/add.html")
