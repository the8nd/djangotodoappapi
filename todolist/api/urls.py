from django.urls import include, path
from rest_framework import routers
from todolist.api import views

router = routers.DefaultRouter()
router.register(r'todolist', views.ToDoListViewSet)
router.register(r'todoitem', views.ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]