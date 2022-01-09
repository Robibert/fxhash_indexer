from datetime import datetime
from enum import  IntEnum

from tortoise import Model, fields
from tortoise.fields.data import SmallIntField


class OfferStatus(IntEnum):
    ACTIVE = 0
    FINISHED = 1
    CANCELED = 2


class MintStatus(Model):
    id= fields.SmallIntField(pk=True)
    pause=fields.BooleanField(default=False)
    enabled=fields.BooleanField(default=True)

    level = fields.BigIntField(default=0)
    timestamp = fields.DatetimeField(default=datetime.utcnow())
    

class Holder(Model):
    address = fields.CharField(36, pk=True)
    name = fields.TextField(default='')
    description = fields.TextField(default='')
    metadata_file = fields.TextField(default='')
    metadata = fields.JSONField(default={})
    hdao_balance = fields.BigIntField(default=0)
    is_split = fields.BooleanField(default=False)
    
    is_moderator = fields.BooleanField(default=False)
    is_banned = fields.BooleanField(default=False)
    is_moderation_admin = fields.BooleanField(default=False)
    is_verified = fields.BooleanField(default=False)
    moderation_state = fields.SmallIntField(default=-1)


class GENTK(Model):
    id = fields.BigIntField(pk=True)
    creator = fields.ForeignKeyField('models.Holder', 'gentks', index=True, null=True)
    title = fields.TextField(default='')
    description = fields.TextField(default='')
    artifact_uri = fields.TextField(default='')
    display_uri = fields.TextField(default='')
    thumbnail_uri = fields.TextField(default='')
    metadata = fields.TextField(default='')
    extra = fields.JSONField(default={})
    mime = fields.TextField(default='')
    royalties = fields.SmallIntField(default=0)
    supply = fields.SmallIntField(default=0)
    is_signed = fields.BooleanField(default=False)
    
    mintable_amount = fields.SmallIntField()
    mint_enabled = fields.BooleanField(default=False)
    mint_price = fields.BigIntField()
    contract_version=fields.SmallIntField()

    level = fields.BigIntField(default=0)
    timestamp = fields.DatetimeField(default=datetime.utcnow())

class LockTime(Model):
    id = fields.BigIntField(pk=True,auto_generate=True)

    value=fields.SmallIntField()
    level = fields.BigIntField(default=0)
    timestamp = fields.DatetimeField(default=datetime.utcnow())



class GENTKHolder(Model):
    holder = fields.ForeignKeyField('models.Holder', 'holders_gentk', null=False, index=True)
    gentk = fields.ForeignKeyField('models.GENTK', 'gentk_holders', null=False, index=True)
    quantity = fields.BigIntField(default=0)




class Offer(Model):
    id = fields.BigIntField(pk=True)
    creator = fields.ForeignKeyField('models.Holder', 'offers', index=True)
    gentk = fields.ForeignKeyField('models.GENTK', 'offers', index=True)
    mint = fields.ForeignKeyField('models.Mint', 'offers', index=True)
    price = fields.BigIntField()
    amount = fields.SmallIntField()
    amount_left = fields.SmallIntField()
    status = fields.IntEnumField(OfferStatus)
    royalties = fields.SmallIntField()
    is_valid = fields.BooleanField(default=True)

    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()


class Trade(Model):
    id = fields.BigIntField(pk=True)
    gentk = fields.ForeignKeyField('models.GENTK', 'trades', index=True)
    offer = fields.ForeignKeyField('models.Offer', 'trades', index=True)
    seller = fields.ForeignKeyField('models.Holder', 'sales', index=True)
    buyer = fields.ForeignKeyField('models.Holder', 'purchases', index=True)
    amount = fields.BigIntField()

    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()


class Mint(Model):
    id = fields.BigIntField(pk=True,auto_generate=True)
    token_id = fields.BigIntField()
    issuer_id = fields.BigIntField()
    gentk = fields.ForeignKeyField('models.GENTK', 'mints', index=True)
    buyer = fields.ForeignKeyField('models.Holder', 'mints', index=True)
    amount = fields.BigIntField()
    iteration = fields.BigIntField()
    ophash = fields.CharField(51)
    level = fields.BigIntField()
    timestamp = fields.DatetimeField()

class Token(Model):
    id = fields.BigIntField(pk=True)
    mint = fields.ForeignKeyField('models.Mint', 'token', index=True)
    buyer = fields.ForeignKeyField('models.Holder', 'tokens', index=True)
    gentk=fields.ForeignKeyField('models.GENTK', 'tokens', index=True)

    amount = fields.BigIntField()

    level = fields.BigIntField()
    timestamp = fields.DatetimeField()



