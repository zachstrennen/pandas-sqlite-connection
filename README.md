#Connecting pandas to a sql database with sqlite
The code in this repository is a template to use when converting a pandas data frame into an SQL database (and vice versa). The data frame used contains information on crypto/NFT scams and rugpulls. The relational model being built is simple. A primary key is generated for each company and that key is then used to link the company names to another table with affiliated information. This code requires the packages sqlite3 and pandas.

Note that this code is very loose and speciic and should not serve as an ultimate template. The idea is to see how a connection is setup. I have a more useful example with psycopg2 on my GitHub. Please view the repository Hospitals_Data_Pipeline.
