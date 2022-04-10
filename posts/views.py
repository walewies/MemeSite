from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .models import Post, Comment
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
class CreatePost(CreateView):
    model = Post
    fields = ('meme_file', 'description')
    template_name = "CreatePost.html"

    def get_success_url(self):
        return reverse_lazy("accounts:profile", kwargs={"slug": self.request.user.slug})

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.memer = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())

class PostAndCommentsView(CreateView):
    template_name = "PostView.html"
    model = Comment
    context_object_name = "comment"
    fields = ('body',)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.memer = self.request.user
        obj.post = Post.objects.get(id=self.kwargs['pk'])
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = Post.objects.get(id=self.kwargs['pk']).memer
        context["post"] = Post.objects.get(id=self.kwargs['pk'])
        context["comments"] = Comment.objects.filter(post=self.kwargs['pk'])
        return context
        
    def get_success_url(self, **kwargs):
        return reverse_lazy("posts:view_post", kwargs={"pk": self.kwargs['pk']})