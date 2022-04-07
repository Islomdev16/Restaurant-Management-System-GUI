import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        sql = """
        CREATE TABLE IF NOT EXISTS employees(
            id Integer Primary Key,
            name text,
            surname text,
            age text,
            role text,
            joined_date text,
            email text,
            gender text,
            country text,
            phone_number text,
            address text
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function Section
    def insert(self, name, surname, age, role, joined_date, email, gender, country, phone_number, address):
        self.cur.execute("insert into employees values (NULL,?,?,?,?,?,?,?,?,?,?)", (name, surname, age, role, joined_date, email, gender, country, phone_number, address))
        self.con.commit()

    # Fetch All Data from DB Section
    def fetch(self):
        self.cur.execute("SELECT * from employees")
        rows = self.cur.fetchall()
        # print(rows)
        return rows

    # Delete a Record in DB Section
    def remove(self, id):
        self.cur.execute("delete from employees where id=?", (id,))
        self.con.commit()

    def update(self, id, name, surname, age, role, joined_date, email, gender, country, phone_number, address):
        self.cur.execute("update employees set name=?, surname=?, age=?, role=?, joined_date=?, email=?, gender=?, phone_number=?, address=? where id=?",
                         (name, surname, age, role, joined_date, email, gender, country, phone_number, address, id))
        self.con.commit()

table = Database("Employee.db")
table.insert("Jack", "Kinsma", "18", "Manual Engineer", "04-16-2004", "test112@gmail.com", "Male", "Uzbekistan", "+998912200123", "Test Address 1")
table.fetch()
# table.remove("2")
# table.update("1", "Test Updated", "Testerov Up", "20", "Backend Developer", "11-11-2011", "testupdated12@gmail.com", "Female", "+998902334445", "Test Updated Address")
