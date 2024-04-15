from django.shortcuts import render

# Create your views here.
posts = [
    {'author' : 'Corey',
    'title' : 'Post 1',
    'date_posted': '03/10/2023',
    'content': 'This is the first post'
     },

    {'author' : 'Schafer',
    'title' : 'Post 2',
    'date_posted': '03/11/2023',
    'content': 'This is the Second post'
     }
]


def home(request):
    context = {'post': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About' })