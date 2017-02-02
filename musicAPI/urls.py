from django.conf.urls import url, include
from django.contrib import admin
from APIMusic import views
from rest_framework.routers import DefaultRouter
from APIMusic.admin import *

router = DefaultRouter()
router.register(r'albums', views.AlbumViewSet)
router.register(r'artists', views.ArtistViewSet)
router.register(r'songs', views.SongViewSet)
router.register(r'genres', views.GenreViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]