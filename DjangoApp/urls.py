"""DjangoApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path, include
# from api import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('schools/', views.SchoolList.as_view()),
#     # path('schools/<int:pk>', views.SchoolDetails.as_view()),
#     # path('students/', views.StudentList.as_view()),
#     # path('students/<int:pk>', views.StudentDetails.as_view()),
#     # path('schools/<int:school_pk>/students/', views.StudentsInSchool.as_view())
# ]
from django.urls import path, include
from api import views

from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = routers.DefaultRouter()
router.register("nested/schools",views.SchoolVeiwSet)
# router.register("students",views.StudentList)

school_router = routers.NestedDefaultRouter(router,"nested/schools",lookup="school")
school_router.register("students",views.StudentViewSet, basename="school-sudents-list")


urlpatterns = router.urls

urlpatterns = [
    # path('schools/', views.SchoolList.as_view()),
    # path('schools/<int:pk>/', views.SchoolDetails.as_view()),
    # path('students/', views.StudentList.as_view()),
    # path('students/<int:pk>/', views.StudentDetails.as_view()),
    # path('schools/<int:school_pk>/students/', views.StudentsInSchool.as_view()),
    path("",include(router.urls)),
    path("",include(school_router.urls)),
]
