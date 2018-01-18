from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        field = [
            'title',
            'slug',
            'content',
            'publish'

        ]


class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        field = [
            'id',
            'title',
            'slug',
            'content',
            'publish'

        ]


"""
data = {
    "title": "Yeahhh buddy",
    "content": "Noew content",
    "slug": "yeah-buddy",
    "publish": "2016-2-12",
    }
    
new_item = PostSerializer(data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""