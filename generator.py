
from db import cur
from file import write_file
from os import linesep
from os import sep

def set_type(type_column:str)->str:
    match type_column:
        case 'date':
            return 'date'
        case 'smallint':
            return 'int'
        case 'timestamp without time zone':
            return 'dt'
        case 'boolean':
            return 'bool'
        case 'character varying':
            return 'str'
        case 'text':
            return 'str'
        case 'integer':
            return 'int'
        case 'bigint':
            return 'int'

def set_class(table_name:str)->str:
    return f"""class {table_name.replace("_","").title()}(SQLModel, table=True): # type: ignore"""

def set_imports(schema_name, table_name)->list:
    import_list = list()

    import_list.append("from typing import Optional")
    import_list.append("from sqlmodel import Field, SQLModel")

    list_types= list()


    sql=f"""Select
                information_schema.columns.data_type
            From
                information_schema.columns
            Where
                information_schema.columns.table_schema = '{schema_name}' And
                information_schema.columns.table_name = '{table_name}'
            Group By
                information_schema.columns.data_type"""
    cur.execute(sql)
    types = cur.fetchall()

    for t in types:
        list_types.append(set_type(t[0]))
    
    list_types = list(dict.fromkeys(list_types))
    
    for t in list_types:
        match t:
            case "datetime":
                import_list.append("from datetime import datetime as dt")
            case "date":
                import_list.append("from datetime import date")
    
    return import_list
    


def is_constraint(column_name:str, table_name:str, schema_name:str, type_constraint:str)->str:
    retorno = ""
    cur.execute(f"""Select
                        ccu.table_schema As foreign_table_schema,
                        ccu.table_name As foreign_table_name,
                        ccu.column_name As foreign_column_name,
                        tc.constraint_type
                    From
                        information_schema.table_constraints As tc Inner Join
                        information_schema.key_column_usage As kcu On tc.constraint_name = kcu.constraint_name And
                        tc.table_schema = kcu.table_schema Inner Join
                        information_schema.constraint_column_usage As ccu On ccu.constraint_name = tc.constraint_name
                    Where
                        tc.constraint_type = '{type_constraint}' And
                        tc.table_schema = '{schema_name}' And
                        tc.table_name = '{table_name}' And
                        kcu.column_name = '{column_name}'""")
    constraints = cur.fetchall()
    if len(constraints)> 0:
        c = constraints[0]
        retorno = c[1] + "." + c[2]
    
    
    return retorno

def generate_columns(schema_name:str, table_name:str)->list:
    retorno = list()
     
    sql_columns=f"""SELECT 
                            information_schema.columns.column_name,
                            information_schema.columns.is_nullable,
                            information_schema.columns.data_type
                            FROM information_schema.columns
                        WHERE
                            table_schema = '{schema_name}'
                        AND 
                            table_name   = '{table_name}'
                        Order By
                            information_schema.columns.ordinal_position"""
    
    cur.execute(sql_columns)
    columns = cur.fetchall()

    for c in columns:
        column_name = c[0]
        nullable = True if c[1] == 'YES' else False
        data_type = c[2]
        fk = is_constraint(column_name=column_name,table_name=table_name, schema_name=schema_name, type_constraint="FOREIGN KEY")
        pk = is_constraint(column_name=column_name,table_name=table_name, schema_name=schema_name, type_constraint="PRIMARY KEY")
        variable_name = "\t" + column_name + ':'
        variable_name = variable_name + f"""Optional[{set_type(data_type)}]""" if nullable else variable_name + set_type(data_type)
        
        constraint=""
        if pk!="" or fk!="":
            if pk!="" and fk!="":
                constraint = f"""= Field(default=None, primary_key=True, foreign_key="{fk}")"""
            elif pk!="":
                constraint = f"""= Field(default=None, primary_key=True)"""
            else:
                constraint = f"""= Field(default=None, foreign_key="{fk}")"""

        retorno.append(variable_name + constraint)

    return retorno

def generate_model(schema_name:str, table_name:str, directory:str):
        model_list = list()
        imports = set_imports(schema_name=schema_name, table_name=table_name)
        class_name = set_class(table_name=table_name)
        columns = generate_columns(schema_name=schema_name,table_name=table_name)
        model_list.extend(imports)
        model_list.append(linesep)
        model_list.append(class_name)
        model_list.extend(columns)
        text = linesep.join(model_list)
        write_file(file=directory+sep+table_name+".py", data=text)




def generate_models_from_schema(schema_name:str, directory:str):
    sql_tables = f"""Select
                    information_schema.tables.table_name
                From
                    information_schema.tables
                Where
                    information_schema.tables.table_schema = '{schema_name}' And
                    information_schema.tables.table_type = 'BASE TABLE'"""
    cur.execute(sql_tables)
    tables = cur.fetchall()

    for t in tables:
        table = t[0]
        generate_model(schema_name=schema_name, table_name=table, directory=directory)

generate_models_from_schema('public', '/home/zetempesta/sqlmodelgenerator/models')

