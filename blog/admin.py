from django.contrib import admin

# Register your models here.
from .models import Post

admin.site.register(Post)
#admin 사이트에 Post를 등록해준것
