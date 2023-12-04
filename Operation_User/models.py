from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, AbstractUser
from django.utils import timezone


# Create your models here.

# File Taken by FileExtensionValidator
# common_file_extensions = [
#     'txt', 'pdf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'zip', 'tar', 'gz',
#     'jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'mp3', 'wav', 'mp4', 'avi', 'mov',
# ]

class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    File = models.FileField(upload_to='OpsU/', validators=[FileExtensionValidator(['docx','pptx','xlsx'])])

    def file_name_substring(self):
        return str(self.File)[5:] if self.File else ''
    
    def __str__(self):
        return self.id



class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_superuser, is_verified, is_Client, is_Operational_user):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email, 
        is_active=True,
        is_Client = is_Client,
        is_Operational_user= is_Operational_user,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        is_verified=is_verified
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password):
    return self._create_user(email, password, False, False, True, False)

  def create_superuser(self, email, password):
    user=self._create_user(email, password, True, True, False, True)
    return user


class USER(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    is_Client = models.BooleanField('Client User', default=True)
    is_Operational_user = models.BooleanField('Operational User', default=False)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)
    

    class Meta:
        default_related_name = 'custom_%(class)s_permissions'
        permissions = [
            ("view_special_content", "Can view special content"),
        ]

    class Meta(AbstractUser.Meta):
        default_related_name = 'custom_%(class)s_groups'

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


