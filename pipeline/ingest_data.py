import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path
from tqdm.auto import tqdm
import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL username')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default='5432', help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--chunksize', default=100000, type=int, help='Chunk size for ingestion')
@click.option('--table-name', default='yellow_taxi_data', help='Target table name')
@click.option('--file-name', default='file_name', help='CSV or Parquet file')


def run(pg_user, pg_pass, pg_host, pg_port, pg_db, chunksize, table_name, file_name):


    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    file_path = Path(file_name)

    if not file_path.exists():
        print(f"File {file_name} doesn't exist.")
        return
    
    if file_path.suffix.lower() == '.csv':
        df_iter = pd.read_csv(
            file_path,
            iterator=True,
            chunksize=chunksize
            )
        
        first = True

        for df_chunk in tqdm(df_iter):

            if  first:

                df_chunk.head(0).to_sql(
                    name=table_name,
                    con=engine,
                    if_exists="replace",
                    index=False
                )
                first = False
                print("Table created")

            df_chunk.to_sql(
                name=table_name,
                con=engine,
                if_exists="append",
                index=False
            )
            print("Inserted:", len(df_chunk))

    elif file_path.suffix.lower() == '.parquet':
        df = pd.read_parquet(file_path)
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace"
        )
        print("Table created and populated")
    else:
        print("Invalid file type.")
        return



if __name__ == '__main__':
    run()