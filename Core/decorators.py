from django.http import HttpResponseForbidden
from functools import wraps

def position_required(view_func):
    """
    Decorator to check if the logged-in user has a non-None position.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            try:
                user_position = request.user.led_unit
            except:
                return HttpResponseForbidden("You do not have permission to access this resource.")

            if user_position is not None:
                return view_func(request, *args, **kwargs)
            return HttpResponseForbidden("You do not have permission to access this resource.")
        return HttpResponseForbidden("You must be logged in to access this resource.")
    
    return _wrapped_view
