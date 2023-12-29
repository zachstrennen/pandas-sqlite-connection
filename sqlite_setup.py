import sqlite3
import pandas as pd


def build_db(path: str):
    """
    Read in the dataset from a selected directory.
    Adjust dataframe to specific format.
    Convert dataframe to simple relational sql model.
    :param path: String containing the path name.
    :return: pandas dataframes of sql tables.
    """

    # Establishes first table with primary key and company name
    company_name_query = '''
    CREATE TABLE IF NOT EXISTS company_info (
        id INTEGER PRIMARY KEY,
        company_name VARCHAR(250) NOT NULL
    );

    '''

    # Second table with all related company info
    company_info_query = '''
    CREATE TABLE IF NOT EXISTS scam_info (
        year INT,
        crypto_nft VARCHAR(250) NOT NULL,
        rugpull_scam VARCHAR(250) NOT NULL,
        amount_stolen INT,
        company_id INT REFERENCES company(id)
    );

    '''

    # Establish sqlite connection
    conn = sqlite3.connect('.../live_test_sqlite.db')
    cursor = conn.cursor()

    # Execute CREATE sql scripts
    cursor.execute(company_name_query)
    cursor.execute(company_info_query)

    # Read in the dataframe
    df = pd.read_csv(path)

    # Convert the dollar amount to a float
    df["Amount Stolen"] = df["Amount Stolen"].replace(',', '', regex=True)
    df["Amount Stolen"] = df["Amount Stolen"].astype(float)

    # Convert data to only include the year
    df['Date'] = pd.to_datetime(df['Date'], format='%b, %Y')
    df['Date'] = pd.DatetimeIndex(df['Date']).year

    # Separate the columns into their respective dataframes to be pushed to the created sql
    df_company = df[['Company Name']]
    df_info = df[['Date', 'Crypto vs NFT', 'Rug Pull vs Scam', 'Amount Stolen']]

    # Push the dataframes to SQL tables
    df_company.to_sql('company_info', conn, if_exists='replace', index=False)
    conn.commit()
    df_info.to_sql('scam_info', conn, if_exists='replace', index=False)
    conn.commit()
    cursor.close()

    # Return the SQL tables as pandas dataframes
    r_df1 = pd.read_sql("select * from company_info", conn)
    r_df2 = pd.read_sql("select * from scam_info", conn)
    return r_df1, r_df2


if __name__ == '__main__':
    # Call function to create SQL tables
    df1, df2 = build_db('data/NFT Rug Pulls.csv')
