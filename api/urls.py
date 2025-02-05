from django.urls import path
from .views import num_properties

urlpatterns = [
    path('classify-number', num_properties, name='classify-number'),
]