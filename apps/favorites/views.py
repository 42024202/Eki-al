from django.shortcuts import render
from django.views import View
from apps.favorites.models import Favorite
from apps.favorites.serializers import FavoriteSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FavoriteListView(APIView):
    def get(self, request):
        favorites = Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(favorites, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class FavoriteAddView(APIView):
    def post(self, request):
        serializer = FavoriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class FavoriteRemoveView(APIView):  
    def delete(self, request, pk):
        try:
            favorite = Favorite.objects.get(pk=pk, user=request.user)
            favorite.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Favorite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class FavoriteDetailView(APIView):
    def get(self, request, pk):
        try:
            favorite = Favorite.objects.get(pk=pk, user=request.user)
            serializer = FavoriteSerializer(favorite)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Favorite.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
