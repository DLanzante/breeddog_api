from rest_framework import generics
from .models import Dog, Breed
from .serializers import DogSerializer, BreedSerializer

# Dog API Views
class DogList(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class DogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

# Breed API Views
class BreedList(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer

class BreedDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
