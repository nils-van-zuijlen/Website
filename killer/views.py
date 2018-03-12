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
    game = Killer.objects.filter(registration_start_date__lte=timezone.now()).get(id=pk)
    players = Participant.objects.filter(game__id=pk).select_related("user__profile")

    context = {
        "game": game,
        "players": players,
        "alive": players.filter(dead=False),
        "dead": players.filter(dead=True),
    }

    return render(request, "killer/view.html", context)

def admin(request):
    return render(request, "killer/admin/index.html")

def add(request):
    return render(request, "killer/admin/add.html")
