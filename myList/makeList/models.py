from django.conf import settings
from django.db import models
from django.utils import timezone
# Create your models here.
# Post(게시글)
# text내용 
# created_date(작성일)
class Post(models.Model):
#class 객체를 정의/ modles.Mode: 이 객체가 장고 모델임을 의미함, 이 코드 때문에 장고는 Post가 데이터베이스에 저장되어야 한다고 알게 된다.
    title = models.CharField(max_length=30)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)#default는 기본값을 의미한다.

    def __str__(self):
        return self.title