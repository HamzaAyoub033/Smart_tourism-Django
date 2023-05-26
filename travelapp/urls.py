from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import packageDetail, booking, contact


urlpatterns = [
    path('', views.index, name='home'),
    path('destination', views.destination, name='destination'),
    path('packages', views.packages, name='packages'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('guide', views.guide, name='guide'),
    path('gallary', views.gallary, name='gallary'),
    path('startup', views.startup, name='startup'),
    path('package/detail/<slug:slug>/', packageDetail.as_view(),name='packagedetail'),
] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)