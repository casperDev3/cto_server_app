from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import UserRequest
from .serializers import UserRequestSerializer
from .serializers import PreventionSerializer

class PreventionView(APIView):
    def post(self, request):
        serializer = PreventionSerializer(data=request.data)
        if serializer.is_valid():
            # Тут можна зберегти дані або відправити їх адміністратору
            print(serializer.validated_data)  # Наприклад, вивести дані в консоль
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_requests(request):
    try:
        user_requests = UserRequest.objects.all()
        serializer = UserRequestSerializer(user_requests, many=True)
        return Response(serializer.data)
    except UserRequest.DoesNotExist:
        return Response({"detail": "No user requests found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def create_user_request(request):
    try:
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_user_request(request, pk):
    try:
        user_request = UserRequest.objects.get(pk=pk)
        serializer = UserRequestSerializer(user_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except UserRequest.DoesNotExist:
        return Response({"detail": "Request not found."}, status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_user_request(request, pk):
    try:
        user_request = UserRequest.objects.get(pk=pk)
        user_request.delete()
        return Response({"detail": "Request deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    except UserRequest.DoesNotExist:
        return Response({"detail": "Request not found."}, status=status.HTTP_404_NOT_FOUND)
