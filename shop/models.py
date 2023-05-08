from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('user must have email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser,PermissionsMixin):
    """User/Merchant in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Shop(models.Model):
    name = models.CharField(max_length=200)
    merchant = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_img', null=True, blank=True)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class ShopConnector(models.Model):
    STATUS = (
        ('ACCEPT', 'Accept'),
        ('PENDING', 'Pending'),
        ('REJECT', 'Reject'),
    )
    sender = models.ForeignKey(Shop, related_name='sender', on_delete=models.CASCADE)
    receiver = models.ForeignKey(Shop, related_name='receiver', on_delete=models.CASCADE)
    status = models.CharField(max_length=200,choices=STATUS, default='')

    @property
    def connected(self):
        if self.status == 'ACCEPT':
            return True
        return False


 
class Cart(models.Model):
    shop = models.OneToOneField(Shop, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.shop.name


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


