from django.urls import path
from main import views


urlpatterns = [
    path("", views.hello),
    path("form/submit/", views.submit_form),
    path("form/update/<str:id_>/", views.update_form),
    path("form/delete/<str:id_>/", views.delete_form)
]

