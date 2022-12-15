# #This url settings is applicable only for , APIView, Mixins, genericsApiView

# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('APIViewapp.urls')),
# ]


#This user settings for viewsets
from django.urls import path, include
from APIViewapp import views
from rest_framework.routers import DefaultRouter
#from rest_framework.routers import SimpleRouter

#router = SimpleRouter()
router = DefaultRouter()

router.register('employee', views.Employee_ModelViewSet, basename='employee') #when we use DefaultRouter then Basename is optional, no need to provide
                                                         #when we use SimpleRouter then you should be provide Basename

urlpatterns = [
    path('api/', include(router.urls)),
   
]