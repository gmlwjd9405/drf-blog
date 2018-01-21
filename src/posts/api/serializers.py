from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
)

from comments.api.serializers import CommentSerializer
from comments.models import Comment
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

post_detail_url = HyperlinkedIdentityField(
    view_name='posts-api:detail',
    lookup_field='slug'
)


class PostListSerializer(ModelSerializer):
    url = post_detail_url
    delete_url = HyperlinkedIdentityField(
        view_name='posts-api:delete',
        lookup_field='slug'
    )
    user = SerializerMethodField()

    class Meta:
        model = Post
        field = [
            'url',
            'user',
            'title',
            'content',
            'publish',
            'delete_url'

        ]

    def get_user(self, obj):
        return str(obj.user.username)


class PostDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = SerializerMethodField()
    image = SerializerMethodField()
    markdown = SerializerMethodField()
    comments = SerializerMethodField()

    class Meta:
        model = Post
        field = [
            'url',
            'user',
            'id',
            'title',
            'slug',
            'content',
            'publish',
            'image',
            'markdown',
            'comments'

        ]

    def get_markdown(self, obj):
        return obj.get_markdown()

    def get_user(self, obj):
        return str(obj.user.username)

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            return None
        return image

    def get_comments(self, obj):
        c_qs = Comment.objects.filter_by_instance(obj)
        comments = CommentSerializer(c_qs, many=True).data
        return comments

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