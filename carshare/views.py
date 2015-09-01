from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from . import forms
from . import models
import notifications


@login_required
def index(request):
    context = {}
    context['announcements'] = models.Announcement.objects.all()
    return render(request, 'carshare/index.html', context)


@login_required
def show(request, aid):
    announcement = get_object_or_404(models.Announcement, id=aid)

    context = {
        'announcement': announcement,
        'registrations': models.Registration.objects.filter(announcement=announcement).all(),
        'user_is_author': request.user == announcement.author,
    }


    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            registration = form.save(commit=False)
            registration.announcement = announcement
            registration.user = request.user
            if request.POST['action'] == 'register' and request.user != announcement.author:
                registration.is_simple_comment = False
                notifications.notify(
                    "%s a publier une demande de covoiturage." % str(request.user.profile),
                    "carshare:show", {'aid': aid},
                    [announcement.author],
                )
            else:
                registrations = models.Registration.objects.filter(announcement=announcement).all()
                users = set(reg.user for reg in registrations if reg.user != request.user)
                notifications.notify(
                    "%s a commenté une offre de covoiturage a laquelle vous avez participé" % str(request.user.profile),
                    "carshare:show", {'aid': aid},
                    users,
                )
            registration.save()
            form.save()
            return redirect(reverse('carshare:show', kwargs={'aid': announcement.id}))
        else:
            context['form'] = form
    else:
        context['form'] = forms.RegistrationForm()

    return render(request, 'carshare/show.html', context)


@login_required
def create(request):
    context = {}

    if request.method == "POST":
        form = forms.AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            form.save()
            return redirect(reverse('carshare:index'))
        else:
            context['form'] = form.as_p()
    else:
        context['form'] = forms.AnnouncementForm().as_p()
    return render(request, 'carshare/create.html', context)


@login_required
def action(request, aid, rid, state):
    announcement = get_object_or_404(models.Announcement, id=aid)
    registration = get_object_or_404(models.Registration, id=rid)

    if not request.user == announcement.author or registration.status:
        return redirect(reverse('carshare:show', kwargs={'aid': aid}))

    if state == 'accepted' and announcement.available_places() > 0:
        notifications.notify(
            "Votre demande de covoiturage à été acceptée",
            "carshare:show", {'aid': announcement.id},
            [registration.user],
        )
        registration.status = 'accepted'
    elif state == 'refused':
        notifications.notify(
            "Votre demande de covoiturage à été refusée",
            "carshare:show", {'aid': announcement.id},
            [registration.user],
        )
        registration.status = 'refused'
    else:
        return redirect(reverse('carshare:show', kwargs={'aid': aid}))

    registration.save()
    return redirect(reverse('carshare:show', kwargs={'aid': aid}))

@login_required
def edit(request, aid):
    announcement = get_object_or_404(models.Announcement, id=aid)
    context = {'announcement': announcement}

    if request.method == "POST":
        form = forms.AnnouncementForm(request.POST, instance=announcement)
        if form.is_valid():
            form.save()
            registrations = models.Registration.objects.filter(announcement=announcement).all()
            users = set(reg.user for reg in registrations if reg.user != request.user)
            notifications.notify(
                "L'offre de covoiturage a été éditée",
                "carshare:show", {"aid": announcement.id},
                users
            )
            return redirect(reverse('carshare:show', kwargs={'aid': aid}))
        else:
            context['form'] = form
    else:
        context['form'] = forms.AnnouncementForm(instance=announcement)
    return render(request, 'carshare/edit.html', context)

@login_required
def delete(request, aid):
    announcement = get_object_or_404(models.Announcement, id=aid)
    if request.user == announcement.author:
        registrations = models.Registration.objects.filter(announcement=announcement).all()
        users = set(reg.user for reg in registrations if reg.user != request.user)
        notifications.notify(
            "L'offre de covoiturage a été supprimée",
            "carshare:index", {},
            users
        )
        announcement.delete()
    return redirect(reverse('carshare:index'))
