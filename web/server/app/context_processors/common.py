import json

from django.contrib.auth.models import AnonymousUser


def template(request):
    context = {}
    if isinstance(request.user, AnonymousUser):
        context.update({'is_logged_in': False})
    else:
        context.update({
            'is_logged_in': True,
            'user_id': request.user.id,
            'user_name': request.user.username,
            'is_admin': request.user.is_staff
        })
    context_json = {"common_data": json.dumps(context)}

    return context_json
