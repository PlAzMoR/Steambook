from rest_framework.routers import DefaultRouter
from .views import UserViewSet, AirticketViewSet
app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'airtickets', AirticketViewSet)


urlpatterns = router.urls
