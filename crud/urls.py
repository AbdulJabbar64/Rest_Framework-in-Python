from django.urls import path
from . import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='CRUD API')


urlpatterns = [
    # path("swagger-doc/", schema_view),
    path("stud/", views.StudentAPI.as_view()),
]