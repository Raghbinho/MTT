from django.conf.urls import url

from . import views,forms

# urlpatterns = [
#     # url(r'^$', views.index, name='index'),
#     url(r'^$', views.home, name='home'),
# ]
# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.welcome, name='welcome'),
    # url(r'^$', views.register_success, name='success'),
    # url(r'^list$', views.filetree, name="list"),
]