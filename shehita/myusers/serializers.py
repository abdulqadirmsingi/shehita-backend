import re
from .models import User
from djoser.serializers import UserSerializer, UserCreateSerializer

class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username', 'password', 'email']

        
    def validate_first_name(self, value):
        return re.sub(r'[^\w]', '', value)
    
    def validate_username(self, value):
        return re.sub(r'[^\w]', '', value)
    
    def validate_last_name(self, value):
        return re.sub(r'[^\w]', '', value)


class CurrentUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','username','email']


#  {
#   "first_name": "john",
#   "last_name": "doe",
#   "username": "john_doe",
#   "password": "securePassword123",
#   "email": "john.doe@example.com"
# }