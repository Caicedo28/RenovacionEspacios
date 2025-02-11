#URLS especificas de la Aplicacion "Espacios"
from django.urls import path
from . import views
urlpatterns=[
    path('',views.inicio),
    path('nuevoAreaPublica/',views.nuevoAreaPublica),
    path('listadoAreaPublica/',views.listadoAreaPublica),
    path('guardarAreaPublica/',views.guardarAreaPublica),
    path('eliminarAreaPublica/<idAre>',views.eliminarAreaPublica),
    path('editarAreaPublica/<idAre>',views.editarAreaPublica),
    path('procesarEdicionAreaPublica/',views.procesarEdicionAreaPublica),

    path('nuevoProyecto/',views.nuevoProyecto),
    path('listadoProyecto/',views.listadoProyecto),
    path('guardarProyecto/',views.guardarProyecto),
    path('eliminarProyecto/<idPro>',views.eliminarProyecto),
    path('editarProyecto/<idPro>',views.editarProyecto),
    path('procesarEdicionProyecto/',views.procesarEdicionProyecto),

    path('nuevoContratista/',views.nuevoContratista),
    path('listadoContratista/',views.listadoContratista),
    path('guardarContratista/',views.guardarContratista),
    path('eliminarContratista/<idCon>',views.eliminarContratista),
    path('editarContratista/<idCon>',views.editarContratista),
    path('procesarEdicionContratista/',views.procesarEdicionContratista),

    path('nuevoMaterial/',views.nuevoMaterial),
    path('listadoMaterial/',views.listadoMaterial),
    path('guardarMaterial/',views.guardarMaterial),
    path('eliminarMaterial/<idMat>',views.eliminarMaterial),
    path('editarMaterial/<idMat>',views.editarMaterial),
    path('procesarEdicionMaterial/',views.procesarEdicionMaterial),
]