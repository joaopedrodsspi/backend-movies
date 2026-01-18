from rest_framework.routers import DefaultRouter
from .views import GenreViewSet, MovieViewSet

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r"genres", GenreViewSet)

urlpatterns = router.urls
