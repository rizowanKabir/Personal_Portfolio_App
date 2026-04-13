from django.contrib import admin
from .models import Skill, Service, Portfolio, Experience, Education, Contact


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display  = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter   = ['category']


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display  = ['title', 'icon', 'order']
    list_editable = ['order']


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display  = ['title', 'technologies', 'order']
    list_editable = ['order']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display  = ['title', 'company', 'start_date', 'end_date', 'order']
    list_editable = ['order']


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display  = ['institution', 'degree', 'end_year', 'order']
    list_editable = ['order']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display     = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_editable    = ['is_read']
    readonly_fields  = ['name', 'email', 'subject', 'message', 'created_at']
