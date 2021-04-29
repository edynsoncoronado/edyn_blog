from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from blogs.models import Category, Blog
from blogs.serializers import CategorySerializer, BlogSerializer

@api_view(['GET', 'POST'])
def category_list(request, format=None):
    if request.method == 'GET':
        category = Category.objects.all()
        serializers = CategorySerializer(category, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = CategorySerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializers = BlogSerializer(blogs, many=True)
        return Response(serializers.data)
    
    elif request.method == 'POST':
        serializers = BlogSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
@api_view(['GET'])
def blog_detail(request, pk):
    try:
        blog = Blog.objects.get(pk=pk)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

    """
    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    """