
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('user_auth.urls')),
    path('home/', include('base.urls')),
    path('payment/', include('payment.urls')),
    path('reviews-and-blog/', include('review_blog.urls')),
    path('products/', include('product.urls')),
    # path('chatbot/', include('chatbot.urls')),
    path('adminside/configuration/', include('adminside.urls')),
    
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)