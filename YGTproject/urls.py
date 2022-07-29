from django.contrib import admin
from django.urls import path, include
from postapp import views

# drf-yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'post',views.PostViewSet)
router.register(r'profile',views.ProfileViewSet)
router.register(r'comment',views.CommentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    #게시글 목록 
    path('', views.home, name='home'),

    #게시글 작성
    path('postcreate', views.postcreate, name='postcreate'),

    #세부 페이지
    path('detail/<int:post_id>', views.detail, name='detail'),

    #댓글 작성
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

    #좋아요
    path('post_like/<int:post_id>', views.post_like, name='post_like'),
    path('comment_like/<int:post_id>', views.comment_like, name='comment_like'),
]

## api 자동 문서화 ##
schema_view = get_schema_view(
    openapi.Info(
        title='게시글 작성 및 댓글 작성 API',
        default_version='API 버전',
        description=
        '''
        게시글 작성 및 댓글 작성 / 
        게시글 목록 / 
        게시글, 댓글 좋아요 기능

        작성자 : 공서은
        ''',
        terms_of_service='',
        contact=openapi.Contact(name='공서은', email='seoeun7872@gmail.com'),
        license=openapi.License(name='게시글 작성 및 댓글 작성 API')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    patterns=urlpatterns,
)

# drf_yasg url 
urlpatterns += [
    path('',include(router.urls)),
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]