from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your viewsi here.


class IndexView(generic.ListView):
    # qlist = Post.objects.all()
    # context = { "postList" : qlist }
    # return render(request, "webportal/index.html", context)
    template_name = 'index.html'
    context_object_name = 'postList'
    def get_queryset(self):
        return Post.objects.all()


class DetailView(generic.DetailView):
    # qlist = get_object_or_404(Post, id=id)
    # context = { "postList" : qlist }
    # return render(request, "webportal/detail.html", context)
    model = Post
    template_name = 'detail.html'