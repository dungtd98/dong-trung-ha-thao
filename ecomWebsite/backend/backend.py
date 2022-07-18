from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
UserModel = get_user_model()
class EmailorUsernameModelBackend(ModelBackend):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email':username}
        else:
            kwargs = {'username':username}
        
        try:
            user = UserModel.objects.get(**kwargs)
        except UserModel.DoesNotExist:
            return None
    