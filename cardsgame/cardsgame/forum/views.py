from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from .models import Forum_post, Comment_post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import PostModelForm, CommentModelForm


class CommentListView(ListView):
    model = Comment_post
    context_object_name = 'comments'
    template_name = 'forum_page1.html'


class PostListView(ListView):
    model = Forum_post
    context_object_name = 'posts'
    template_name = 'forum_page1.html'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Forum_post
    form_class = PostModelForm
    success_url = reverse_lazy('forum_page')
    template_name = 'new_post.html'


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.forum_post_author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get(self,  request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)

class CommentsCreateView(LoginRequiredMixin, CreateView):
    model = Comment_post
    form_class = CommentModelForm
    success_url = reverse_lazy('forum_page')
    template_name = 'add_comment.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.comment_author = self.request.user
        post_id = self.kwargs['post_id']
        forum = Forum_post.objects.get(id=post_id)
        self.object.forum = forum
        self.object.save()
        return super().form_valid(form)

    def get(self,  request, *args, **kwargs):
        print(request.user)
        return super().get(request, *args, **kwargs)


