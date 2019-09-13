class ClosePGConnection:

    def __init__(self):
        ''' Initialise constructor for pg closure. '''
        print("Connection termination initiated")

    def close_pg(self,conn):
        conn.close()
        print("Connection closed Successfully")
        return True;