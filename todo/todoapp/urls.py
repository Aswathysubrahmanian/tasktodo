
from django.urls import path
from . import views

urlpatterns = [

    path("",views.home,name="home"),
    # path("details/", views.details, name="details"),
    path("delete/<int:taskid>/",views.delete,name="delete"),
    path("edit/<int:id>/", views.update, name="update"),
    path("classhome/",views.Tasklistview.as_view(),name="classhome"),
    path("cbvdetail/<int:pk>/",views.DetailView.as_view(),name="cbvdetail"),
    path("cbvupdate/<int:pk>/",views.updateview.as_view(),name="cbvupdate"),
    path("cbvdelete/<int:pk>/",views.deleteview.as_view(),name="cbvdelete"),

]
