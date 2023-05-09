from django.contrib import admin
from .models import Post
# Register your models here.

# 첫번째 방법
# 바로 사용
# admin.site.register(Post)

# 두번 째 방법
# 클래스에 담아서 사용
# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)

# 세번 째 방법
# 데코레이터 이용
@admin.register(Post) # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'message', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']
    def message_length(self, post):
        return f'{len(post.message)} 글자'