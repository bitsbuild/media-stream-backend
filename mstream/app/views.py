from rest_framework.viewsets import ModelViewSet
from app.models import (
    ContentGenre,
    Artist,
    Content,
    ArtistContentRelation,
    Reviews,
    SubscriptionModels,
    SubscriptionMapping,
    ParentalControlTags,
    ContentMediaFile,
    ContentType
)
from app.serializer import (
    ContentGenreSerializer,
    ArtistSerializer,
    ContentSerializer,
    ArtistContentRelationSerializer,
    ReviewsSerializer,
    SubscriptionModelsSerializer,
    SubscriptionMappingSerializer,
    ParentalControlTagsSerializer,
    ContentMediaFileSerializer,
    ContentTypeSerializer
)
class ContentGenreViewSet(ModelViewSet):
    queryset = ContentGenre.objects.all()
    serializer_class = ContentGenreSerializer
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
class ArtistContentRelationViewSet(ModelViewSet):
    queryset = ArtistContentRelation.objects.all()
    serializer_class = ArtistContentRelationSerializer
class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
class SubscriptionModelsViewSet(ModelViewSet):
    queryset = SubscriptionModels.objects.all()
    serializer_class = SubscriptionModelsSerializer
class SubscriptionMappingViewSet(ModelViewSet):
    queryset = SubscriptionMapping.objects.all()
    serializer_class = SubscriptionMappingSerializer
class ParentalControlTagsViewSet(ModelViewSet):
    queryset = ParentalControlTags.objects.all()
    serializer_class = ParentalControlTagsSerializer
class ContentMediaFileViewSet(ModelViewSet):
    queryset = ContentMediaFile.objects.all()
    serializer_class = ContentMediaFileSerializer
class ContentTypeViewSet(ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer