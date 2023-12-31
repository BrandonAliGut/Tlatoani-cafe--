from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import Group
import datetime
import django.contrib.auth.password_validation as validators



class MyUserManager(BaseUserManager):
    
        
    def create_user(self, email,name, lastname, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name = name,
            lastname=lastname,
        )
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, lastname, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            lastname=lastname,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user



class User_models(AbstractBaseUser,PermissionsMixin):
    email           = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    
    name            = models.CharField(max_length=50, verbose_name="name people")
    lastname        = models.CharField(max_length=50, verbose_name="last name people")
    is_active       = models.BooleanField(default=True)
    #is_staff=   models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    created_at      = models.DateField( auto_now_add=True, editable=False)
    update_at       = models.DateField(default=datetime.datetime.now())

    objects         = MyUserManager()
    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["name","lastname",]

    def __str__(self):
        return self.email

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
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        
