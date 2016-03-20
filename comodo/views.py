from __future__ import absolute_import
from django.shortcuts import render
from django.views import generic
from .models import Post
from .forms import RegistrationForm, EditPostForm, CreatePostForm
from django.contrib.auth.models import User
from .models import MyUser
from django.http import HttpResponseRedirect,HttpResponse
from  django.template.context_processors import csrf




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

# class SignUpView(generic.CreateView):
#     form_class = RegistrationForm
#     model = MyUser
#     template_name = 'register.html'
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.set_password(MyUser.objects.make_random_password())
#         obj.email = self.request.cleaned_data.get("email")
#         obj.city = self.request.cleaned_data.get("city")
#         obj.save()

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)  # filled form/i'm skipping validation for this example
        if form.is_valid():
            form.save(commit=True)
            print("Form is valid")
        else:
            return HttpResponse(str((form.errors)))
        return HttpResponseRedirect('/comodo/')  # go to some other page if successfully saved

    else:
        form = RegistrationForm  # if the user accessed the register url directly, just display the empty form
    return render(request, 'register.html', {'form': form})
#
#     def form_valid(self, form):
#         obj = form.save(commit=False)
#         obj.set_password(self.POST.get('password'))

# def register(request):
#
#     form = RegistrationForm(request.POST or None)
#
#     if form.is_valid():
#         user = form.save()
#         # email = form.cleaned_data.get("email")
#         user.set_password(user.password)
#         user.save()
#
#     context = {
#         "form" : form,
#     }
#
#     return render(request, "register.html",context)


    # if request.method == 'GET':
    #     form = RegistrationForm
    # else:
    #     form = RegistrationForm(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect('/comodo/')
    # args = {}
    # args.update(csrf(request))
    # args['form'] = RegistrationForm()
    # print args
    # return render(request, 'register.html', args)

class CreatePostView(generic.CreateView):
    form_class = CreatePostForm
    model = Post
    template_name = 'post_create.html'
    success_url = '/comodo'
    # def form_valid(self, form):
    #     resp = super(CreatePostView, self).form_valid(form)
    #     form.instance.user = MyUser.objects.get(self.request.user)
    #     form.instance.save()
    #     # self.object = form.save(commit=False)
    #     # self.object.user = self.request.user
    #     # self.object.save()
    #     return resp

    # def form_valid(self, form):
    #     form.instance.user = MyUser.objects.get(user=self.request.user)
    #     form.instance.save()
    #     return super(CreatePostForm, self).form_valid(form)

class EditPostView(generic.UpdateView):
    form_class = EditPostForm
    model = Post
    template_name = 'post_edit.html'
    success_url = '/comodo'