from django.conf.urls import url
from . import views

app_name = 'editpage'

urlpatterns = [
	# /edit/
    url(r'^$', views.index, name="index"),
]