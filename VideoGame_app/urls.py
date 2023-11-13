from django.contrib import admin
from django.urls import path

from VideoGame_app import views

urlpatterns = [
    path('sortGame', views.sortGame, name="sortGame"),
    path('showGame', views.showGame, name="showGame"),
    path('insertGame', views.insertGame, name="insertGame"),
    path('editGame/<int:id>', views.editGame, name="editGame"),
    path('', views.HomePage, name="HomePage"),
    path('updateGame/<int:id>', views.updateGame, name="updateGame"),
    path('delGame/<int:id>', views.delGame, name="delGame"),
    path('deletedGame/<int:id>', views.deletedGame, name="deletedGame"),
    path('runQueryGame', views.runQueryGame, name="runQueryGame"),
    path('ProcessCustomQuery/', views.ProcessCustomQuery, name="ProcessCustomQuery"),
    path('InputCustomQuery/', views.InputCustomQuery, name="InputCustomQuery"),

    path('showUser', views.showUser, name="showUser"),
    path('insertUser', views.insertUser, name="insertUser"),
    path('sortUser', views.sortUser, name="sortUser"),
    path('editUser/<int:id>', views.editUser, name="editUser"),
    path('updateUser/<int:id>', views.updateUser, name="updateUser"),
    path('delUser/<int:id>', views.delUser, name="delUser"),
    path('deletedUser/<int:id>', views.deletedUser, name="deletedUser"),
    path('runQueryUser', views.runQueryUser, name="runQueryUser"),
    path('ProcessCustomQueryforuser/', views.ProcessCustomQueryforuser, name="ProcessCustomQueryforuser"),
    path('InputCustomQueryUser/', views.InputCustomQueryUser, name="InputCustomQueryUser"),

]
