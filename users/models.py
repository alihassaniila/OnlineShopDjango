from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

class UserManager(BaseUserManager):
    def create_user(self, email, username, phone_number, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            username=username
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, phone_number, password):
        user = self.create_user(
            phone_number= phone_number,
            email=self.normalize_email(email),
            password=password,
            username=username
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('username', max_length=32, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True)
    last_name = models.CharField('last name', max_length=30, blank=True)
    email = models.EmailField('email address', unique=True, null=True, blank=True)
    phone_number = models.BigIntegerField('mobile number', unique=True, null=True, blank=True)
    is_active = models.BooleanField('active', default=True)
    is_staff = models.BooleanField('staff status', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'phone_number']

    class Meta:
        db_table = 'users'
        verbose_name = 'user'
        verbose_name_plural = 'users'

class UserProfile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    avatar = models.ImageField('avatar', blank=True)
    birthday = models.DateField('birthday', null=True, blank=True)
    province = models.ForeignKey(verbose_name='province', to='Province', null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'user_profiles'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'

    # @property
    # def get_first_name(self):
    #     return self.user.first_name
    #
    # @property
    # def get_last_name(self):
    #     return self.user.last_name
    #
    # def get_nickname(self):
    #     return self.nick_name if self.nick_name else self.user.username
class Province(models.Model):
    name = models.CharField(max_length=50)
    is_valid = models.BooleanField(default=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name