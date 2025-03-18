from django.urls import path
from .views import GeneralInformationListCreateView, GeneralInformationDetailView

urlpatterns = [
    path('general-info/', GeneralInformationListCreateView.as_view(), name='general-info-list-create'),
    path('general-info/<int:pk>/', GeneralInformationDetailView.as_view(), name='general-info-detail'),
]
