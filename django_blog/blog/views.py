from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse

from django.db.models import Q
from django.shortcuts import render
from .models import Post

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def profile_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            request.user.email = email
            request.user.save()
    return render(request, 'blog/profile.html')

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# List View: Display all posts
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Detail View: Show individual post
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create View: Allow authenticated users to create new posts
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']
    
    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the logged-in user as the author
        return super().form_valid(form)

# Update View: Allow authors to edit their posts
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user  # Ensure the post is updated by the original author
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Check if the logged-in user is the author of the post

# Delete View: Allow authors to delete their posts
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')  # Redirect to the post list after deletion

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author  # Ensure the post can only be deleted by the author
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
        return redirect('post_detail', pk=post.id)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        form = CommentForm(instance=comment)
        return render(request, 'blog/comment_form.html', {'form': form})

    def post(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)

    def test_func(self):
        comment = get_object_or_404(Comment, id=self.kwargs['pk'])
        return self.request.user == comment.author

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, View):
    def post(self, request, pk):
        comment = get_object_or_404(Comment, id=pk)
        post_id = comment.post.id
        comment.delete()
        return redirect('post_detail', pk=post_id)

    def test_func(self):
        comment = get_object_or_404(Comment, id=self.kwargs['pk'])
        return self.request.user == comment.author

def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(tags__name__icontains=query)
    ).distinct()  # Ensure distinct posts if they have multiple tags
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})
def tagged_posts(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/tagged_posts.html', {'posts': posts, 'tag': tag_name})
