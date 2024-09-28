from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_type', 'category', 'amount', 'date', 'description')
    search_fields = ('category', 'description', 'amount')
    list_filter = ('transaction_type', 'date')
    ordering = ('-date',)  # Order by date descending

    # Optional: Customizing the form layout
    fieldsets = (
        (None, {
            'fields': ('transaction_type', 'category', 'amount', 'date', 'description')
        }),
    )





