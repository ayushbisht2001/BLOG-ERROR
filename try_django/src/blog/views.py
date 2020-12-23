from django.shortcuts import render , get_object_or_404 , redirect
from django.contrib.auth.decorators import   login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
# Create your views here.

from .models import BlogPost
from .forms import *
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
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request,template_name,context)

# @ login_required()
@ staff_member_required
def blog_post_create_view(request):
    # create objects / create blogs
    # use of form
    # request.user will return something if "   @ staff_member_required or above one is present "
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        obj = form.save(commit = False)
        obj.user = request.user
        obj.title = form.cleaned_data.get("title")
        obj.save()
        # title = form.cleaned_data['title']
        # slug = form.cleaned_data["slug"]
        # content = form.cleaned_data["content"]

        """
         cd = {"x" : 3, "y": 6}
         
         then  **cd gives (x=3,y = 6) arguments 
         => create(**form.cleaned_data) === create(title=title, slug = slug,content = content)
        
        """
        # obj = BlogPost.objects.create(**form.cleaned_data)   : this is undertaken by BlogPostModelForm
        form = BlogPostModelForm()       # To reinitialise the form





        """
        obj = BlogPost.objects.create(title = title,slug=slug,content =content)
             # or  ................
        obj = BlogPost()
        obj.title = title
        obj.save()
            """


    template_name = 'blog/form.html'
    context = {'form': form}
    return render(request,template_name,context)


def blog_post_detail_view(request,slug):
    # 1 object --> detail view
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    template_name = "blog/detail.html"
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request,slug):
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    form = BlogPostModelForm(request.POST or None ,instance=obj)
    if form.is_valid():
        form.save()
    template_name = "form.html"
    context = {  'form' : form , "title" : f"Update {obj.title} "}
    return render(request, template_name, context)

def blog_post_delete_view(request , slug):
    obj = get_object_or_404(BlogPost, slug=slug)  # id  :  should be an integer value
    template_name = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object": obj}
    return render(request, template_name, context)






