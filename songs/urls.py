from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from songs.views import *

urlpatterns = [
    path('list-songs/', AudioAPIView.as_view(), name='audio_fetch'),
    path('upload/', AudioUploadAPIView.as_view(), name='audio_upload'),
    path('playlist/<str:playlist_name>/', playlistAPIView.as_view(), name='playlistAPI'),
    path('audio/<int:song_id>/title/', SongAPIView.as_view(), name='AudioTitleView'),
    path('audio/<int:song_id>/segment/<int:duration>/', AudioSegmentView.as_view(), name='audioAPITest'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
