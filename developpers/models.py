from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
class DevelopperManager(BaseUserManager):
    def create_user(self, username,email,prefered_language=None,picture=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            username = username,
            prefered_language=prefered_language,
            picture=picture,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username,email, password=None):
        user = self.create_user(
            username,
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class Developper(AbstractBaseUser):
    username = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique = True)
    prefered_language = models.CharField(max_length=255,default="Python",null=True,blank=True)
    picture = models.ImageField(null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login",auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser= models.BooleanField(default=False)
    REQUIRED_FIELDS = [
        'username', 
    ]
    
    objects = DevelopperManager()
    USERNAME_FIELD = 'email'
    
    def __str__(self):
        return self.username + " | "+self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

   
# Create your models here.
