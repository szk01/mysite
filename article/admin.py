from django.contrib import admin
from .models import Article,ArticleType

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #将文章对象的几个属性用列表形式表现出来
    list_display = ('id','title','article_type','content','author','get_read_num','is_deleted','created_time','last_update_time')
    #正序 ordering = ('id',) 反序就是-id

#admin.site.register(Article, ArticleAdmin)

@admin.register(ArticleType)
class ArticleTypeAdmin(admin.ModelAdmin):
    list_display = ('id','type_name')

