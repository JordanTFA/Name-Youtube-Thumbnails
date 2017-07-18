from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
	url(r'', include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^edit/', include('edit.urls')),
    #url(r'^about/', include('home.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)