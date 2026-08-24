from django.urls import path
from main.views import hello,hello_piyush,hello_jatin,form


urlpatterns = [
    path("", hello),
    path("piyush/", hello_piyush),
    path("jatin/", hello_jatin),
    path("form/", form)
]