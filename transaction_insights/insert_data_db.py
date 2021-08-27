"""Script to insert monthly expense data per category to the database"""
import os
import sys

sys.path.insert(0, "..")
from process_data import ProcessData
import sqlite3

os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "transaction_insights.settings")

from expense_data.models import ExpenseData

process_data_object = ProcessData()


def store_data_to_db():
    monthly_expenses_per_category = process_data_object.monthly_expenses_per_category()
    conn = sqlite3.connect("db.sqlite3")
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS ExpenseData""")
    monthly_expenses_per_category.to_sql(
        "ExpenseData", conn, if_exists="replace", index=False
    )
    conn.commit()
    conn.close()
