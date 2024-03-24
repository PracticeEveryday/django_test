from django import forms
from app.models import Board


# HTML 폼을 어떻게 보여줄 것인가?
# 저장을 햇을 때 들어온 값의 유효성 검사 실시함.
class PostForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = "__all__"
