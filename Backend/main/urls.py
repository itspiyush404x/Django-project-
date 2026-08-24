from django.urls import path
from main.views import hello,hello_piyush,hello_jatin


urlpatterns = [
    path("", hello),
    path("piyush/", hello_piyush),
    path("jatin/", hello_jatin),
]