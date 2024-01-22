from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.recepies, name="Recepies"),
    path('delete/<id>', views.delete_r, name="Delete"),
    path('update/<id>', views.update_r, name="Update"),
]
