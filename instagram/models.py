from django.db import models

# User Model이 변경 될 수도 있으므로 해당 방법은 사용하지 않는다. --> settings에 설정해서 사용.
# from django.contrib.auth.models import User # 기본적이 유저 모델 사용할 때 사용.
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to='instagram/post/%Y/%m/%d')
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java toString
    def __str__(self):
        # return f"Custome Post Object({self.id})"
        return f'{self.message}'

    class Meta:
        ordering = ['-id']  # id 필드에 대해 역순

    # model에 메세지 관련 특성 구현 하는 방법(admin 에서도 구현 가능)
    # def message_length(self):
    #     return len(self.message)
    #
    # message_length.short_description = '메세지 글자수'


class Comment(models.Model):
    # 이런식으로도 작성 가능
    # post = models.ForeignKey('instagram.Post', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public' : True}) # post_id 필드가 생성이됨 (id)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
