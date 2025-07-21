from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from user.serializers import UserSerializer
@api_view(['POST'])
def create_user(request):
    try:
        srlzr =  UserSerializer(data=request.data)
        srlzr.is_valid(raise_exception=True)
        srlzr.save()
        return Response(
            {
                "Status":"Account Creation Successful"
            },status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST
        )
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_user(request):
    try:
        request.user.delete()
        return Response(
            {
                "Status":"Account Deleted Successfully"
            },status=HTTP_200_OK
        )
    except Exception as e:
        return Response(
            {
                "Status":"Error",
                "Error":str(e)
            },status=HTTP_400_BAD_REQUEST
        )