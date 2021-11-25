from django import forms
from .models import Post, Category

# choices = [('codding', 'codding'), ('sports', 'sports'), ('enternainment', 'enternainment')]
choices = Category.objects.all().values_list('name', 'name')
choice_list = [item for item in choices]

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'author', 'category', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': choice_list
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'category': forms.Select(choices=choice_list, attrs={
                'class': 'form-control',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'title_tag', 'body']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'title_tag': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'author': forms.Select(attrs={
                'class': 'form-control',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
            }),
        }