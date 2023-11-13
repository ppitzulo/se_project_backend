from rest_framework import generics
from .models import Score
from .serializer import ScoreSerializer

# Create your views here.
class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer