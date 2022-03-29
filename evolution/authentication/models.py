from django.db import models
from django.apps import apps
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone

class UserManager(BaseUserManager):
    def _create_user(self, username, email, birth, sex, password, **extra_fields):
        if not email:
            raise ValueError('이메일 주소는 필수로 입력되어야 합니다.')
        GlobalUserModel = apps.get_model(self.model._meta.app_label, self.model._meta.object_name)
        user = self.model(
            email=self.normalize_email(email), # 이메일의 도메인 부분을 소문자로 처리한다(BaseUserManager에 정의된 함수)
            username = username,
            birth=birth,
            sex=sex,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_user(self, username, email=None, birth=None, sex=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, birth, sex, password, **extra_fields)


    def create_superuser(self, username, email, birth, sex, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self._create_user(username, email, birth, sex, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email',
        max_length=100,
        unique=True
    )
    # username 부분은 django의 github에서 abstractuser모델의 username에서 그대로 가져옴
    # 아이디로 입력받은 값이 사용 가능한 값인지 확
    username_validator = UnicodeUsernameValidator()
    username=models.CharField(
        _('username'),
        max_length=100,
        unique=True,
        help_text=_('Required. 100 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("이 아이디는 이미 존재합니다."),
        },
    )

    birth=models.DateField(
        auto_now=False,
        unique=False,
        max_length=50,
    )

    sex = models.CharField(
        max_length=10,
    )
    is_general = models.BooleanField(default=True)
    is_owner = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(
        verbose_name=_('Date joined'),
        default=timezone.now
    )

    objects= UserManager() # default manager

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username' # username을 id로 사용한다.
    REQUIRED_FIELDS = ['email','birth', 'sex']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)
    def get_full_name(self):
        return self.username
    def get_short_name(self):
        return self.username

    get_full_name.short_description = _('Full name')

class address_model(models.Model):
    address_id = models.AutoField(primary_key=True, db_column='address_id')
    x = models.CharField(max_length=30, db_column='x')
    y = models.CharField(max_length=30, db_column='y')
    total_address = models.CharField(max_length=100, db_column='total_address')

    class Meta:
        db_table = "address"