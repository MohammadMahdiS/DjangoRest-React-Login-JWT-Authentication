from django.urls import path
from .views import RegisterView, RetriveUserView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('me/', RetriveUserView.as_view(), name="me")

]