from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer
from django.contrib.auth import get_user_model, login
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect

def landing_page(request):
    if request.user.is_authenticated:
        # Render the landing page for authenticated users
        ...
    else:
        return redirect('user-login')

class CustomUserList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomUserDetail(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        try:
            user = CustomUser.objects.get(pk=pk)
            self.check_object_permissions(self.request, user)
            return user
        except CustomUser.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(
            instance=user, data=request.data, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLoginView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user = request.user
            serializer = CustomUserSerializer(user)
            return Response({'user_data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)
        
    def post(self, request, *args, **kwargs):
            username = request.data.get('username')
            password = request.data.get('password')

            if username is None or password is None:
                return Response({'detail': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

            User = get_user_model()
            user = User.objects.filter(username=username).first()
            print (user,user.check_password(password),user.password)

            if user and user.check_password(password):
                login(request, user)  # Manually login the user
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid login credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            
class UserLogoutView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.auth.delete()  # This will delete the token and effectively "log out" the user.
        return Response(status=status.HTTP_200_OK)
            

class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = CustomUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            role_data = request.data.get('role')  # Get the role from request data
            if role_data is not None:
                role = role_data.lower()  # Convert to lowercase if role_data is not None
            else:
                # Default role handling, you can choose what to do here
                role = 'attendee'  # or return an error, or whatever makes sense for your application

            print(f"Backend received role: {role}")

            # Check role and set the corresponding flags
            if role == 'organiser':
                serializer.validated_data['is_organiser'] = True
                serializer.validated_data['is_attendee'] = False
            elif role == 'attendee':
                serializer.validated_data['is_attendee'] = True
                serializer.validated_data['is_organiser'] = False
            # You can add other roles here as needed.

            print(f"Serializer validated data: {serializer.validated_data}")

            user = serializer.save()  # Save the user after updating the flags

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
