from django.urls import path
from . import views

app_name = 'articles'

# 비어있는 문자열을 가지고 온다는것은 /articles에 해당되는 경로만 받겠다는 거고
# /articles/뒤에 아무것도 없는 애들은 name 뒤로 보내줄것.
# 그 때 views에 있는 index를 실행 시킨다.
# 앞에 있는 url을 그대로 쓰겠다는 말.
urlpatterns = [
    path('', views.index, name='index'),

    # => articles/5
    path('<int:id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<int:id>/edit', views.edit, name='edit'),
    path('<int:id>/update', views.update, name='update'),
]