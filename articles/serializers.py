# articles/serializers.py
from rest_framework import serializers
from .models import Article
from .models import Comment

class ArticleListSerializer(serializers.ModelSerializer):
    """게시글 목록 조회 Serializer"""

    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'created_at','image', 'view_count',)  # 조회수 필드 추가
        read_only_fields = ('author', )
        
        
class ArticleDetailSerializer(serializers.ModelSerializer):
    """게시글 상세 조회 및 생성 Serializer"""
    author = serializers.ReadOnlyField(source='author.email') # author 필드에 작성자의 이메일만 출력
    article_is_liked = serializers.SerializerMethodField() #좋아요 여부
    image = serializers.ImageField()
    class Meta:
        model = Article
        fields = ('id', 'author', 'title', 'content', 'image', 'created_at', 'updated_at', 'view_count', 'article_is_liked')  # 조회수 필드 추가

    def get_article_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.article_like_users.filter(pk=request.user.pk).exists()  # 좋아요 여부 확인
        return False
    
    def get_image(self, obj):
        request = self.context.get('request')  # Serializer context에서 request 가져오기
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
        


class CommentSerializer(serializers.ModelSerializer):
    """댓글 조회 및 생성 및 수정 및 삭제 Serializer"""
    author = serializers.ReadOnlyField(source='author.email')
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField() #좋아요 여부
    
    class Meta:
        model = Comment
        fields = ('id', 'article', 'author', 'content', 'created_at', 'updated_at', 'like_users', 'like_count', 'is_liked')
        read_only_fields = ('article','like_users')
        
    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(pk=request.user.pk).exists()
        return False