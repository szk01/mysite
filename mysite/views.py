import datetime
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render_to_response
from django.utils import timezone
from django.db.models import Sum
from django.core.cache import cache
from article.models import Article
from read_statist.utils import get_seven_day_hot_data,get_today_hot_data

def get_7_days_hot_articles():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    #通过时间筛选
    articles = Article.objects.filter(read_details__date__lt=today, read_details__date__gte=date)
    #通过id,title分组
    article_group = articles.values('id','title').annotate(read_num_sum=Sum('read_details__read_num'))
    return article_group.order_by('-read_num_sum')[:7]

#这个参数是固定的
def index(request):
    article_content_type = ContentType.objects.get_for_model(Article)
    dates,read_num = get_seven_day_hot_data(article_content_type)
    today_hot_data = get_today_hot_data(article_content_type)

    #获取7天热门博客的缓存数据
    hot_articles_for_7_days=cache.get('hot_articles_for_7_days')
    if hot_articles_for_7_days is None:
        hot_articles_for_7_days = get_7_days_hot_articles()
        cache.set('hot_articles_for_7_days',hot_articles_for_7_days,60*60)#一小时缓存一次
        print('cache')
    else:
        print('have used cache!')

    context = {}
    context['dates'] = dates
    context['read_num'] = read_num
    context['today_hot_data'] = today_hot_data

    context['hot_articles_for_7_days'] = get_7_days_hot_articles()

    return render_to_response('index.html',context)