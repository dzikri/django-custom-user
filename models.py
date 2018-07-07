from django.db import models
from django.core.mail import send_mail
from django.utils.translation import ugettext, ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class UserManager(BaseUserManager):

    def create_user(self,username,password,email=None,is_active=True,is_staff=False,is_admin=False):
        if not username:
            raise ValueError(_('Username is empty: '),username)
        if not password:
            raise ValueError(_('Password is empty: '),password)
        user = self.model(username = username)
        user.set_password(password)
        if email: user.email = self.normalize_email(email)
        user.active = is_active
        user.staff = is_staff
        user.admin = is_admin
        user.save(using=self._db)
        return user

    def create_staffuser(self,username,password,email=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=True
        )
        return user

    def create_superuser(self,username,password,email=None):
        user = self.create_user(
            username=username,
            password=password,
            email=email,
            is_staff=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255,unique=True)
    email = models.EmailField(max_length=255,blank=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    @property
    def is_active(self):
        return self.active

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_superuser(self):
        return self.admin

    def has_perm(self,perm, obj=None):
        if self.is_admin and self.is_staff:
            return True
        return False

    def has_module_perms(self,app_label):
        return True

    def __str__(self):
        return self.username
