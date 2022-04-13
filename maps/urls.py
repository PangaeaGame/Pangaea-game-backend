from django.urls import path
from .views import MapListCreate, MapRetrieveDelete

urlpatterns = [
    path('', MapListCreate.as_view()),
    path('<int:pk>/', MapRetrieveDelete.as_view())
]
