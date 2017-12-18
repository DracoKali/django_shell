from apps.user_login.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

# use this function to create users with validations
def create_valid_user():

    user = {}
    print "Enter a First Name"
    user['first_name'] = raw_input()

    print "Enter a Last Name"
    user['last_name'] = raw_input()

    print "Enter an Email Address"
    user['email'] = raw_input()

    print "Enter an Age"
    user['age'] = raw_input()

   
    if is_valid(**user):
        User.objects.create(**user)
        print "successfully created a user"

def is_valid(**kwargs):
    valid = True
    
    existing = User.objects.filter(email=kwargs['email'])
    if len(existing) > 0:
        valid = False
        print "Email is already in use"
    if len(kwargs['first_name']) < 3 or len(kwargs['last_name']) < 3:
        valid = False
        print 'Name fields must be at least 3 characters'


    try:
        validate_email(kwargs['email'])
    except ValidationError:
        valid = False
        print "invalid email"
    
    return valid