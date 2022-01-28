from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from bank.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bank/', include('bank.urls')),
    path('',HomeView,name="home")
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
