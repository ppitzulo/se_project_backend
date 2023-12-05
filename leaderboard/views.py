from rest_framework import generics
from .models import Score
from .serializer import ScoreSerializer

# Create your views here.
class ScoreListCreateView(generics.ListCreateAPIView):
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer

    def get_queryset(self):
        # Return the top ten highest scores
        return Score.objects.order_by('-score')[:10]