from rest_framework.routers import DefaultRouter
from .views import *
app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)


urlpatterns = router.urls
