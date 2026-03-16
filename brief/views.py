from django.shortcuts import render, redirect
from .forms import BriefResponseForm


def brief_form_view(request):
    if request.method == "POST":
        form = BriefResponseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("brief_success")
    else:
        form = BriefResponseForm()

    return render(request, "brief/brief_form.html", {"form": form})


def success_view(request):
    return render(request, "brief/success.html")