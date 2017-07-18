from django.conf.urls import url
from . import views

app_name = 'homepage'

urlpatterns = [
	# /
    url(r'^$', views.index, name="index"),

    # /about/
    url(r'^about/', views.about, name="about"),
]