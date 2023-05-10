from django.db import models

# Create your models here.
class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True)
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Java toString
    def __str__(self):
        #return f"Custome Post Object({self.id})"
        return f'{self.message}'

    # model에 메세지 관련 특성 구현 하는 방법(admin 에서도 구현 가능)
    # def message_length(self):
    #     return len(self.message)
    #
    # message_length.short_description = '메세지 글자수'
    #
    #