from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,get_object_or_404
from Apis.serializers import *
from USMAApp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages

#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet


from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser

# Create your views here.



#-----------------------------MODEL VIEW SETS-----------------------------------

#-------KWA AJILI YA MUSIC VIDEOS MODEL--------------
class UniversitiesViewSet(ModelViewSet):
	queryset = Universities.objects.all()
	serializer_class = UniversitiesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['Created']

	#search
	search_fields = ['UniversityName']

	#Ordering videos
	ordering_fields = ['Created']

	#Pagination
	pagination_class = PageNumberPagination

# FILTER ALL COURSE MODEL FOR SPECIFIC UNIVERSITY


# UNIVERSITY OF DAR ES SALAAM
class UdsmUniversityCoursesViewSet(ModelViewSet):
	queryset = UniversityCourses.objects.filter(university__UniversityName__icontains="University of Dar es salaam")
	serializer_class = UniversityCoursesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	
	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['university','Created']

	#search
	search_fields = ['CourseName']

	#Ordering videos
	ordering_fields = ['Created']


# UNIVERSITY OF DODOMA
class UdomUniversityCoursesViewSet(ModelViewSet):
	queryset = UniversityCourses.objects.filter(university__UniversityName__icontains="University of Dodoma")
	serializer_class = UniversityCoursesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	
	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['university','Created']

	#search
	search_fields = ['CourseName']

	#Ordering videos
	ordering_fields = ['Created']


# UNIVERSITY OF MBEYA
class MustUniversityCoursesViewSet(ModelViewSet):
	queryset = UniversityCourses.objects.filter(university__UniversityName__icontains="Mbeya University")
	serializer_class = UniversityCoursesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	
	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['university','Created']

	#search
	search_fields = ['CourseName']

	#Ordering videos
	ordering_fields = ['Created']



# UNIVERSITY OF DIT
class DitUniversityCoursesViewSet(ModelViewSet):
	queryset = UniversityCourses.objects.filter(university__UniversityName__icontains="DIT")
	serializer_class = UniversityCoursesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

	
	#filter product by category and search field
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['university','Created']

	#search
	search_fields = ['CourseName']

	#Ordering videos
	ordering_fields = ['Created']























# FILTER ALL PROJECTS MODEL FOR SPECIFIC COURSE AND UNIVERSITY


# UDSM -> COMPUTER ENGINEERING
class UdsmComputerEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Computer Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



# UDSM -> ELECTRICAL ENGINEERING
class UdsmElectricalEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Electrical Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


# UDSM -> ICT
class UdsmICTAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="ICT")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

# UDSM -> OTHER PROJECTS
class UdsmOtherProjectsAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Other Projects")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination










# UDOM -> COMPUTER ENGINEERING
class UdomComputerEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Computer Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



# UDOM -> ELECTRICAL ENGINEERING
class UdomElectricalEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Electrical Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


# UDOM -> ICT
class UdomICTAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="ICT")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

# UDOM -> OTHER PROJECTS
class UdomOtherProjectsAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Other Projects")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination




# Must -> COMPUTER ENGINEERING
class MustComputerEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Computer Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



# Must -> ELECTRICAL ENGINEERING
class MustElectricalEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Electrical Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


# Must -> ICT
class MustICTAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="ICT")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

# Must -> OTHER PROJECTS
class MustOtherProjectsAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Other Projects")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination






# Dit -> COMPUTER ENGINEERING
class DitComputerEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Computer Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



# Dit -> ELECTRICAL ENGINEERING
class DitElectricalEngineeringAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Electrical Engineering")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


# Dit -> ICT
class DitICTAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="ICT")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

# Dit -> OTHER PROJECTS
class DitOtherProjectsAllProjectsViewSet(ModelViewSet):
	queryset = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Other Projects")
	serializer_class = AllProjectsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination















	# ---------------------ARTICLES-------------------------------


class ArticlesViewSet(ModelViewSet):
	queryset = Articles.objects.all()
	serializer_class = ArticlesSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------AI---------------

class AIArticlesViewSet(ModelViewSet):
	queryset = ArticlesCategory.objects.filter(
		ArticlesName__ArticlesName__icontains="AI Articles"
		)
	serializer_class = ArticlesCategorySerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------WEBSITE-------------
class WebsiteArticlesViewSet(ModelViewSet):
	queryset = ArticlesCategory.objects.filter(
		ArticlesName__ArticlesName__icontains="Website Articles"
		)
	serializer_class = ArticlesCategorySerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination




  # -------------------MOBILE APP-------------
class MobileApplicationsArticlesViewSet(ModelViewSet):
	queryset = ArticlesCategory.objects.filter(
		ArticlesName__ArticlesName__icontains="Mobile Applications Articles"
		)
	serializer_class = ArticlesCategorySerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination









	# ---------------------HOB-------------------------------


class HobsViewSet(ModelViewSet):
	queryset = Hob.objects.all()
	serializer_class = HobSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



  # -------------------WEBSITES EXPERTS-------------
class WebsitesExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Websites Developers"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------WEBSITES EXPERTS-------------
class MobileApplicationsExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Mobile Applications Developers"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------GRAPHIC DESIGNERS EXPERTS-------------
class GraphicsDesignerExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Graphics Designer"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------COMPUTER MAINTENANCE EXPERTS-------------
class ComputerMaintenanceExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Computer Maintenance Experts"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination



  # -------------------MACHINE LEARNING  EXPERTS-------------
class MachineLearningExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Machine Learning Experts"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------COMPUTER VISION  EXPERTS-------------
class ComputerVisionExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Computer Vision Experts"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination


  # -------------------AUTOMATION  EXPERTS-------------
class AutomationExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Automation Experts"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination

  # -------------------DATA ANALYSIS  EXPERTS-------------
class DataAnalysisandVisualizationExpertsViewSet(ModelViewSet):
	queryset = Experts.objects.filter(
		CategoryName__CategoryName__icontains="Data Analysis and Visualization Experts"
		)
	serializer_class = ExpertsSerializer
	# permission_classes=[IsAuthenticated]
	#Pagination
	pagination_class = PageNumberPagination