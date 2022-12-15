#< API VIEW CONCEPT>

# from django.shortcuts import render
# from .models import Employee
# from .serializers import EmployeeSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

#view for non -id based operation

# class EmployeeListView(APIView):
#     def get(self, request):  #db -->qs-->dict-->json -->browser
#         Employee_list = Employee.objects.all() #This queryset object, it may empty [] or it contains many records [{},{},{}]
#         serializer = EmployeeSerializer(Employee_list, many=True) #serializer class convert at a time one record but  many records is there it not converting into json thats why we write many=True.
#         #return Response(serializer)           #if we write like this then it hiding data it show like object1, object2... it successfully not converting
#         return Response(serializer.data, status=status.HTTP_200_OK)       #if we passing 'data' parameter then it show object like 'virat', 'rohit' all data displaying.... it successfully converting

#     def post(self, request): #browser --> json--> dict--> qs--> db
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# #view for id based operation

# class EmployeeDetailView(APIView):
#     def get(self,request,pk):
#         try:
#             employee = Employee.objects.get(id=pk)

#         except Employee.DoesNotExist:
#             data = {"message": "Requested Resource Not Available!"}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)
        
#         else:
#             serializer = EmployeeSerializer(employee)
#             return Response(serializer.data, status=status.HTTP_200_OK)

# #This is common code
#     def get_obj_by_id(self, pk):
#         try:
#             employee= Employee.objects.get(id=pk)
#         except:
#             employee = None
#         return employee
# #------------------------------------

#     def put(self,request,pk):
#         employee = self.get_obj_by_id(pk) #Employee object or None value we are getting    #[common code using here]

#         if employee is None:
#             data = {"message": "Requested Resource Not Available to Update!"}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)
#         else:
#             serializer = EmployeeSerializer(employee, data=request.data)  #here old data conain in 'employee', & new data contain in 'request.data', old data replace by new data.
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             else:
#                 return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#     def delete(self,request,pk):
#         employee = self.get_obj_by_id(pk) #Employee object or None value we are getting    #[common code using here]
#         if employee is None:
#             data = {"message": "Requested Resource Not Available to Delete!"}
#             return Response(data, status=status.HTTP_404_NOT_FOUND)
#         else:
#             employee.delete()
#             data = {"message": "Requested Resource deleted Successfully!"}
#             return Response(data, status=status.HTTP_204_NO_CONTENT)





# <MIXINS CONCEPT>

# from .models import Employee
# from .serializers import EmployeeSerializer
# from rest_framework import mixins, generics


# #view for non-id based operations -> get & create
# class EmployeeListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)


# #view for id based operations -> put, 
# class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request,pk):
#         return self.retrieve(request)
    
#     def put(self, request,pk):
#         return self.update(request)

#     def delete(self, request,pk):
#         return self.destroy(request)





#<Generics Concept>

# from .models import Employee
# from .serializers import EmployeeSerializer
# from rest_framework import generics


# # #view for non-id based operations
# class EmployeeListView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer


# # #view for id based operations
# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer





#<viewsets concept>

from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets


# #view for ID & non-id based operations
class Employee_ModelViewSet(viewsets.ModelViewSet):   #by using this single class we can perform id & and non id based operations, no need to define other extra class
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer