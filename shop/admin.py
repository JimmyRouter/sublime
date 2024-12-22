from django.contrib import admin
from django import forms
from .models import *


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('cat_tag', 'cat_name', 'cat_description')


class UnitsAdmin(admin.ModelAdmin):
    list_display = ('unit_tag', 'unit_name', 'unit_okei')


class TicketsAdmin(admin.ModelAdmin):
    list_display = ('client_email', 'client_phone', 'client_name', 'ticket_subject')


class ServicesAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('cat', 'tag', 'name', 'description', 'unit', 'unit_price', 'img', 'ico')
        widgets = {
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 20}),
        }


class ServicesAdmin(admin.ModelAdmin):
    form = ServicesAdminForm
    list_display = ('cat', 'tag', 'name', 'description', 'unit', 'unit_price', 'img', 'ico')


admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Units, UnitsAdmin)
admin.site.register(Product, ServicesAdmin)
admin.site.register(Tickets, TicketsAdmin)


