from rest_framework.serializers import (
    ModelSerializer, HyperlinkedIdentityField, SerializerMethodField
)

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        field = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content'

        ]