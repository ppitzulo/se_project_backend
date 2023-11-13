from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from audiomanager.views import *

urlpatterns = [
    path('list-songs/', AudioAPIView.as_view(), name='audio_fetch'),
    path('audio/<int:song_id>/', AudioAPITest.as_view(), name='audioAPITest'),
    path('audio/<int:song_id>/segment/<int:duration>/', AudioSegmentView.as_view(), name='audioAPITest'),
    path('csrf-token', CSRFTokenAPIView.as_view(), name='csrf_token'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
