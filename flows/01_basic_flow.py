from prefect import task, flow
from prefect.blocks.system import Secret

import psycopg2
import pandas as pd


@task
def extract_data():
    with psycopg2.connect(
            host="aws-0-ap-south-1.pooler.supabase.com",
            database="postgres",
            port="5432",
            user="postgres.evzquwutdsfcxeaeenqm",
            password="DataIntegrationFramework") as conn:
        query = "SELECT * FROM public.bikshare_trips"
        df = pd.read_sql(query, conn)

    print(df)


@flow(name="Basic Flow")
def basic_flow():
    data = extract_data()


if __name__ == "__main__":
    basic_flow()
