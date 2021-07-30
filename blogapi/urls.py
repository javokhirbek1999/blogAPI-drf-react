from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PostList, PostDetailFilter

app_name='blog_posts'

router = DefaultRouter()
router.register('',PostList,basename='posts')

urlpatterns = [
    path('', include(router.urls)),
    path('search/', PostDetailFilter.as_view(),name='detailfilter')
]