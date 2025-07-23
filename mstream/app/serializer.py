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
from rest_framework import serializers
class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = '__all__'
class ContentGenreSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = ContentGenre
        fields = '__all__'
class ArtistSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
class ArtistContentRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArtistContentRelation
        fields = '__all__'
class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
class SubscriptionModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionModels
        fields = '__all__'
class SubscriptionMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionMapping
        fields = '__all__'
class ParentalControlTagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParentalControlTags
        fields = '__all__'
class ContentMediaFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentMediaFile
        fields = '__all__'
class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = '__all__'