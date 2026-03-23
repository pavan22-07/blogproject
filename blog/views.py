from django.shortcuts import render,redirect
from . models import Post, Comment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    posts=Post.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        text = request.POST.get('text')
        Comment.objects.create(post=post, text=text)
    comments = post.comment_set.all()

    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments': comments
    })
def log_out_view(request):
    return render(request, 'log_out.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})