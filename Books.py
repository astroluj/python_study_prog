#-*- conding: utf-8 -*-


# DB Class
class Sqlite3_admin:

    def __init__(self, name):
        # DB db conn
        self.__conn = None
        self.__name = name

        self.__create_table__()

    # Create Table
    def __create_table__(self):
        cursor = self.__db_connect__()
        # table names
        if self.__conn:
            cursor.execute(
                           '''
                           CREATE TABLE IF NOT EXISTS {0} (
                           id UNSIGNED INT AUTO_INCREMENT NOT NULL,
                           name VARCHAR (100) NOT NULL,
                           author VARCHAR (100) NOT NULL,
                           price UNSIGNED INT NOT NULL,
                           PRIMARI KEY (id),
                           UNIQUE (name, author, price)) 
                           '''.format(name))
            try:         
                self.__conn.commit()
            except Exception as e:
                return e
            finally:
                cursor = self.__db_close__()
        
    # DB Select
    def db_select_all(self, table, selections, whereData):
        cursor = self.__db_connect__()
        if self.__conn:
            cursor.execute('Select {0} from {1} {2}'.format(selections,
                                                            table,
                                                            whereData))
            return cursor.fetchall()
        else:
            print('Sqlite3 not connect')
        self.__db_close__()
        
            
    # DB Insert
    def db_insert(self, table, wantData, valueData):
        cursor = self.__db_connect__()
        if self.__conn:
            cursor.execute('INSERT INTO {0} {1} VALUES ({2})'.format(table,
                                                                     wantData,
                                                                     valueData))
            try:
                self.__conn.commit()
            except Exception as e:
                return e
            finally:
                self.__db_close__()
        
    # DB Delete
    def db_delete(self, table, whereData):
        cursor = self.__db_connect__()
        if self.__conn:
            cursor.execute('DELETE FROM {0} {1}'.format(table,
                                                        whereData))
            try:
                self.__conn.commit()
            except Exception as e:
                return False
            finally:
                self.__db_close__()
        
    # DB Update
    def db_update(self, table, updateData, whereData):
        cursor = self.__db_connect__()
        if self.__conn:
            cursor.execute('UPDATE {0} SET {1} {2}'.format(table,
                                                           updateData,
                                                           whereData))
            try:
                self.__conn.commit()
            except Exception as e:
                return False
            finally:
                self.__db_close__()   
            
    # DB connection and close private functions
    def __db_connect__(self):
        # connect and create db
        if self.__name:
            try:
                self.__conn = sqlite3.connect(self.__name)

                return self.__conn.cursor()
            except Exception as e:
                print('DB connection Error : {0}'.format(e))
        else:
            print('Name is empty')

    def __db_close__(self):
        try:
            self.__conn.close()
        except Exception as e:
            print('DB Close Error : {0}'.format(e))


# 도서관리 클래스
class Book(Sqlite3_admin):
    def __init__(self):
        self.__name = None
        self.__author = None
        self.__price = 0

        # Create DB
        db = Sqlite3_admin()
    def __make_where__(author, name, price):
        return 'WHERE author {0}{1} and name {2}{3} and price {4} {5}'.\
                   format(('=', author if author
                           else '!=', 'NULL'),
                          ('=', name if name
                           else '!=', 'NULL'),
                          ('=', price if price
                           else '!=', 'NULL'))

    
    # Parameters is list
    def insert_info(self, table, name, author, price):
        if name and author and price:
            # Authors, Names, Prices Insert
            return db.db_insert(table = table,
                                wantData = 'author, name, price',
                                valueData = '{0}, {1}, {2}'.format(author,
                                                                   name,
                                                                   price))
        else:
            print('Bad Request')

    def delete_info(self, table, name = None, author = None, price = None):
        return db.db_delete(table = table,
                            whereData = __make_where__(author,
                                                       name,
                                                       price))

    def update_info(self, table, name = None, author = None, price = None):
        return db.db_update(table = table,
                            updateData = '{0}{1} {2} {3}{4} {5} {6}{7}'.\
                                             format(('author=', author if author
                                                     else '', ''),
                                                    (',' if author and name
                                                     else ''),
                                                    ('name=', name if name
                                                     else '', ''),
                                                    (',' if name and pice
                                                     else ''),
                                                    ('price=', price if price
                                                     else '', '')),
                            whereData = __make_where__(author,
                                                       name,
                                                       price))
    def search_info(self, table, name = None, author = None, price = None):
        return db.db_select(table = table,
                            selections = '*',
                            whereData = __make_where__(author,
                                                       name,
                                                       price))

    def printAllInfo(self):
        return db.db_select(table = table,
                            selections = '*')

    

    
