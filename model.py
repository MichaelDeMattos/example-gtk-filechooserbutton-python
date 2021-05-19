# -*- coding: utf-8 -*-

import os
from peewee import IntegerField, CharField, BlobField, DateTimeField, Model, SqliteDatabase
from datetime import datetime

db = SqliteDatabase(os.curdir+os.path.sep+"data"+os.path.sep+"dotpyc.db")
__all__ = ["ModelPycFile", "Meta"]

class ModelPycFile(Model):
    id = IntegerField(primary_key=True)
    description = CharField(max_length=256, null=False)
    file_name = CharField(max_length=256, null=False)
    file = BlobField(null=False)
    create_date = DateTimeField(default=datetime.now(), null=False)

    class Meta:
        database = db

if __name__ == "__main__":
    """ Create tables if not exists """
    db.create_tables([ModelPycFile])
    