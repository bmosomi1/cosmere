from django.db import models


class MiwamaMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Miwama Mpesa"
        verbose_name_plural = "Miwama Mpesa"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reference} - {self.amount}"


class RealBoutiqueMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)
    is_processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Real Boutique M-pesa Record"
        verbose_name_plural = "Real Boutique M-pesa Records"

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.reference} - {self.amount}"


class PerezuMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)


class NopeMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)


class CleanShift(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)


class GreenNoteMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)


class OlemaxMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)


class AquaNovaMpesa(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = models.CharField(max_length=250)
    amount = models.CharField(max_length=250)
    reference = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    type = models.CharField(max_length=250)
    account_number = models.IntegerField(null=True)
    till_number = models.IntegerField(null=True)
    processed = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)
    organization_balance = models.CharField(max_length=250, null=True)