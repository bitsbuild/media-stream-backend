from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
@api_view(['POST'])
def create_user(request):
    pass
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    pass