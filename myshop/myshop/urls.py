from django.contrib import admin
from django.urls import path, include

# image 파일 엑세스 하기 위한 라이브러리
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('shop.urls')),
    path('users/', include('users.urls')),
    path('product/', include('product.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)