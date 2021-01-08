from django.http import HttpResponse
from django.shortcuts import  render
from django.template.loader import  get_template

# dont repeat yourself : DRY
# from blog.models import BlogPost

from .forms import *
from blog.models import *


def home_page(request):
    my_title = "HOME"
    qs= BlogPost.objects.all()[:5]
    context = {"title": my_title,"blog_list": qs }
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title = my_title)

    # if request.user.is_authenticated :
    #     context = {"title" : my_title , "my_list": [1,2,3,4,5]}

    return render(request,"home.html",context)

def about_page(request):
    return render(request,"about.html" , {"title" : "About US"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {"title" : "Contact US" , "form" : form}
    return render(request,"form.html",context)

# This is something like writing html on notepad and then render it out to get the final result
def txtRendering_page(request):
    context = {"title":"Notepad"}
    template_name = "title.txt"                     # rendering a string
    template_obj = get_template(template_name)
    rendered_string = template_obj.render(context)
    return render(request,"hello_world.html",{"title" : rendered_string})

# this whole thing do the same as above one did , but using httpresponse
def example_page(request):
    context = {"title" : "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    print(template_obj , "hello world 123456")
    return HttpResponse(template_obj.render(context))
