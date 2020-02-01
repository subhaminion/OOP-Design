class Schema():
    def __init__(self, col_name, col_type, col_constraint):
        self.col_name = col_name
        self.type = col_type
        self.constraint = col_constraint
        self.value = None

    def set_value(self, val):
        self.value = val
        return self


class Table():
    def __init__(self, table_name):
        self.table_name = table_name
        self.table_schema = []
        self.table_values = []

    def define_schema(self, schema):
        for i in schema:
           to_append_table_schema = Schema(i.get("col_name"), i.get("col_type"), i.get("col_constraint"))
           self.table_schema.append(to_append_table_schema)

    def insert_values(self, values):
        to_insert_table = self.table_schema
        for val, row in zip(values, to_insert_table):
            self.table_values.append(row.set_value(val.get("col_value")))
        print((self.table_values[3].value))

class Database():
    def __init__(self, database_name):
        self.database_name = database_name
        self.tables = []

    def create_table(self, table_name, table_rows):
        table = Table(table_name)
        table.define_schema(table_rows)
        self.tables.append(table)

    def insert(self, table_name, values):
        # print(values)
        to_insert_table = self.tables[0]
        to_insert_table.insert_values(values)

    def print(self):
        print('----------------------------------------')
        for i in self.tables[0].table_schema:
            print(i.col_name, i.value)
        print('----------------------------------------')


database_obj = Database("employee")
rows = [
    {"col_name":"id", "col_type": "int", "col_constraint": "required"},
    {"col_name":"name", "col_type": "character", "col_constraint": "required"},
    {"col_name":"age", "col_type": "int", "col_constraint": "required"}
]
database_obj.create_table("emp", rows)
values = [
    {"col_name": "id","col_value": "1"},
    {"col_name": "name","col_value": "subham"},
    {"col_name": "age","col_value": "24"},
    {"col_name": "id","col_value": "2"},
    {"col_name": "name","col_value": "heythere"},
    {"col_name": "age","col_value": "29"},
]
database_obj.insert("emp", values)

# database_obj.print()