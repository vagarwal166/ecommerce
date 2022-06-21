from django.contrib import admin
from django.urls import path,include
from . import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('',include('buyy.urls')),

]
# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
