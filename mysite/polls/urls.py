from django.conf.urls import url
from .views import index, person_list, person_add
urlpatterns = [
    url(r'^asas/(?P<context>[0-9]+)', index),
    url(r'^list/', person_list, name='list'),
    url(r'^add/', person_add, name='add'),

]