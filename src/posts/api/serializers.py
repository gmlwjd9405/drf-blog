from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        field = [
            'title',
            # 'slug',
            'content',
            'publish'

        ]


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
            'user',
            'id',
            'title',
            'slug',
            'content',
            'publish'

        ]


"""
from posts.models import Post
from posts.api.serializers import PostDetailSerializer

data = {
    "title": "Yeahhh buddy",
    "content": "Noew content",
    "slug": "yeah-buddy",
    "publish": "2016-2-12",
    }

obj = Post.objects.get(id=2)

new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)
"""