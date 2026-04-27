from django.db import models
import uuid
from django.contrib.auth import get_user_model
from user.models import Address

UserModel = get_user_model()

class Extensions(models.Model):
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Order(Extensions):
    PENDING_STATE = "p"
    COMPLETED_STATE = "c"

    ORDER_CHOICES = ((PENDING_STATE, "pending"), (COMPLETED_STATE, "completed"))

    uuid = models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    # cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    order_number = models.CharField(max_length=250, blank=True, null=True)
    status = models.CharField(max_length=1, choices=ORDER_CHOICES, default=PENDING_STATE)
    is_paid = models.BooleanField(default=False)
    address = models.ForeignKey(Address, related_name="order_address", on_delete=models.CASCADE)

    def __str__(self):
        return self.cart.user.username
