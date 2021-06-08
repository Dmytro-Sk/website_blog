from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404

from .models import Post, Category
from .forms import CategoryForm, PostForm, EditPostForm


class BlogPageView(ListView):
    model = Post
    template_name = 'blog/main_page.html'
    ordering = ['-id']


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_details.html'


class UpdatePostView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = EditPostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    def get_success_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.object.pk})


class DeletePostView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blog-page')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'blog/add_category.html'


class CategoryListView(ListView):
    model = Post
    template_name = 'blog/category_details.html'

    def get_queryset(self):
        category = get_object_or_404(Category, name=self.kwargs.get('category').capitalize().replace('-', ' '))
        return Post.objects.filter(category=category).order_by('-add_post_date')
