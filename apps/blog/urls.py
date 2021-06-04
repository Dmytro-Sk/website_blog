from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog-page'),
    path('add_post', views.AddPostView.as_view(), name='add-post'),
    path('post_details/<int:pk>', views.PostDetailView.as_view(), name='post-details'),
]
