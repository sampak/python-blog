from rest_framework.views import APIView
from rest_framework import generics
from blogs.models import Post
from blogs.serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response


class PostView(APIView):
    def get(self, request, *args, **kwargs):
        if 'pk' in kwargs:
            try:
                post = Post.objects.get(pk=kwargs['pk'])
                serializer = PostSerializer(post)
                return Response(serializer.data)
            except Post.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            posts = Post.objects.all()
            serializer = PostSerializer(posts, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        else:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
