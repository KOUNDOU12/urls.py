from django.shortcuts import render, redirect, get_object_or_404

from .forms import RegistrationForm
from .models import Registration


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            inscription = form.save()
            return redirect("inscriptions:confirmation", ticket_id=inscription.ticket_id)
    else:
        form = RegistrationForm()

    return render(request, "inscriptions/register.html", {"form": form})


def confirmation(request, ticket_id):
    inscription = get_object_or_404(Registration, ticket_id=ticket_id)
    return render(request, "inscriptions/confirmation.html", {"inscription": inscription})
