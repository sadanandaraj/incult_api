from rest_framework.routers import DefaultRouter
from . import views

app_name = "stores"

router = DefaultRouter()
router.register("", views.StoreViewSet)

urlpatterns = router.urls
