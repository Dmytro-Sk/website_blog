from django import forms

from .models import Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'New Category',
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body', 'post_image']
        labels = {
            'title': 'Post Title',
            'category': 'Choose Category',
            'body': 'Post Text',
        }


class EditPostForm(PostForm):
    PostForm.Meta.labels = {
        'title': 'Edit Post Title',
        'category': 'Edit Post Category',
        'body': 'Edit Post Text',
        'post_image': 'Change Post Image',
    }
