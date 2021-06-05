from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse

from .models import Post
from .forms import PostForm


class BlogPageView(ListView):
    model = Post
    template_name = 'blog/main_page.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def get_success_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.object.pk})
