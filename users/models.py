from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
import uuid as uuid_lib

# Create your models here.
class User(AbstractUser):

    # replace id with uuid
    id = models.UUIDField(default=uuid_lib.uuid4,
                            primary_key=True, editable=False)