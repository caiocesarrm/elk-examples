from django.urls import path

from ness_elastic.users.views import *

app_name = "users"
urlpatterns = [

    path("create/", view=CreateAuthUserView.as_view()),
]
