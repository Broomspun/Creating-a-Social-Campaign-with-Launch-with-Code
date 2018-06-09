from django.shortcuts import render


def home(request):
    context = {
        "title": 'Welcome'
    }

    return render(request, 'home.html', context)
