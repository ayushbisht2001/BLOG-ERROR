from django.shortcuts import render

# Create your views here.
from .models import  SearchQuery
from blog.models import BlogPost

def search_view(request):
    # <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" name="q">
    query = request.GET.get('q', None)      # getting query from the search form , where input field  is assigned with a name of 'q'
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query" : query }

    if query is not None:
        SearchQuery.objects.create(user = user , query = query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request,'searches/view.html',context)
