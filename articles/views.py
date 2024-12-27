# articles/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from .models import Article
from .serializers import ArticleListSerializer, ArticleDetailSerializer
from django.core.cache import cache
from .serializers import CommentSerializer
from .models import Comment

class ArticleListCreate(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        """게시글 목록 조회"""
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)  # 목록용 Serializer 사용
        return Response(serializer.data)

    def post(self, request):
        """게시글 생성"""
        serializer = ArticleDetailSerializer(data=request.data)  # 상세 Serializer 사용
        if serializer.is_valid():
            print("FILES:", request.FILES) # 업로드된 파일 정보 확인
            print("DATA:", request.data) # 요청 데이터 확인
            serializer.save(author=request.user)
            print(serializer.errors)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ArticleDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, article_pk):
        return get_object_or_404(Article, pk=article_pk)

    def get(self, request, article_pk):
        """게시글 상세 조회"""
        article = self.get_object(article_pk)
        
        # 로그인한 사용자이고 작성자가 아닌 경우에만 조회수 증가 처리
        # 24시간 동안 같은 IP에서 같은 게시글 조회 시 조회수가 증가하지 않음
        if request.user != article.author:
            # 해당 사용자의 IP와 게시글 ID로 캐시 키를 생성
            cache_key = f"view_count_{request.META.get('REMOTE_ADDR')}_{article_pk}"
            
            # 캐시에 없는 경우에만 조회수 증가
            if not cache.get(cache_key):
                article.view_count += 1
                article.save()
                # 캐시 저장 (24시간 유효)
                cache.set(cache_key, True, 5)

        serializer = ArticleDetailSerializer(article)  # 상세 Serializer 사용
        return Response(serializer.data)
    
    def put(self, request, article_pk):
        
        article = self.get_object(article_pk)
        if request.user != article.author:
            return Response({'detail': '수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = ArticleDetailSerializer(article, data=request.data)  # 상세 Serializer 사용
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, article_pk):
        article = self.get_object(article_pk)
        if request.user != article.author:
            return Response({'detail': '삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)

        article.delete()  # 게시글 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)  # 204 No Content 응답

class ArticleLike(APIView):
    def get_article(self, article_pk):
        return get_object_or_404(Article, pk=article_pk)

    def post(self, request, article_pk):
        """상품 좋아요 토글"""
        article = self.get_article(article_pk)
        user = request.user
        
        # 이미 좋아요를 눌렀는지 확인
        if article.article_like_users.filter(pk=user.pk).exists():
            # 좋아요 취소
            article.article_like_users.remove(user)
            message = "상품을 찜 취소하였습니다."
        else:
            # 좋아요 추가
            article.article_like_users.add(user)
            message = "상품을 찜 했습니다."

        # 상품 정보를 시리얼라이저를 통해 반환
        serializer = ArticleDetailSerializer(article, context={'request': request})
        return Response({
            'message': message,
            'comment': serializer.data
        }, status=status.HTTP_200_OK)
    



class CommentListCreate(APIView):

    def get_article(self, article_pk):
        return get_object_or_404(Article, pk=article_pk)

    def get(self, request, article_pk):
        """댓글 목록 조회"""
        article = self.get_article(article_pk)
        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, article_pk):
        """댓글 생성"""
        article = self.get_article(article_pk)
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user, article=article)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class CommentListDelete(APIView):

    def get_article(self, article_pk):
        return get_object_or_404(Article, pk=article_pk)
    
    def get_comment(self, article, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk, article=article)

    
    def put(self, request, article_pk, comment_pk):
        article = self.get_article(article_pk)
        comment = self.get_comment(article, comment_pk)
        if request.user != article.author:
            return Response({'detail': '수정 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, article_pk, comment_pk):
        article = self.get_article(article_pk)
        comment = self.get_comment(article, comment_pk)
        if request.user != article.author:
            return Response({'detail': '삭제 권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
        comment.delete()  # 댓글 삭제
        return Response(status=status.HTTP_204_NO_CONTENT)





class CommentLike(APIView):

    def get_article(self, article_pk):
        return get_object_or_404(Article, pk=article_pk)

    def get_comment(self, article, comment_pk):
        return get_object_or_404(Comment, pk=comment_pk, article=article)

    def post(self, request, article_pk, comment_pk):
        """댓글 좋아요 토글"""
        article = self.get_article(article_pk)
        comment = self.get_comment(article, comment_pk)
        user = request.user
        
        # 이미 좋아요를 눌렀는지 확인
        if comment.like_users.filter(pk=user.pk).exists():
            # 좋아요 취소
            comment.like_users.remove(user)
            message = "댓글 좋아요가 취소되었습니다."
        else:
            # 좋아요 추가
            comment.like_users.add(user)
            message = "댓글을 좋아요 했습니다."

        # 댓글 정보를 시리얼라이저를 통해 반환
        serializer = CommentSerializer(comment, context={'request': request})
        return Response({
            'message': message,
            'comment': serializer.data
        }, status=status.HTTP_200_OK)
    

