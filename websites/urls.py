from django.urls import path
from .controllers import website_controller
app_name = "websites"
urlpatterns = [
    path('',website_controller.index,name="list"),
    path('create/',website_controller.create,name="create"),
    path('edit/<int:id>',website_controller.edit,name="edit"),
   
    path('delete/<int:id>',website_controller.delete,name="delete"),
    path('<str:slug>',website_controller.show,name="detail")
]