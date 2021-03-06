from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializer import PostSerializer
# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
