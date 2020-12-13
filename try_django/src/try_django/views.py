from django.http import HttpResponse
from django.shortcuts import  render
from django.template.loader import  get_template
# dont repeat yourself : DRY


def home_page(request):
    my_title = "hello there...."
    context = {"title": my_title,"my_list": ["shabbu","sanu","satvik","satvika"]}
    # doc = "<h1>{title}</h1>".format(title=my_title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title = my_title)
    return render(request,"home.html",context)

def about_page(request):
    return render(request,"about.html" , {"title" : "About US"})

def contact_page(request):
    return render(request,"hello_world.html",{"title" : "Contact US"})

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
    return HttpResponse(template_obj.render(context))

