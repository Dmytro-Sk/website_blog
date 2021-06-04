from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

from .models import Post


class BlogPageView(ListView):
    model = Post
    template_name = 'blog/main_page.html'
    context_object_name = 'posts_list'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    fields = '__all__'
    success_url = ''

    def get_success_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.object.pk})
