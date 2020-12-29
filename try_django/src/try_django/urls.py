"""try_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , re_path , include
from .views import *
from blog.views import *
from django.conf import  settings
from searches.views import *
from register.views import *
from django.views.generic import TemplateView
urlpatterns = [
    path('home',home_page),
    path('blog-new/', blog_post_create_view),
    path('search/' , search_view),
    path('blog/', include('blog.urls')),

    re_path(r'^about[a-zA-Z0-9]*/$',about_page),        # re_path :  regular expression path
    re_path(r'^contact[a-zA-Z0-9]*/$',contact_page),
    path('admin/', admin.site.urls),
    path('register/',register),
    # path("",include("user")),
    re_path(r'^example[a-zA-Z0-9]*/$',example_page),
    re_path(r'^text[a-zA-Z0-9]*/$',txtRendering_page),
    # re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_page),
    path('',include("django.contrib.auth.urls")),  # for login and logout and redirect to the html file of registration folder
    path('accounts/', include('allauth.urls')),
    # path('',TemplateView.as_view(template_name='login.html')),

            ]

if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
