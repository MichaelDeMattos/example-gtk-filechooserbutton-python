# -*- coding: utf-8 -*-

import sqlite3


class Model(object):
    def __init__(self, *args):
        self.connection = sqlite3.connect("dotpyc.db")
        self.cursor = self.connection.cursor()
        self.create_schema()

    def create_schema(self):
        sqlquery = ("create table if not exists pyc_file("
                    " cod_pyc_file integer primary key autoincrement,"
                    " description varchar(500) not null,"
                    " name_file varchar(500) not null,"
                    " file blob not null,"
                    " date_create date default current_timestamp)")
        self.cursor.execute(sqlquery)
        self.connection.commit()

    def search_file(self):
        sqlquery = ("select  p.cod_pyc_file,"
                    " p.description,"
                    " p.name_file"
                    " from pyc_file p")
        self.cursor.execute(sqlquery)
        return self.cursor.fetchall()

    def save_file(self, file_bytecode, name, description):
        sqlquery = ("insert into pyc_file"
                    " (file, name_file, description)"
                    " values"
                    " (?,?,?)")
        sqlargs = (sqlite3.Binary(file_bytecode), name, description)
        self.cursor.execute(sqlquery, sqlargs)
        self.connection.commit()

    def delete_file(self, cod_file):
        sqlquery = ("delete from pyc_file"
                    " where cod_pyc_file = ?")
        sqlargs = [cod_file]
        self.cursor.execute(sqlquery, sqlargs)
        self.connection.commit()

    def search_file_id(self, code):
        sqlquery = ("select p.name_file, p.file"
                    " from pyc_file p"
                    " where p.cod_pyc_file = ?")
        sqlargs = [code]
        self.cursor.execute(sqlquery, sqlargs)
        return self.cursor.fetchall()
