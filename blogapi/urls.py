from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostList, PostDetailFilter, AdminPostDetail, CreatePost, EditPost, DeletePost

app_name='blog_posts'

router = DefaultRouter()
router.register('',PostList,basename='posts')

urlpatterns = [
    path('search/', PostDetailFilter.as_view(),name='postsearch'),
    path('', include(router.urls)),
    path('admin/create/', CreatePost.as_view(), name='createpost'),
    path('admin/edit/postdetail/<int:pk>/', AdminPostDetail.as_view(), name='adminpostdetail'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='editpost'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='deletepost'),
]