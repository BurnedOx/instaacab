from django.contrib.auth.models import Group


def get_roll(grp_name):
    try:
        roll = Group.objects.get_or_create(name=grp_name)[0]
        return roll
    except:
        return None
