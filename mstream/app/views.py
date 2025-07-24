from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from statistics import mean
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
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
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'about', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'about', 'parental_control_tags', 'genre', 'cast', 'type', 'rating', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ArtistContentRelationViewSet(ModelViewSet):
    queryset = ArtistContentRelation.objects.all()
    serializer_class = ArtistContentRelationSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'artist', 'content', 'relation', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user', 'content', 'title', 'review', 'rating', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
    def create(self, request, *args, **kwargs):
        try:
            serialzer = self.get_serializer(data=request.data)
            serialzer.is_valid(raise_exception=True)
            self.perform_create(serialzer)
            reviewed_content = request.data['content']
            revs = list(Reviews.objects.filter(content=reviewed_content).values_list('rating',flat=True))
            rating = mean(revs)
            content_object = Content.objects.get(pk=reviewed_content)
            content_object.rating = rating
            content_object.save()
            return Response({
                "Status":"Review Creation Successfull"
            },status=HTTP_200_OK)
        except Exception as e:
            return Response({
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST)
class SubscriptionModelsViewSet(ModelViewSet):
    queryset = SubscriptionModels.objects.all()
    serializer_class = SubscriptionModelsSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class SubscriptionMappingViewSet(ModelViewSet):
    queryset = SubscriptionMapping.objects.all()
    serializer_class = SubscriptionMappingSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'user', 'plan', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ParentalControlTagsViewSet(ModelViewSet):
    queryset = ParentalControlTags.objects.all()
    serializer_class = ParentalControlTagsSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ContentMediaFileViewSet(ModelViewSet):
    queryset = ContentMediaFile.objects.all()
    serializer_class = ContentMediaFileSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'content', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields
class ContentTypeViewSet(ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'type', 'created', 'updated']
    search_fields = filterset_fields
    ordering_fields = filterset_fields