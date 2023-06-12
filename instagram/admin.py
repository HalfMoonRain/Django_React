from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Post, Comment, Tag


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
@admin.register(Post)  # Wrapping
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo_tag', 'message', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}" style = "width:72px"/>')
        return None

    def message_length(self, post):
        return f'{len(post.message)} 글자'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
