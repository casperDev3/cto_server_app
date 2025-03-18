from rest_framework import generics
from .models import GeneralInformation
from .serializers import GeneralInformationSerializer

# Список и создание записей (GET, POST)
class GeneralInformationListCreateView(generics.ListCreateAPIView):
    queryset = GeneralInformation.objects.all()
    serializer_class = GeneralInformationSerializer

# Детальный просмотр, обновление и удаление (GET, PUT, DELETE)
class GeneralInformationDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = GeneralInformation.objects.all()
    serializer_class = GeneralInformationSerializer
