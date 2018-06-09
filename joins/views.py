from django.shortcuts import render
from .forms import JoinForm
from .models import Join

# Create your views here.


def get_ip(request):
    try:
        x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forward:
            ip = x_forward.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
    except:
        ip = ''

    return ip


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
        if created:
            new_join_old.ip_address = get_ip(request)
            new_join_old.save()

    template = "home.html"
    context = {
        "title": 'Welcome',
        "form": form
    }

    return render(request, template, context)
