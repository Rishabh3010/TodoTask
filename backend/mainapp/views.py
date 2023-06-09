from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from .models import Todo
from .serializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class Todo_fetch(APIView):
    authentication_classes = [JWTAuthentication] #Adding the JWTAuthentication class to the authentication_classes, by default it will check the Authorization header for the token
    permission_classes = [IsAuthenticated] #Adding the IsAuthenticated class to the permission_classes, by default it will check if the user is authenticated or not

    def get(self, request):
        user = request.user
        todos = Todo.objects.filter(user=user) #Filtering the todos based on the user
        serializer = TodoSerializer(todos, many=True) #Serializing the todos, many=True because we are serializing a list of todos
        return Response({'status': 'success', 'message': 'Todos fetched successfully', 'data': serializer.data})
    


class Todo_add(APIView):  
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            user = request.user
            data = request.data
            data['user'] = user.id #Adding the user id to the data
            serializer = TodoSerializer(data=data)
            if not serializer.is_valid(): #Checking if the data is valid or not
                return Response({'status': 'error', 'message': serializer.errors})
            serializer.save() #Saving the data to the database if the data is valid
            return Response({'status': 'success', 'message': 'Todo created successfully', 'data': serializer.data})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e), 'data': {}})
    
class Todo_update(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def patch(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({'status': 'error', 'message': 'uid is required'})
            obj = Todo.objects.filter(uid = data.get('uid')) #Getting the todo object based on the uid
            if not obj.exists():
                return Response({'status': 'error', 'message': 'Todo does not exist for the given uid'})
            
            serializer = TodoSerializer(obj[0], data=data, partial=True) #Passing the data and partial=true to update only the fields that are passed in the request

            if not serializer.is_valid():
                return Response({'status': 'error', 'message': serializer.errors}) 
            serializer.save() 
            return Response({'status': 'success', 'message': 'Todo updated successfully', 'data': serializer.data})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e), 'data': {}})

class Todo_delete(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request):
        try:
            data = request.data
            if not data.get('uid'):
                return Response({'status': 'error', 'message': 'uid is required'})
            obj = Todo.objects.filter(uid = data.get('uid'))
            if not obj.exists():
                return Response({'status': 'error', 'message': 'Todo does not exist for the given uid'})
            obj[0].delete() #Deleting the todo object
            return Response({'status': 'success', 'message': 'Todo deleted successfully', 'data': {}})
        except Exception as e:
            return Response({'status': 'error', 'message': str(e), 'data': {}})
    


