from django.urls import path
from .views import home, add_transaction, edit_transaction, delete_transaction

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_transaction, name='add_transaction'),
    path('edit/<int:transaction_id>/', edit_transaction, name='edit_transaction'),  # URL for editing
    path('delete/<int:transaction_id>/', delete_transaction, name='delete_transaction'),  # URL for deleting
]
