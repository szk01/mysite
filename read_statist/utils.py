import datetime                   #顺序：先引进python自带的，然后引进框架的，最后是自己写的
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum,ReadDetail

#阅读次数加1,并且返回相应的cookies信息
def read_statist_once_read(request,obj):
    ct = ContentType.objects.get_for_model(obj)
    key = "%s_%s_read " % (ct.model, obj.pk)

    if not request.COOKIES.get(key):  # 如果cookies不存在，则加1
        # 总的阅读量计数加1
        readnum, create=ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)#如果不存在就创建一个
        readnum.read_num += 1
        readnum.save()

        #当天阅读量
        date = timezone.now().date()
        read_num_day,create = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk,date=date)
        read_num_day.read_num +=1
        read_num_day.save()

    return key
#拿到相应日期的总阅读数量
def get_seven_day_hot_data(content_type):#参数是不同的类型模型 此时是ReadDetail
    today = timezone.now().date()
    dates = []
    read_nums =[]
    for i in range(7,0,-1):
        date =  today - datetime.timedelta(days=i) #datetime.timedelta(days=1)是一天的日期差
        dates.append(date.strftime('%m/%d'))
        read_details=ReadDetail.objects.filter(content_type=content_type,date=date) #filter是筛选出相应属性的具体数据
        result=  read_details.aggregate(read_num_sum=Sum('read_num')) #aggregrate()是聚合函数,返回的是字典
        read_nums.append(result['read_num_sum'] or 0)
    return dates,read_nums

#从read_details模型拿到今天的数据
def get_today_hot_data(content_type):
    today = timezone.now().date()
    read_details = ReadDetail.objects.filter(content_type=content_type,date=today)
    return read_details.order_by('-read_num')[:7]

#从read_details模型中拿到一周的数据
def get_7_days_hot_data(content_type):
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    #筛选出一周内所有的数据
    read_details = ReadDetail.objects.filter(content_type=content_type, date__lt=today, date__gte=date)
    #合并相同的文章阅读数,即是按照文章进行分组values()
    same_article_num = read_details.values('content_type','object_id').annotate(read_num_sum=Sum('read_num'))
    return same_article_num.order_by('-read_num')[:7]
