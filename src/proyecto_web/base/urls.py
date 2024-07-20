from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, ElminarTarea, Login, PaginaRegistro, custom_logout
from django.contrib.auth.views import LogoutView

urlpatterns = [path("", ListaPendientes.as_view(), name="tareas"),
               path("login/", Login.as_view(), name="login"),
               path("registro/", PaginaRegistro.as_view(), name="registro"),
               path('logout/', custom_logout, name='logout'),
               path("tarea/<int:pk>", DetalleTarea.as_view(), name="tarea"),
               path("crear_tarea/", CrearTarea.as_view(), name="crear_tarea"),
               path("editar_tarea/<int:pk>", EditarTarea.as_view(), name="editar_tarea"),
               path("eliminar_tarea/<int:pk>", ElminarTarea.as_view(), name="eliminar_tarea")]
