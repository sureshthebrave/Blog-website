from django.urls import path
from blogapp.views import blog,post,search_view,get_category

urlpatterns = [
    path('blog/',blog,name="blog"),
    path('post/<str:title>/',post,name="post"),
    path('search/',search_view,name="search"),
    path('category/<str:cat>/',get_category,name="category"),

]