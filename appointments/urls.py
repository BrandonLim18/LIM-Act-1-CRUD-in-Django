from django.urls import path
from .views import (
    DoctorListCreateView, DoctorRetrieveUpdateDestroyView,
    PatientListCreateView, PatientRetrieveUpdateDestroyView,
    AppointmentListCreateView, AppointmentRetrieveUpdateDestroyView
)

urlpatterns = [
    # Doctor URLs
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDestroyView.as_view(), name='doctor-detail'),
    
    # Patient URLs
    path('patients/', PatientListCreateView.as_view(), name='patient-list-create'),
    path('patients/<int:pk>/', PatientRetrieveUpdateDestroyView.as_view(), name='patient-detail'),
    
    # Appointment URLs
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentRetrieveUpdateDestroyView.as_view(), name='appointment-detail'),
]