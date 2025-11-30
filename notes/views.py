from django.shortcuts import render
from .models import Notes
from .serializers import NoteSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics


# Create your views here.

class NoteList(generics.ListCreateAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
   # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        self.permission_classes = [AllowAny] 
        
        if self.request.method == 'POST':
            self.permission_classes = [IsAuthenticated]
        return super().get_permissions()

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notes.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

