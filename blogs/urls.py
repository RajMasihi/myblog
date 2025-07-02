#from myblogs.blogs.models import Post
from .views import home, post, category
from django.contrib import admin
admin.site.site_header = 'Blogs by Raj Masihi'
admin.site.site_title='blog'
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
    path('blogs/<slug:url>', post),
    path('category_post/<slug:url>', category)
] 