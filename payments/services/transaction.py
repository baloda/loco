from django.db.models import Sum
from payments.models import Transactions
class TransactionService:


    @classmethod
    def get_all(cls):
        records = Transactions.objects.all()
        return records

    @classmethod
    def get(cls, id):
        record = Transactions.objects.get(id=id)
        return record


    @classmethod
    def get_by_id(cls, id):
        return Transactions.objects.get(id=id)


    @classmethod
    def get_by_types(cls, category):
        ids_query_set = Transactions.objects.filter(type=category).values_list("id")
        return list(sum(tuple(ids_query_set), ()))


    @classmethod
    def get_hierarchical_amount_sums(cls, id):
        record: Transactions = cls.get_by_id(id=id)

        amount__sum = Transactions.objects.filter(
            hierarchy__icontains=cls.join_hierarchy(record.hierarchy, id)
        ).aggregate(Sum("amount"))

        hierarchical_amount_sums = record.amount + amount__sum.get("amount__sum") or 0
        return hierarchical_amount_sums

    @classmethod
    def create(cls, data):
        amount, _type, parent_id = [
            data.get(k) for k in ["amount", "type", "parent_id"]
        ]
        if parent_id:
            hierarchy = cls.create_hierarchy(parent_id)

        record = Transactions(
            amount=amount,
            type=_type,
            parent_id=parent_id,
            hierarchy=hierarchy
        )
        record.save()
        return record

    @classmethod
    def update(cls, id, data):
        record: Transactions = cls.get(id=id)
        record.amount = data.get("amount") or record.amount
        record.type = data.get("type") or record.type
        record.parent_id = data.get("parent_id") or record.parent_id

        if record.parent_id:
            record.hierarchy = cls.create_hierarchy(record.parent_id)
        record.save()
        return record

    @classmethod
    def create_hierarchy(cls, parent_id=None):
        if parent_id is None:
            return None
        parent: Transactions = cls.get_by_id(id=parent_id)
        return cls.join_hierarchy(parent.hierarchy, parent_id)

    @classmethod
    def join_hierarchy(cls, hierarchy, parent_id):
        return (hierarchy or "").rstrip("/") + ("/%s/" % parent_id)

