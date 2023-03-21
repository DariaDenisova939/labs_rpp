import csv
import random
import string
import sqlite3
import cherrypy

from peewee import *
from datetime import date

db = SqliteDatabase('FinancialTransfers.db')


class FinancialTransfers(Model):
    number = IntegerField()
    date = DateField()
    time = TimeField()
    transfer_amount = IntegerField()
    transaction_description = CharField()

    class Meta:
        database = db


FinancialTransfers.create_table()


class Table(object):
    @cherrypy.expose
    def index(self):
        html_code = """<html>
          <head><title>Таблица</title></head>
          <body>
          <form method="get" action="add">
              <input type="text" value="number" name="number" />
              <input type="text" value="date" name="date" />
              <input type="text" value="time" name="time" />
              <input type="text" value="transfer_amount" name="transfer_amount" />
              <input type="text" value="transaction_description" name="transaction_description" />
              <button type="submit">add to database</button>
          </form>
          <table align="center">
          <style type="text/css">
          TABLE {
              width: 500px;
              border-collapse: collapse;
          }
          TD, TH {
              padding: 3px;
              border: 1px solid black;
          }
          </style>
          <p align="center">Financial Transfers</p>
          <tr>
          <td align="center">number</td>
          <td align="center">date</td>
          <td align="center">time</td>
          <td align="center">transfer amount</td>
          <td align="center">transaction description</td>
          </tr>"""
        for item in FinancialTransfers.select():
            html_code += """<tr><form method="get" action="changes">
              <td><input type="text" value=" """ + str(item.number) + """"name="number" /></td>
              <td><input type="text" value=" """ + str(item.date) + """"name="date" /></td>
              <td><input type="text" value=" """ + str(item.time) + """"name="time" /></td>
              <td><input type="text" value=" """ + str(item.transfer_amount) + """"name="transfer_amount" /></td>
              <td><input type="text" value=" """ + str(item.transaction_description) + """"name="transaction_description" /></td>
              <td><input type="hidden" value=" """ + str(item.id) + """"name="id" /></td>
              <td><button type="submit">change</button></td></tr>
          </form>"""
        html_code += """</table>
        </body>
        </html>"""

        return html_code

    @cherrypy.expose
    def add(self, number="number", date="date", time="time", transfer_amount="transfer_amount",
            transaction_description="transaction_description"):
        flag = True
        for item in FinancialTransfers.select():
            if item.number == int(number):
                flag = False
                break
        if flag:
            FinancialTransfers(number=int(number), date=str(date), time=str(time), transfer_amount=int(transfer_amount),
                               transaction_description=str(transaction_description)).save()
        return Table.index(self)

    @cherrypy.expose
    def changes(self, number="number", date="date", time="time", transfer_amount="transfer_amount",
                transaction_description="transaction_description", id="id"):
        FinancialTransfers(number=int(number), date=str(date), time=str(time), transfer_amount=int(transfer_amount),
                           transaction_description=str(transaction_description)).update(number=number)
        for item in FinancialTransfers.select():
            if item.id == int(id):
                item.number = int(number)
                item.date = date.replace(' ', '')
                item.time = time.replace(' ', '')
                item.transfer_amount = int(transfer_amount)
                item.transaction_description = transaction_description.strip()
                item.save()
                break
        return Table.index(self)


if __name__ == '__main__':
    cherrypy.quickstart(Table())
