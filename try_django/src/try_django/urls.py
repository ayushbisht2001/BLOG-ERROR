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
urlpatterns = [
    path('home',home_page),
    path('blog-new/', blog_post_create_view),

    path('blog/', include('blog.urls')),

    re_path(r'^about[a-zA-Z0-9]*/$',about_page),        # re_path :  regular expression path
    re_path(r'^contact[a-zA-Z0-9]*/$',contact_page),
    path('admin/', admin.site.urls),

    re_path(r'^example[a-zA-Z0-9]*/$',example_page),
    re_path(r'^text[a-zA-Z0-9]*/$',txtRendering_page),
    # re_path(r'^blog/(?P<slug>\w+)/$', blog_post_detail_page),

]
if settings.DEBUG:
    # test mode
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
