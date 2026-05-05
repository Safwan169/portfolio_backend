from rest_framework.routers import DefaultRouter
from .views import ProjectListViewSet

router=DefaultRouter()
router.register('projects',ProjectListViewSet,basename='projects')
urlpatterns=router.urls