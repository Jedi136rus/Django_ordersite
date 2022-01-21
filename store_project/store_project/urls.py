from django.contrib import admin
from django.urls import path
from lending import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page),
    path('thanks', views.thanks_page, name='thanks'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)