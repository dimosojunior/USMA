from django.urls import path
from . import views

# MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Universities', views.UniversitiesViewSet)



router.register('UdsmUniversityCourses', views.UdsmUniversityCoursesViewSet)
router.register('UdomUniversityCourses', views.UdomUniversityCoursesViewSet)
router.register('MustUniversityCourses', views.MustUniversityCoursesViewSet)
router.register('DitUniversityCourses', views.DitUniversityCoursesViewSet)


# UDS PROJECTS
router.register('UdsmComputerEngineeringAllProjects', views.UdsmComputerEngineeringAllProjectsViewSet)
router.register('UdsmElectricalEngineeringAllProjects', views.UdsmElectricalEngineeringAllProjectsViewSet)
router.register('UdsmICTAllProjects', views.UdsmICTAllProjectsViewSet)
router.register('UdsmOtherProjectsAllProjects', views.UdsmOtherProjectsAllProjectsViewSet)



# UDOM PROJECTS
router.register('UdomComputerEngineeringAllProjects', views.UdomComputerEngineeringAllProjectsViewSet)
router.register('UdomElectricalEngineeringAllProjects', views.UdomElectricalEngineeringAllProjectsViewSet)
router.register('UdomICTAllProjects', views.UdomICTAllProjectsViewSet)
router.register('UdomOtherProjectsAllProjects', views.UdomOtherProjectsAllProjectsViewSet)


# MUST PROJECTS
router.register('MustComputerEngineeringAllProjects', views.MustComputerEngineeringAllProjectsViewSet)
router.register('MustElectricalEngineeringAllProjects', views.MustElectricalEngineeringAllProjectsViewSet)
router.register('MustICTAllProjects', views.MustICTAllProjectsViewSet)
router.register('MustOtherProjectsAllProjects', views.MustOtherProjectsAllProjectsViewSet)





# DIT PROJECTS
router.register('DitComputerEngineeringAllProjects', views.DitComputerEngineeringAllProjectsViewSet)
router.register('DitElectricalEngineeringAllProjects', views.DitElectricalEngineeringAllProjectsViewSet)
router.register('DitICTAllProjects', views.DitICTAllProjectsViewSet)
router.register('DitOtherProjectsAllProjects', views.DitOtherProjectsAllProjectsViewSet)










#ARTICLES
router.register('Articles', views.ArticlesViewSet)


router.register('AIArticles', views.AIArticlesViewSet)
router.register('WebsiteArticles', views.WebsiteArticlesViewSet)
router.register('MobileApplicationsArticles', views.MobileApplicationsArticlesViewSet)



#HOB
router.register('Hobs', views.HobsViewSet)

router.register('WebsitesExperts', views.WebsitesExpertsViewSet)
router.register('MobileApplicationsExperts', views.MobileApplicationsExpertsViewSet)
router.register('GraphicsDesignerExperts', views.GraphicsDesignerExpertsViewSet)
router.register('ComputerMaintenanceExperts', views.ComputerMaintenanceExpertsViewSet)
router.register('MachineLearningExperts', views.MachineLearningExpertsViewSet)
router.register('ComputerVisionExperts', views.ComputerVisionExpertsViewSet)
router.register('AutomationExperts', views.AutomationExpertsViewSet)
router.register('DataAnalysisandVisualizationExperts', views.DataAnalysisandVisualizationExpertsViewSet)




# router.register('CategoryViewSet', views.CategoryViewSet)



#cart router
# router.register('CartViewSet', views.CartViewSet)

#------MWISHO HAPA THEN KAREGISTE KWENYE URL PATTERN---------

urlpatterns = router.urls