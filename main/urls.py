from django.urls import path
from main.views import show_main, create_form_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register,login_user,logout_user,edit_product,delete_product,edit_form, delete_form

app_name = 'main'

urlpatterns = [
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('json/', show_json, name='show_json'),
    path('create-form-entry', create_form_entry, name='create_form_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('', show_main, name='show_main'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    path('edit-mood/<uuid:id>', edit_form, name='edit_form'),
    path('delete/<uuid:id>', delete_form, name='delete_form'),
]