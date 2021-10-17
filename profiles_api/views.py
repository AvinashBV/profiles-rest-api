from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers, models, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.settings import api_settings


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as function (get, post, put, delete)',
            'banana',
            'orange'
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
    
    def post(self, request):
        """Create a Hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, pk=None):
        """Handle updating an object"""
        return Response({'method': 'PUT'})
    
    
    def patch(self, request, pk=None):
        """Handle partial update an object"""
        return Response({'method': 'PATCH'})
    
    def delete(self, request, pk=None):
        """delete an object"""
        return Response({'method': 'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        """returns a list of viewset features"""
        a_viewset = [
            'Uses Http methods as function (list, create, update, destroy)',
            'banana',
            'orange'
        ]
        
        return Response({'message': 'Hello', 'a_viewset': a_viewset})
    
    def create(self, request):
        """create a new hello message"""
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
            
    def retreive(self, request, pk=None):
        """handle getting an object by ID"""
        return Response({"http_method": "GET"})
    
    
    def update(self, request, pk=None):
        """handle update of an object"""
        return Response({"http_method": 'PUT'})
    
    
    def partial_update(self, request, pk=None):
        """handle updating part of an object"""
        return Response({"http_method": 'PATCH'})
    
        
    def destroy(self, request, pk=None):
        """handle delete of an object"""
        return Response({"http_method": 'Delete'})
 
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
    

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES