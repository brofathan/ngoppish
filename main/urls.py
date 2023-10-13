from django.urls import path
#from .views import main_page, form_page, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', main_page, name="homepage"),
    path('create-product/', form_page, name="create-product"),
    path('register/', register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_user, name="logout"),

    path("delete/<int:id>", delete_product, name="delete-product"),
    path("edit/<int:id>/<int:param>", edit_product, name="edit-amount"),

    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 

    path('get-product/', get_product_json, name='get_product_json'),
    path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
    path('delete-product/<int:id>', delete_product_ajax, name='delete_product_ajax')
]
