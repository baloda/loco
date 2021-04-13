from django.db import models

TYPE_CHOICES = (
    ((), ())
)


class Base(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    updated_at = models.DateTimeField(auto_now=True, blank=False)

    class Meta:
        abstract = True

class Transactions(Base):
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    hierarchy = models.CharField(blank=True,null=True, max_length=1024)
    amount = models.FloatField(null=True)
    type = models.CharField(max_length=128)

    class Meta:
        db_table="transactions"
        managed = True

    def __str__(self):
        return "id: {}   amount: {}  type: {} parent_id: {}".format(
            self.id, self.amount, self.type,
            (self.parent.id if self.parent else None),
        )