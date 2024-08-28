from django.db import models
from django.contrib.auth import get_user_model

Employee = get_user_model()
 

class WorkUnit(models.Model):
    name = models.CharField(max_length=255)
    manager = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_work_units')

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255)
    unit_leader = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, related_name='led_unit')
    work_unit = models.ForeignKey(WorkUnit, on_delete=models.CASCADE, related_name='units')

    def __str__(self):
        return self.name


class Plan(models.Model):
    work_unit = models.ForeignKey(WorkUnit, on_delete=models.CASCADE, related_name='plans')
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='plans')

    def __str__(self):
        return f'Plan for {self.unit.name}'

class AnnualPlan(models.Model):
    MONTH_CHOICES = [
        ('H1', 'First 6 Months (Jan-Jun)'),
        ('H2', 'Second 6 Months (Jul-Dec)'),
    ]
    
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='annual_plans')
    months = models.CharField(max_length=2, choices=MONTH_CHOICES)
    weight = models.FloatField()
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Annual Plan for {self.plan.unit.name}'


class CasualPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='casual_plans')
    deadline = models.DateField()
    weight = models.FloatField()
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Casual Plan for {self.plan.unit.name}'


class SubActivity(models.Model):
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='sub_activities')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='sub_activities')
    deadline = models.DateField()
    activity = models.TextField()
    weight = models.FloatField()
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Sub Activity for {self.employee.name}'



class CharacterEvaluation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='given_evaluations')
    evaluation_date = models.DateField()
    behavior_description = models.ForeignKey('BehaviorDescription', on_delete=models.CASCADE)

    def __str__(self):
        return f'Evaluation for {self.employee.name} by {self.evaluator.name}'

class BehaviorDescription(models.Model):
    character_evaluation = models.ForeignKey(CharacterEvaluation, on_delete=models.CASCADE)
    description = models.TextField()
    weight = models.FloatField()
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.description
