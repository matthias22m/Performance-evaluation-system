from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
Employee = get_user_model()
 

class WorkUnit(models.Model):
    name = models.CharField(max_length=255)
    position_id = models.CharField(max_length=30, unique=True)
    manager = models.OneToOneField(Employee, on_delete=models.SET_NULL, null=True, related_name='managed_work_units')

    def __str__(self):
        return self.name

class Unit(models.Model):
    name = models.CharField(max_length=255, unique=True)
    position_id = models.CharField(max_length=30, unique=True)
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
    activity = models.TextField()
    weight = models.FloatField()
    result = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f'Annual Plan for {self.plan.unit.name} - {self.activity[0:20]}'


class CasualPlan(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, related_name='casual_plans')
    deadline = models.DateField()
    activity = models.TextField()
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
        return f'Sub Activity for {self.employee.email}'

'''
Implication

behavior_one => ፀረ ኪራይ ሰብሳቢነት፣ አመለካከትና ተግባር ለማስወገድ የሚያሳየው ጥረት
behavior_two => ብቃቱን ለማሳደግ የሚያደርገው ጥረት
behavior_three => ለተገልጋዩ የሚሰጠው ክብርና በማገልገሉ የሚሰማው ኩራት 
behavior_four => ሌሎችን ለመደገፍና ለማብቃት የሚያደርገው ጥረት
behavior_five => አሠራሩን ለማሻሻልና በኢኮቴ ለማስደገፍ የሚያደርገው ጥረትና ዝንባሌ
behavior_six => የአፈፃፀም ግብረ መልስ በወቅቱና በአግባቡ የመስጠትና የመቀበል ዝንባሌ
'''

class CharacterEvaluation(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='evaluations')
    evaluator = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='given_evaluations')
    evaluation_date = models.DateField(auto_now=True)
    behavior_one = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    behavior_two = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    behavior_three = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    behavior_four = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    behavior_five = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    behavior_six = models.FloatField(default=1,validators=[MinValueValidator(1), MaxValueValidator(4)])
    result = models.FloatField(default=0)
    
    class Meta:
        unique_together = ('evaluator', 'employee')

    def __str__(self):
        return f'Evaluation for {self.employee.first_name} by {self.evaluator.first_name}'

