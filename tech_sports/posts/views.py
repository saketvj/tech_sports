from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
# getting from the db
# single_post = Post.objects.get(id = 1)
def post_list(request):
    if request.method == "GET":
        q_dict = request.GET
        posts = Post.objects.all()
        context = {'posts' :posts}
        return render(request,"posts/list-view.html",context)

def post_detail(request,pk):
    # print("AAAAAAAAAAAA")
    post = Post.objects.get(id =pk )
    # print(id)
    # print(post.created_at.date())
    context = {'posts' :post}

    return render(request,"posts/detail-view.html",context)


def search_view(request):
    # print(dir(request))
    # print(request)
    q_dict = request.GET #its a dict after querying.
    pk = q_dict["q"]
    context = {}
    if pk :
        post_object = Post.objects.get(id = pk)
        context = {"posts": post_object}
    return render(request, "posts/search.html",context)


# @login_required
# def create_view(request):
#     # print(dir(request))
#     context = {}
#     if request.method == "POST":
#         # print(request)
#         # print(request.user)
#         title = request.POST.get("title")
#         author = request.user
#         content = request.POST.get("title")
#         post_object = Post.objects.create(title = title,content = content,author = author)
#         context['created'] = True
#         context['post'] = post_object

#     return render(request, "posts/create.html",context)

@login_required
def create_view(request):
    # print(dir(request))
    form = PostForm()
    context = {"form":form}
    if request.method == "POST":
        form  = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            author = request.user
            content = form.cleaned_data.get("content")
            post_object = Post.objects.create(title = title,content = content,author = author)
            print(post_object.id)
            context['post'] = {'title':title,'author':author,'content':content,'id':post_object.id}
            context['created'] = True
    
    return render(request, "posts/create.html",context)


# tags






