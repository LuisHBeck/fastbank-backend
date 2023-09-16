from django.contrib import admin

from .models import (
	NaturalPerson,
	LegalPerson,
	Address,
	Email,
	Phone,
)

@admin.register(NaturalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
	list_display = [
		'name',
		'birth_date',
		'cpf',
		'rg',
		'social_name',
	]


@admin.register(LegalPerson)
class NaturalPersonAdmin(admin.ModelAdmin):
	list_display = [
		'fantasy_name',
		'establishment_date',
		'cnpj',
		'municipal_registration',
		'state_registration',
		'legal_nature'
	]