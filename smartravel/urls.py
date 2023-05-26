from xml.dom.minidom import Document
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travelapp.urls')),
    path('auth/', include('authentication.urls')),
]

urlpatterns = urlpatterns + \
    static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "helpers.views.handle_not_found"
handler500 = "helpers.views.handle_server_error"
