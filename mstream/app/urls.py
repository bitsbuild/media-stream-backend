from rest_framework.routers import DefaultRouter
from app.views import (
    ContentGenreViewSet,
    ArtistViewSet,
    ContentViewSet,
    ArtistContentRelationViewSet,
    ReviewsViewSet,
    SubscriptionModelsViewSet,
    SubscriptionMappingViewSet,
    ParentalControlTagsViewSet,
    ContentMediaFileViewSet,
    ContentTypeViewSet
)
router = DefaultRouter()
router.register(ContentGenreViewSet)
router.register(ArtistViewSet)
router.register(ContentViewSet)
router.register(ArtistContentRelationViewSet)
router.register(ReviewsViewSet)
router.register(SubscriptionModelsViewSet)
router.register(SubscriptionMappingViewSet)
router.register(ParentalControlTagsViewSet)
router.register(ContentMediaFileViewSet)
router.register(ContentTypeViewSet)
urlpatterns = router.urls
