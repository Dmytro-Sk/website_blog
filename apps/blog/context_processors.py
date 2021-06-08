from .models import Category


def get_context_data(request):
    context = {'category_data': Category.objects.all()}
    return context
