from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import RegistrationForm, EditPostForm
from .models import MyUser


# Create your viewsi here.


class IndexView(generic.ListView):
    # qlist = Post.objects.all()
    # context = { "postList" : qlist }
    # return render(request, "webportal/index.html", context)
    template_name = 'index.html'
    context_object_name = 'postList'
    paginate_by = 2
    def get_queryset(self):
        return Post.objects.all()

# @login_required(login_url='/accounts/login')
class DetailView(generic.DetailView):
    # qlist = get_object_or_404(Post, id=id)
    # context = { "postList" : qlist }
    # return render(request, "webportal/detail.html", context)
    # if not MyUser.is_authenticated():
    #     raise Http404
    # if not MyUser.is_authenticated():
    #     raise  Http404
    model = Post
    template_name = 'detail.html'

class SignUpView(generic.CreateView):
    form_class = RegistrationForm
    model = MyUser
    template_name = 'register.html'
    success_url = '/'

class EditPostView(generic.UpdateView):
    form_class = EditPostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/'