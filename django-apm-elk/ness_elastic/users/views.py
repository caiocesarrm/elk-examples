from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, RedirectView, UpdateView
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from ness_elastic.users.serializer import CreateAuthUserSerializer
from django.contrib.auth.models import Group
from rest_framework.response import Response

User = get_user_model()


class CreateAuthUserView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    model = User
    raise_exception = True
    serializer_class = CreateAuthUserSerializer

    def create(self, request, *args, **kwargs):
        grupos = Group.objects.all()
            
        user = self.request.user
        email = self.request.data['email']

        if(User.objects.filter(email=email).exists()):
            return(Response({"success": False, "message": "Email " + email + " já cadastrado."}))

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_user = serializer.save()
        auth_user.username = serializer.validated_data['email']
        if request.data['password'] != request.data['confirm_password']:
            return Response({"success": False, 'message':'Os passwords são diferentes.'}) 
        auth_user.set_password(request.data['password'])
        auth_user.is_active = False
        auth_user.save()
        #self.send_registration_link_email(auth_user.email)

        #headers = self.get_success_headers(serializer.data)
        
        return Response({"success": True, 'message':'Cadastrado com sucesso.'})





