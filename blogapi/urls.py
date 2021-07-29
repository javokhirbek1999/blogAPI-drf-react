from rest_framework.routers import DefaultRouter

from .views import PostList

app_name='blog_posts'

router = DefaultRouter()
router.register('',PostList,basename='posts')

urlpatterns = router.urls