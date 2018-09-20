from django.shortcuts import render_to_response,get_object_or_404
from django.core.paginator import Paginator
from .models import Article,ArticleType
from django.conf import settings
from django.db.models import Count
from read_statist.utils import read_statist_once_read

# Create your views here.

'''
这些函数的功能是输入网址的时返回什么页面
'''
#分页功能的函数
def get_article_list_common_data(articles_all_list,request):
    #article_all_list = Article.objects.all()
    page_num = request.GET.get('page', 1)  # 获取url页面参数  (GET请求)
    paginator = Paginator(articles_all_list, settings.EACH_PAGE_ARTICLE_NUMBER)  # 每10页分一页
    page_of_articles = paginator.get_page(page_num)  # 根据参数在网页显示的某个page,无效则为page1
    current_page = page_of_articles.number  # 获取当前页码
    page_range = list(range(max(current_page - 2, 1), current_page)) + list(
        range(current_page, min(current_page + 2, paginator.num_pages) + 1))
    # 加上省略号标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 加上首页和尾页
    if page_range[0] != 1:
        page_range.insert(0, 1)  # 0是索引值，1是插入对象
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    #单个网页对象
    context['page_of_articles'] = page_of_articles
    # 单页的所有文章
    context['articles'] = page_of_articles.object_list
    context['page_range'] = page_range
    return context


#文章列表
def article_list(request):
    articles_all_list = Article.objects.all()

    context = get_article_list_common_data(articles_all_list,request)
    context['article_types'] = ArticleType.objects.annotate(article_count = Count('article'))#给每个分类写注释(给每个对象添加字段)

    return render_to_response('article/article_list.html', context)


def articles_with_type(request, article_type_pk):
    article_type = get_object_or_404(ArticleType, pk=article_type_pk)  # 例如：pk=1,拿到随笔中的所有文章
    article_all_list = Article.objects.filter(article_type = article_type)  #由类型筛选出来的文章

    context = get_article_list_common_data(article_all_list,request)
    # 拿到文章分类的对象,总共4个
    context['article_types'] = ArticleType.objects.annotate(article_count = Count('article'))
    context['article_type'] = article_type
    return render_to_response('article/articles_with_type.html', context)


#显示文章具体内容
def article_detail(request,article_pk):
    article = get_object_or_404(Article, pk= article_pk)
    read_cookies_key = read_statist_once_read(request,article)

    context = {}
    context['article'] = article
    context['previous_article'] = Article.objects.filter(created_time__gt=article.created_time).last()
    context['next_article'] = Article.objects.filter(created_time__lt=article.created_time).first()
    response = render_to_response('article/article_detail.html',context)

    response.set_cookie('article_%s_read'% article_pk,'true')   #cookies被保存为字典 key,value 有效期/没有就是关闭浏览器
    return response
