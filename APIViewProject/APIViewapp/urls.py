
#This url settings is applicable only for , APIView, Mixins, genericsApiView

# from django.urls import path
# from .import views

# urlpatterns = [
#     path('employee/', views.EmployeeListView.as_view()),
#     path('employee/<int:pk>/', views.EmployeeDetailView.as_view()),
# ]



#url settings for viewsets

# from django.urls import path, include
# from .import views
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()

# router.register('employee', views.Employee_ModelViewSet)

# urlpatterns = [
#     path(' ', include(router.urls)),
   
# ]