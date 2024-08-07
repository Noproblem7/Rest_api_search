from django.urls import path
from .views import ArtistAPIView, AlbumAPIView, SongAPIView, SongDetailAPIView, AlbumDetailAPIView, ArtistDetailAPIView

urlpatterns = [
    path('artist/', ArtistAPIView.as_view(), name='artist'),
    path('album/', AlbumAPIView.as_view(), name='album'),
    path('song/', SongAPIView.as_view(), name='song'),
    path('song/<int:id>/', SongDetailAPIView.as_view(), name='song-detail'),
    path('album/<int:id>/', AlbumDetailAPIView.as_view(), name='album-detail'),
    path('artist/<int:id>/', ArtistDetailAPIView.as_view(), name='artist-detail'),
]