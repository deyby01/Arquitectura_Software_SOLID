from django.urls import path
from .views import OrdenView

urlpatterns = [
    path('ordenes/', OrdenView.as_view(), name='crear-orden'),
]