from django.urls import path
from . import views

urlpatterns = [
    path("",views.top, name="top"),
    path("flow/<int:pk>/", views.flow, name="flow"),
    path("<int:pk>/", views.detail, name="detail"),
    path("favorites/", views.favorites, name="favorites"),
    path("search/", views.search, name="search"),

    #フォローフォーム
    path("flow/create/", views.flow_create, name="flow_create"),
    path("flow/<int:pk>/edit/", views.flow_update, name="flow_edit"),
    path("flow/<int:pk>/delete/", views.flow_delete, name="flow_delete"),

    #リファレンスフォーム
    path("create/",views.create, name="create"),
    path("<int:pk>/edit/",views.update, name="edit"),
    path("<int:pk>/delete/",views.delete, name="delete"),
]

# edit = ユーザー向けの画面名 ,update = プログラム上の処理名