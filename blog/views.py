from django.shortcuts import render
from .models import Post


posts = [
    {
        'author': 'Blake John',
        'title': 'Blog Post Test 1',
        'content': 'This is a test post.',
        'date_posted': 'October 11, 2020'
    },
    {
        'author': 'Sarah Williams',
        'title': 'Blog Post Test 2',
        'content': 'This is test post 2.',
        'date_posted': 'October 9, 2020'
    }
]


# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
