from .views import ProjectListViewSet
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('tecnologies',ProjectListViewSet,basename='tecnologies')
urlpatterns=router.urls