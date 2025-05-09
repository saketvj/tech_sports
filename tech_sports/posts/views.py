from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,Tag
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.db.models import Q


# Create your views here.
# getting from the db
# single_post = Post.objects.get(id = 1)
def post_list(request):
    context = {}
    if request.method == "GET":
        category = request.GET.get("tag")
        # q_dict = request.GET #its a dict after querying.
        keyword = request.GET.get("q")
        # print(keyword)
        context = {}
        if keyword :
            # posts = Post.objects.filter(content__icontains  = keyword)
            # context = {"posts": post_object}
            # vector = SearchVector("content", weight="A") + SearchVector("tag__title", weight="C")
            # query = SearchQuery(keyword)
            # posts = Post.objects.annotate(rank=SearchRank(vector, query)).filter(rank__gte=0.3).order_by("rank")
            posts = Post.objects.filter(Q(title__icontains = keyword )|Q(content__icontains =keyword ) | Q(tags__title__icontains = keyword))
        elif category:
            
            q1 = Post.objects.filter(tags__title = category)
            posts = q1
            context['category'] = category


           
        else:
            posts = Post.objects.all()
        
        paginator = Paginator(posts, 6) 
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context['posts'] =page_obj
        return render(request,"posts/list-view.html",context)


def post_detail(request,pk):
    # print("AAAAAAAAAAAA")
    post = Post.objects.get(id =pk )
    # print(id)
    # print(post.created_at.date())
    context = {'posts' :post}

    return render(request,"posts/detail-view.html",context)


# def search_view(request):
#     # print(dir(request))
#     # print(request)
#     q_dict = request.GET #its a dict after querying.
#     keyword = q_dict["q"]
#     print(keyword)
#     context = {}
#     if keyword :
#         post_object = Post.objects.filter(content__search = keyword)
#         context = {"posts": post_object}
#     return render(request, "posts/search.html",context)


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
    form = PostForm() 
    context = {"form":form}
    if request.method == "POST":

        form  = PostForm(request.POST)

        if form.is_valid(): 
            post = form.save(commit=False)      
            post.author = request.user
            tags = form.cleaned_data['tags']
            context['post'] = post
            post.save()  # Save the post with tags
            post.tags.set(tags)  # Set the many-to-many relationship
            context['created'] = True

    return render(request, "posts/create.html",context)





