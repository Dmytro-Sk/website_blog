from django.shortcuts import render


def home_page(request):
    return render(request, 'home_page/home_page.html', {'content': 'Home page'})
