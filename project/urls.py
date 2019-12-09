from django.urls import include, path, re_path

from . import views

urlpatterns = [
    path('ass_list/<str:slug>', views.list_assignment),
    path('view_ass/<str:slug>', views.view_assignment),
    path('create_ass/<str:slug>', views.create_assignment),
    path('open_project/', views.open_project),
    path('update_assignment/<str:slug>', views.update_assignment),
    path('delete_assignment/<str:slug>', views.delete_assignment),
    path('add_sub/<str:slug>', views.add_submission),
    path('view_sub/<str:slug>', views.evaluation),
    path('view_your_marks/<str:slug>', views.viewmarks),
    path('delete_comment/<str:slug>/<str:slugs>', views.delete_comment),
    path('add_comment/<str:slug>', views.add_comment),
    path('view_submission/<str:slug>/<str:submit_by>', views.submitby),
]
