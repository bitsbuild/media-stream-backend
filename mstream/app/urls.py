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
router.register(r'genre',viewset=ContentGenreViewSet,basename='genre')
router.register(r'artists',viewset=ArtistViewSet,basename='artists')
router.register(r'contents',viewset=ContentViewSet,basename='contents')
router.register(r'artconrelation',viewset=ArtistContentRelationViewSet,basename='artconrelation')
router.register(r'reviews',viewset=ReviewsViewSet,basename='reviews')
router.register(r'submodels',viewset=SubscriptionModelsViewSet,basename='submodels')
router.register(r'submap',viewset=SubscriptionMappingViewSet,basename='submap')
router.register(r'parcontag',viewset=ParentalControlTagsViewSet,basename='parcontag')
router.register(r'conmediafile',viewset=ContentMediaFileViewSet,basename='conmediafile')
router.register(r'contype',viewset=ContentTypeViewSet,basename='contype')
urlpatterns = router.urls
