from django.contrib import admin
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
admin.site.register(ContentGenre)
admin.site.register(Artist)
admin.site.register(Content)
admin.site.register(ArtistContentRelation)
admin.site.register(Reviews)
admin.site.register(SubscriptionModels)
admin.site.register(SubscriptionMapping)
admin.site.register(ParentalControlTags)
admin.site.register(ContentMediaFile)
admin.site.register(ContentType)