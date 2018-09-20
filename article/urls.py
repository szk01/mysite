from django.contrib import admin
from django.urls import path
from . import views


#  start with localhost:8000/article/
#name 在HTML中用url关键词可以代表路径
urlpatterns = [
    # 文章列表
    path('',views.article_list, name = 'article_list'),
    # 文章具体内容
    path('<int:article_pk>',views.article_detail, name = 'article_detail'),
    # 博客类别
    path('type/<int:article_type_pk>',views.articles_with_type, name="articles_with_type"),
]