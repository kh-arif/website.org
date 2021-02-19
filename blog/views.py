from django.views import generic
from .models import Post
from django.shortcuts import render

def home(request):
    return render(request,'index.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'



class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'