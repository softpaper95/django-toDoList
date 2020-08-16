from django import forms
from .models import Post

class PostForm(forms.ModelForm):#장고에 이폼이 ModelForm이라는걸 알려준다.
     
     class Meta: #어떤 모델이 쓰여야 하는지 장고에 알려준다.
         model = Post
         fields = ('title', 'text',)