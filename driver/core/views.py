from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from core.models import Hint
from core.serializers import HintSerializer


class HintList(APIView):
    """
    List all hints or create new hint
    """

    def get(self, request, format=None):
        hints = Hint.objects.all()
        serializer = HintSerializer(hints, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = HintSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HintDetail(APIView):
    """
    Retrive, update or delete a hint instance
    """

    def get_object(self, pk):
        try:
            return Hint.objects.get(pk=pk)
        except Hint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        hint = self.get_object(pk)
        serializer = HintSerializer(hint, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        hint = self.get_object(pk)
        serializer = HintSerializer(hint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        hint = self.get_object(pk)
        hint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
