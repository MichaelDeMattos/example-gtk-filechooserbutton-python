# -*- coding: utf-8 -*-

from peewee import Table
from model import db, ModelPycFile

__all__ = ["ControllerModelPycFile"]

class ControllerModelPycFile(object):
    def __init__(self, *args):
        ...

    def search_file(self):
        tb_pyc_file = Table("ModelPycFile")
        query = (
            tb_pyc_file.select(
                tb_pyc_file.c.id, 
                tb_pyc_file.c.description,
                tb_pyc_file.c.file_name
            )
        )

        list_store = []
        [list_store.append(row.values()) for row in query.execute(db)]
        return list_store
    
    def save_file(self, file_bytecode, name, description):
        query = ModelPycFile(
            file=file_bytecode, file_name=name, description=description
        )
        query.save()

    def delete_file(self, cod_file):
        query = ModelPycFile.delete().where(
            ModelPycFile.id == cod_file
        )
        query.execute(db)
    
    def search_file_id(self, code):
        tb_pyc_file = Table("ModelPycFile")
        query = (
            tb_pyc_file.select( 
                tb_pyc_file.c.file_name,
                tb_pyc_file.c.file
            ).where(tb_pyc_file.c.id == code)
        )

        return query.execute(db)[0]
