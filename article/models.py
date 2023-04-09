from django.db import models

# Create your models here.

from django.contrib.auth.models import User
# timezone 用于处理时间相关事务。
from django.utils import timezone
from mdeditor.fields import MDTextField

#文章数据模型
class Article(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='作者',default=User)
    title=models.CharField('标题',max_length=60)
    summary=models.TextField('摘要',max_length=200,blank=True)
    body=MDTextField(verbose_name='正文')
    #background=models.ImageField(upload_to='article_img/%Y/%m/%d/', verbose_name='文章图片', blank=True, null=True)
    views=models.PositiveIntegerField('阅读量', default=0)
    created=models.DateTimeField('创建时间', default=timezone.now)
    updated=models.DateTimeField('更新时间', auto_now=True)
    #元数据定义
    class Meta:
        ordering=['-created']   #数据返回顺序：依照created倒序排列
    #模型类调用定义
    def __str__(self):
        return self.title       #返回对象属性title
