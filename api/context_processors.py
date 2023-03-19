from .models import UserProfile, Assistant

def user_context(request):
    context = {}
    user_role = None
    user_obj = None
 
    if request.user.is_authenticated:
        try:
            user_obj = UserProfile.objects.get(user=request.user)
            user_role = user_obj.role
        except UserProfile.DoesNotExist:
            pass
 
    if user_role == 'doctor' or user_role == 'general_manager':
        context['profile'] = user_obj
    elif user_role == 'assistant':
        context['assistant'] = Assistant.objects.get(user=request.user)
    else:
        context['guest'] = True
     
    return context
