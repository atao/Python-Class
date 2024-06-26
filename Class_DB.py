class database:
    def __init__(self, database):
        self.database = database

    def prepare_database(self, table, columns):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            # Dynamically create the column definitions
            columns_definitions = ', '.join([f'"{col}" {dtype}' for col, dtype in columns.items()])
            # Create the SQL query string
            query = f'CREATE TABLE IF NOT EXISTS "{table}" ({columns_definitions})'
            # Execute the query
            cursor.execute(query)
            conn.commit()
            print("[+] {} successfully created!".format(self.database))
        except sqlite3.IntegrityError:
            print("[!] Already exists")
        except Exception as e:
            print(f"[!] Error: {e}")
            conn.rollback()
            raise e
        finally:
            conn.close()

    def store_data(self, table, data):
        try:
            conn = sqlite3.connect(self.database)
            cursor = conn.cursor()
            # Dynamically create the column names and placeholders
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['?'] * len(data))
            # Create the SQL query string
            query = f'INSERT OR IGNORE INTO {table} ({columns}) VALUES ({placeholders})'
            # Execute the query with the appropriate values
            cursor.execute(query, tuple(data.values()))
            id = cursor.lastrowid
            conn.commit()
        except sqlite3.IntegrityError:
            print("[!] Already exist")
        except Exception as e:
            print(f"[!] Error {e}")
            conn.rollback()
            raise e
        finally:
            print(f"[+] Last id {id} - {data}")
            conn.close()
