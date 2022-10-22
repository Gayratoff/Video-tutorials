import sqlite3

class Database:
    def __init__(self,path_to_db="main.db"):
        self.path_to_db= path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self,sql: str,parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters=()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data=None
        cursor.execute(sql,parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql ="""
        CREATE TABLE myfiles_teacher (
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            email varchar(255),
            laguage varchar(3),
            PRIMARY KEY (id)
            );
"""

    @staticmethod
    def format_args(sql, parameters:dict):
        sql += " AND ".join([
            f"{item}=?"for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, name: str,email: str=None, laguage: str="uz"):
          # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO myfiles_teacher (id, name, email, laguage) VALUES(?,?,?,?)
        """
        self.execute(sql, parameters=(id, name, email, laguage), commit=True)

    def select_all_users(self):
        sql="""
        SELECT * FROM myfiles_teacher
        """
        return self.execute(sql, fetchall=True)

    def select_user(self,**kwargs):
        # SQL_EXAMPLE = "SELECT * FROM myfiles_teacher where id=1 AND Name='John'"

        sql = "SELEFT * FROM myfiles_teacher WHERE"
        sql , parameters = self.format_args(sql,kwargs)
        return self.execute(sql, parameters=parameters,fetchone=True)

    def count_users(self):
        return self.execute("SELECT COUNT(*)FROM myfiles_teacher;",fetchone=True)

    def delete_user(self):
        self.execute("DELETE FROM myfiles_teacher WHERE TRUE",commit=True)

# -------------------- O'zim ishlaganim-------------------------------

    def user_qoshish(self,  ism: str, tg_id:int,  fam: str = None,):
        # SQL_EXAMPLE ="INSERT INTO myfiles_teacher(id,name,email)VALUES(1,"john","john@hgmail.com")"

        sql="""
        INSERT INTO users ( ism,fam, tg_id) VALUES(?,?,?)
        """
        self.execute(sql, parameters=( ism, fam,  tg_id), commit=True)

    def select_all_foidalanuvchilar(self):
        sql="""
        SELECT * FROM users
        """
        return self.execute(sql, fetchall=True)


def logger(statement):
    print(f"""
    --------------------------------------------------------
    Executing:
    {statement}
    --------------------------------------------------------
""")

