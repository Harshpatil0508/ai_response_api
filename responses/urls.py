from django.urls import path
from .views import ResponseListCreateView, ResponseDetailView

urlpatterns = [
    path('responses/', ResponseListCreateView.as_view(), name='response-list-create'),
    path('responses/<int:pk>/', ResponseDetailView.as_view(), name='response-detail'),
]