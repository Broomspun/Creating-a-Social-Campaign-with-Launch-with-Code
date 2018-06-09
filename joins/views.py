from django.shortcuts import render
from .forms import JoinForm
from .models import Join

# Create your views here.


def home(request):

    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email=email)
    #

    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        # we might do something here
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        new_join.save()

    template = "home.html"
    context = {
        "title": 'Welcome',
        "form": form
    }

    return render(request, template, context)
