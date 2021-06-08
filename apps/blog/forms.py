from django import forms

from .models import Post, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'New Category*',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'body']
        labels = {
            'title': 'Post Title*',
            'category': 'Choose Category*',
            'body': 'Post Text*',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter text here'})
        }


class EditPostForm(PostForm):
    PostForm.Meta.labels = {
        'title': 'Edit Post Title',
        'category': 'Edit Post Category',
        'body': 'Edit Post Text',
    }
