from .models import Users
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests
from django.shortcuts import redirect

def home(request):
    return redirect("users")

class UsersAPI(APIView):
    def get(self,request):
        query = request.query_params.get('q')
        if query is not None:
            search = Users.objects.filter(first_name__icontains=query)
            if search:
                serializer = UsersSerializer(search,many=True)
                return Response(serializer.data)
            else:
                response = requests.get("https://dummyjson.com/users/search?q=" + query)
                if response.status_code == 200:
                    data = response.json()['users']                    
                    for i in range(len(data)):
                        x = Users()
                        x.first_name = data[i]['firstName']
                        x.last_name = data[i]['lastName']
                        x.age = data[i]['age']
                        x.gender = data[i]['gender']
                        x.email = data[i]['email']
                        x.phone = data[i]['phone']
                        x.Birth_date = data[i]['birthDate']
                        x.save()
                        
                    search = reversed(Users.objects.all().order_by('-id')[:len(data)])
                    serializer = UsersSerializer(search,many=True)
                    return Response(serializer.data)
                else:
                    return Response({'message':'Something went wrong'},status=status.HTTP_400_BAD_REQUEST)
                    
        search = Users.objects.all()
        serializer = UsersSerializer(search,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk=None):
        id = pk
        search = Users.objects.get(pk=id)
        serializer = UsersSerializer(search,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None):
        id = pk
        search = Users.objects.get(pk=id)
        serializer = UsersSerializer(search,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk=None):
        if pk is not None:
            search = Users.objects.get(pk=pk)
            search.delete()
        else:
            search = Users.objects.all()
            search.delete()
        return Response({'msg':'Data Deleted'})