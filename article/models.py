from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericRelation
from read_statist.models import ReadNumExpandMethod,ReadDetail

#Create your models here.
class ArticleType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name



class Article(models.Model,ReadNumExpandMethod):
    title = models.CharField(max_length=30)
    article_type = models.ForeignKey(ArticleType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    created_time = models.DateTimeField(auto_now_add = True)
    last_update_time = models.DateTimeField(auto_now= True)
    #使用用户模型models,使用外键,关联表删除文章作者不删除
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING,default=1)
    #利用反向泛型关系,将模型ReadDetail的属性加持到模型Article上
    read_details = GenericRelation(ReadDetail)
    #显示删除,在数据库不删除
    is_deleted = models.BooleanField(default=False)

    #后台显示文章标题名称
    def __str__(self):
        return "<Article: %s>" %self.title


class Meta:
    ordering =['-created_time']      #排序
