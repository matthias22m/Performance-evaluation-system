from django.contrib import admin
from .models import WorkUnit, Plan, AnnualPlan, CasualPlan, Unit, SubActivity, CharacterEvaluation

# Register your models here.
admin.site.register(WorkUnit)
admin.site.register(Plan)
admin.site.register(AnnualPlan)
admin.site.register(CasualPlan)
admin.site.register(Unit)
admin.site.register(SubActivity)
admin.site.register(CharacterEvaluation)
