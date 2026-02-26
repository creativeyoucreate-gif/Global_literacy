import streamlit as st
import pandas as pd
import mysql.connector
def run():

    # ---- Database Connection ----
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="KAvi",
        database=""
    )

    cursor = conn.cursor()