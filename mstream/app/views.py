from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAdminUser,IsAuthenticated
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
class ArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ContentViewSet(ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ArtistContentRelationViewSet(ModelViewSet):
    queryset = ArtistContentRelation.objects.all()
    serializer_class = ArtistContentRelationSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ReviewsViewSet(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewsSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAuthenticated]
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
class SubscriptionMappingViewSet(ModelViewSet):
    queryset = SubscriptionMapping.objects.all()
    serializer_class = SubscriptionMappingSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ParentalControlTagsViewSet(ModelViewSet):
    queryset = ParentalControlTags.objects.all()
    serializer_class = ParentalControlTagsSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ContentMediaFileViewSet(ModelViewSet):
    queryset = ContentMediaFile.objects.all()
    serializer_class = ContentMediaFileSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]
class ContentTypeViewSet(ModelViewSet):
    queryset = ContentType.objects.all()
    serializer_class = ContentTypeSerializer
    throttle_classes = [UserRateThrottle]
    permission_classes = [IsAdminUser]