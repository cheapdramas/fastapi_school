import psycopg
from db.pg.connect import async_connect,connect




functions =[

]

index_queries = [

]

triggers =[

]




async def connect_():
    async with await async_connect() as conn:
        return conn
    
async def get_db_version():
    async with await async_connect() as conn:
        cursor = conn.cursor()
        await cursor.execute('SELECT VERSION()')
        return await cursor.fetchone()
    


def create_table_schools_query() -> str:
    query = """
        CREATE TABLE IF NOT EXISTS schools (
            id INTEGER PRIMARY KEY NOT NULL UNIQUE CHECK (id<10000),
            full_name VARCHAR UNIQUE,
            short_name VARCHAR,
            email VARCHAR UNIQUE,
            director VARCHAR UNIQUE,
            town VARCHAR
        )
        """
    
    index_queries.append("""
    CREATE INDEX IF NOT EXISTS idx_name ON schools(full_name,short_name)
    """
    )
    index_queries.append(
    """
    CREATE INDEX IF NOT EXISTS idx_director ON schools(director)
    """
    )

    function_autoincrement = """
        CREATE OR REPLACE FUNCTION autoincrement_id() RETURNS integer AS $$
           SELECT MAX(schools.id) +1 FROM schools;
        $$ LANGUAGE SQL;
    """
    functions.append(function_autoincrement)

    return query



def create_table_classes_query() ->str:
    query = """
        CREATE TABLE IF NOT EXISTS classes(
            id INTEGER PRIMARY KEY NOT NULL UNIQUE,
            name VARCHAR(5) NOT NULL,
            school_id INTEGER NOT NULL,
           
            FOREIGN KEY(school_id) REFERENCES schools(id) ON DELETE CASCADE

            
            
        )

    """

    index_queries.append(
        "CREATE INDEX IF NOT EXISTS idx_class_name ON classes(name)"
    )
    index_queries.append(
         "CREATE INDEX IF NOT EXISTS idx_class_school_id  ON classes(school_id)"
    )
     #function for before insert trigger,which not allows to insert 2 same class names in one school 
    before_insert_function = """  
        CREATE OR REPLACE FUNCTION trigger_before_insert()
            RETURNS TRIGGER
            LANGUAGE PLPGSQL
        AS
        $$
       
        BEGIN
            
            
         
            IF (SELECT COUNT(*) FROM classes WHERE school_id = new.school_id AND name=NEW.name) >= 1 THEN
                RAISE EXCEPTION 'This class already exists in this school' USING ERRCODE = 'unique_violation';
                ROLLBACK;
            
            END IF;
            RETURN NEW;

        END;
        $$;
    """

    functions.append(before_insert_function)


    trigger_before_insert =""" 
        CREATE TRIGGER classes_before_insert
        BEFORE INSERT
        on classes
        FOR EACH ROW
        EXECUTE FUNCTION trigger_before_insert();

    """
    triggers.append(trigger_before_insert)

   
    return query



def create_table_teachers_query()->str:
    query = """
        CREATE TABLE IF NOT EXISTS teachers(
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            first_name VARCHAR(20) NOT NULL,
            second_name VARCHAR(30) NOT NULL,
            lesson VARCHAR(30) NOT NULL,
            class_id INTEGER UNIQUE,
            FOREIGN KEY(class_id) REFERENCES classes(id)
        )
        """

    index=   "CREATE INDEX IF NOT EXISTS class_id ON teachers(class_id)"
    index_queries.append(index)
    
    return query    


def create_table_students_query() -> str:
    query = """
        CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY UNIQUE NOT NULL,
            first_name VARCHAR(20) NOT NULL,
            second_name VARCHAR(30) NOT NULL,
            birthday DATE NOT NULL,
            class_id INTEGER NOT NULL,

            FOREIGN KEY(class_id) REFERENCES classes(id)
        )
    """
    
    index_queries.append('CREATE INDEX IF NOT EXISTS idx_name ON students(first_name,second_name)')


    function_before_insert = """
        CREATE OR REPLACE FUNCTION students_before_insert()
            RETURNS TRIGGER
            LANGUAGE PLPGSQL
        AS 
        $$
        BEGIN

            IF (SELECT COUNT(*) FROM students WHERE class_id = NEW.class_id) >=34 THEN
                RAISE EXCEPTION 'One class support`s to 34 student';
                ROLLBACK;

            

            END IF;
            RETURN NEW;



        END;
        $$;

    """

    functions.append(function_before_insert)



    trigger_before_insert = """
        CREATE TRIGGER before_insert_students
        BEFORE INSERT
        ON students
        FOR EACH ROW
        EXECUTE FUNCTION students_before_insert();
    """

    triggers.append(trigger_before_insert)
    

    return query




def create_tables():
    with connect() as conn:
        
        cursor = conn.cursor()
        #queries for table creation
        table_queries = [
            create_table_schools_query(),
            create_table_classes_query(),
            create_table_teachers_query(),
            create_table_students_query()
        ]
    
        #queries for functions creation
        
        
        #commiting our functions because we will use them as default pk value in schools table
        
        
        #executing tables
        for table_query in table_queries:
            cursor.execute(table_query)
    
        

       
       
        #creating indexes
        for index_q in index_queries:
            cursor.execute(index_q)
        
        for function in functions:
            cursor.execute(function)

        for trigger in triggers:
            cursor.execute(trigger)
        



        #global commit
        conn.commit()

def drop_tables():

    def drop(table_names:list):
        with connect() as conn:
            for name in table_names:
                conn.execute(f'DROP TABLE IF EXISTS {name} CASCADE')
            conn.commit()

            
    drop([
        'schools',
        'classes',
        'teachers',
        'students'
          
    ])


