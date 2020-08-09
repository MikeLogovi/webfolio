from django.urls import path
from .controllers import developper_controller
app_name = "developpers"
urlpatterns = [
    path('',developper_controller.index,name="home"),
    path('register/',developper_controller.register,name="register"),
    path('login/',developper_controller.login_,name="login"),
    path('logout/',developper_controller.logout_,name="logout"),
]
