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
from django.contrib.auth.models import User
class ContentSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(many=True, queryset=ContentGenre.objects.all(), write_only=True)
    cast = serializers.PrimaryKeyRelatedField(many=True, queryset=Artist.objects.all(), write_only=True)
    parental_control_tags = serializers.PrimaryKeyRelatedField(many=True, queryset=ParentalControlTags.objects.all(), write_only=True)
    type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all(), write_only=True)
    genre_name = serializers.StringRelatedField(source='genre',many=True,read_only=True)
    cast_name = serializers.StringRelatedField(source='cast',many=True,read_only=True)
    parental_control_tags_name = serializers.StringRelatedField(source='parental_control_tags',many=True,read_only=True)
    type_name = serializers.StringRelatedField(source='type',read_only=True)
    class Meta:
        model = Content
        fields = '__all__'
class ContentGenreSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ContentGenre
        fields = '__all__'
class ArtistContentRelationSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all(),write_only=True)
    artist = serializers.PrimaryKeyRelatedField(queryset=Artist.objects.all(),write_only=True)
    content_name = serializers.StringRelatedField(source='content',read_only=True)
    artist_name = serializers.StringRelatedField(source='artist',read_only=True)
    class Meta:
        model = ArtistContentRelation
        fields = '__all__'
class ArtistSerializer(serializers.ModelSerializer):
    credits = ArtistContentRelationSerializer(many=True,read_only=True)
    class Meta:
        model = Artist
        fields = '__all__'
class ReviewsSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all(),write_only=True)
    content_name = serializers.StringRelatedField(source='content',read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Reviews
        fields = '__all__'
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
class SubscriptionModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionModels
        fields = '__all__'
class SubscriptionMappingSerializer(serializers.ModelSerializer):
    plan = serializers.PrimaryKeyRelatedField(queryset=SubscriptionModels.objects.all(),write_only=True)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(),write_only=True)
    plan_name = serializers.StringRelatedField(source='plan',read_only=True)
    user_user = serializers.StringRelatedField(source='user',read_only=True)
    class Meta:
        model = SubscriptionMapping
        fields = '__all__'
class ParentalControlTagsSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ParentalControlTags
        fields = '__all__'
class ContentMediaFileSerializer(serializers.ModelSerializer):
    content = serializers.PrimaryKeyRelatedField(queryset=Content.objects.all(),write_only=True)
    content_name = serializers.StringRelatedField(source='content',read_only=True)
    class Meta:
        model = ContentMediaFile
        fields = '__all__'
class ContentTypeSerializer(serializers.ModelSerializer):
    content = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = ContentType
        fields = '__all__'