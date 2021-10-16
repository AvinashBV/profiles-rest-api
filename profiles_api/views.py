from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """Test API view"""
    
    def get(self, request, format=None):
        """returns a list of APIView features"""
        an_apiview = [
            'Uses Http methods as function (get, post, put, delete)',
            'banana',
            'orange'
        ]
        
        return Response({'message': 'Hello', 'an_apiview': an_apiview})