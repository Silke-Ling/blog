# 引入path
from django.urls import path

# 正在部署的应用名称
app_name = 'article'

from . import views

urlpatterns = [
    #将url映射到view
    path('detail_<int:id>/',views.article,name='article_detail'),
    path('',views.index,name='article'),
]