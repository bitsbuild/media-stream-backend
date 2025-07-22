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
from rest_framework.serializers import ModelSerializer
class ContentGenreSerializer(ModelSerializer):
    class Meta:
        model = ContentGenre
        fields = '__all__'
class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = '__all__'
class ContentSerializer(ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
class ArtistContentRelationSerializer(ModelSerializer):
    class Meta:
        model = ArtistContentRelation
        fields = '__all__'
class ReviewsSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
class SubscriptionModelsSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionModels
        fields = '__all__'
class SubscriptionMappingSerializer(ModelSerializer):
    class Meta:
        model = SubscriptionMapping
        fields = '__all__'
class ParentalControlTagsSerializer(ModelSerializer):
    class Meta:
        model = ParentalControlTags
        fields = '__all__'
class ContentMediaFileSerializer(ModelSerializer):
    class Meta:
        model = ContentMediaFile
        fields = '__all__'
class ContentTypeSerializer(ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'