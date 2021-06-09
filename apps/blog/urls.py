from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.BlogPageView.as_view(), name='blog-page'),

    path('post/add/', views.AddPostView.as_view(), name='add-post'),
    path('post/<int:pk>/details/', views.PostDetailView.as_view(), name='post-details'),
    path('post/<int:pk>/update/', views.UpdatePostView.as_view(), name='update-post'),
    path('post/<int:pk>/delete/', views.DeletePostView.as_view(), name='delete-post'),
    path('post/<int:pk>/like/', views.PostLikeToggleView.as_view(), name='post-like'),

    path('category/add/', views.AddCategoryView.as_view(), name='add-category'),
    path('category/<str:category>/details/', views.CategoryListView.as_view(), name='category-details'),
]
