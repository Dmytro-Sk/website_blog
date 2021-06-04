from django.shortcuts import render


def blog_page(request):
    return render(request, 'blog/main_page.html', {'content': 'Blog Page'})
