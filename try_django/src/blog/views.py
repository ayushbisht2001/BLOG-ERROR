from django.shortcuts import render , get_object_or_404
from django.http import Http404
# Create your views here.

from .models import BlogPost

# get  ---> 1 object
# filter ----> list of objects


# /..........................................................................



# def blog_post_detail_page(request,slug):
#     # try:
#     #     obj = BlogPost.objects.get(id=post_id)
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise  Http404
#
#     # queryset = BlogPost.objects.filter(slug=slug)
#     # if queryset.count() == 0:
#     #     raise  Http404
#     #
#     # obj = queryset.first()
#     obj = get_object_or_404(BlogPost,slug=slug)    # id  :  should be an integer value
#
#     template_name = "blog_post_detail.html"
#     context = {"object" : obj}
#     return render(request,template_name,context)

# CRUD : create , retrieve , update, delete
# ..... GET --> Retrieve / List
#.......POST --> Create / update / Delete



# ..................................................................................................................






def blog_post_list_view(request):
    # list out objects
    #  also search
    qs = BlogPost.objects.all() # list of python objects

    # qs = BlogPost.objects.filter(title__icontains = 'hello')        # Searching .... .. . On the basis of title
    template_name = 'blog_post_list.html'
    context = {'object_list': qs}
    return render(request,template_name,context)


def blog_post_create_view(request):
    # create objects / create blogs
    # use of form

    template_name = 'blog_post_create.html'
    context = {'form':None}
    return render(request,template_name,context)


def blog_post_detail_view(request,slug):
    # 1 object --> detail view
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    template_name = "blog_post_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    template_name = "blog_post_update.html"
    context = {"object": obj , 'form' : None}
    return render(request, template_name, context)

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    template_name = "blog_post_delete.html"
    context = {"object": obj}
    return render(request, template_name, context)






