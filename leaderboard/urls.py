from django.urls import path
from .views import ScoreListCreateView

urlpatterns = [
    path('', ScoreListCreateView.as_view(), name='score-list-create'),
]
