import pyodbc
from is_rpi import is_rpi


class SqlComm:
    def __init__(self):
        self.settings = dict(
            database="HOCK",
            server=r"192.168.60.13\inst1",
            port="1433",
            user="VyrobaStandalone",
            password="Kmt0203"

        )
        if is_rpi():
            self.settings["driver"] = 'FreeTDS'
        else:
            self.settings["driver"] = 'SQL Server'

    def get_data_from_db(self, sqlstr):
        try:
            conn = pyodbc.connect(
                f"Driver={self.settings['driver']};"
                f"Server={self.settings['server']};"
                f"Database={self.settings['database']};"
                f"UID={self.settings['user']};"
                f"PWD={self.settings['password']};"
                f"PORT={self.settings['port']}"
            )
        except Exception as e:
            print("Error SQL:")
            print(e)
            return None
        else:
            cursor = conn.cursor()
            cursor.execute(sqlstr)
            newdata = cursor.fetchall()
            cursor.close()
        return newdata


# sql = SqlComm()
# query = "[sp_OPERACE_STROJ] @operace=20, @stroj=11"
# res = sql.get_data_from_db(query)
# print(res)
