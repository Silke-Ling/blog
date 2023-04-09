from django.contrib import admin

# Register your models here.

from . import models

# 注册应用到admin中
admin.site.register(models.Article)
