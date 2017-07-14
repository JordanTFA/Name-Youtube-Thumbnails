from django.conf.urls import url
from . import views

app_name = 'aboutpage'

urlpatterns = [
	# /about/
    url(r'^$', views.index, name="index"),
]