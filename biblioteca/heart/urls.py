from django.urls import path

from . import views
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from Blibioteca import settings

urlpatterns = [

#------ paginas livro ---
    path('heart/livros/',views.Livros_lis),
    path('heart/cadastrar_liv/',views.Formulario_liv),
    path('heart/editar/',views.Livros_reg),
    path('heart/detalhes/<int:id>/',views.Detalhes_liv),
    path('heart/deletar/<int:id>/', views.Deletar_liv),
    path('heart/editar/submit',views.Editar_liv),

#-------paginas editora-----
    path('heart/editora/', views.Editoras_lis),
    path('heart/detalhes_edi/<int:id>',views.Detalhes_Edi),
    path('heart/cadastrar_edi/',views.Editora_reg),
    path('heart/cadastrar_edi/submit',views.Cadastrar_edi),
    path('heart/deletar_edi/<int:id>/',views.Deletar_edi),

#-------paginas de reserva-----
    path('heart/reserva/',views.Reservar_lis),
    path('heart/editar_res/',views.Reserva_reg),
    path('heart/deletar_res/<int:id>',views.Deletar_res),
    path('heart/cadastrar_res/',views.Formulario_res),

#------- index,login,logout,cadastrar user-----
    path('',views.Index,name = 'index'),
    path('heart/index/',views.Index),
    path('heart/user/',views.Usuario),
    path('heart/login/',views.Login),
    path('heart/login/submit',views.Login_user),
    path('heart/logout/',views.Login),
    path('heart/cadastrar_user/',views.Cadastrar_User),
    path('heart/deletar_user/<int:id>',views.Deletar_user)

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)