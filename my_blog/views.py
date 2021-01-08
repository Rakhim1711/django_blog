from django.shortcuts import render, get_object_or_404
from .models import Blogs

def all_blogs(request):
    blog = Blogs.objects.all()
    return render(request, 'my_blog/all_blogs.html', {'blogs':blog})

def detail(request, blog_id):
    blog = get_object_or_404(Blogs, pk=blog_id)

    return render(request, 'my_blog/detail.html', {'blog':blog})
