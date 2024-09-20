from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import Unit, WorkUnit

@receiver(post_save, sender=Unit)
def update_unit_leader_position(sender, instance, created, **kwargs):
    if instance.unit_leader:
        instance.unit_leader.position = instance.position_id
        instance.unit_leader.save()

@receiver(pre_save, sender=Unit)
def handle_unit_leader_change(sender, instance, **kwargs):
    if instance.pk:
        old_unit = Unit.objects.get(pk=instance.pk)
        if old_unit.unit_leader and old_unit.unit_leader != instance.unit_leader:
            old_unit.unit_leader.position = None
            old_unit.unit_leader.unit = None
            old_unit.unit_leader.save()

        if instance.unit_leader and old_unit.unit_leader != instance.unit_leader:
            instance.unit_leader.position = instance.position_id
            instance.unit_leader.unit = instance
            instance.unit_leader.save()

@receiver(post_save, sender=WorkUnit)
def update_workunit_manager_position(sender, instance, created, **kwargs):
    if instance.manager:
        instance.manager.position = instance.position_id
        instance.manager.save()

@receiver(pre_save, sender=WorkUnit)
def handle_workunit_manager_change(sender, instance, **kwargs):
    if instance.pk:
        old_workunit = WorkUnit.objects.get(pk=instance.pk)
        if old_workunit.manager and old_workunit.manager != instance.manager:
            old_workunit.manager.position = None
            old_workunit.manager.save()

        if instance.manager and old_workunit.manager != instance.manager:
            instance.manager.position = instance.position_id
            instance.manager.save()