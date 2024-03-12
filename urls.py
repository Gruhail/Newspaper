from django.urls import path
from .views import Posts, PostDetail, PostCreate, PostEdit, PostDelete


urlpatterns = [
    path('news', Posts.as_view(), name='home'),
    path('news/<int:pk>', PostDetail.as_view(), name='post'),
    path('news/create', PostCreate.as_view(), name='newpost'),
    path('news/<int:pk>/edit', PostEdit.as_view(), name='edit'),
    path('news/<int:pk>/delete', PostDelete.as_view(), name='deletenews')
    ]
