class NeedleWunsch:
    def __init__(self, str1=None, str2=None):
        from termcolor import colored
        if str1 is not None and str2 is not None:
            self.str1, self.str2 = str1, str2
            print(colored("NeedlemanWunsch (NW) object will be initialized with given texts.", "yellow"))
            self.initTable()
            print(colored("NeedlemanWunsch (NW) object is initialized with given texts.", "yellow"))
        else:
            self.str1 = self.str2 = self.table = None
            print( colored("NeedlemanWunsch (NW) object is empty initialized. Strings need to be provided \
                with \"setStrings\" method before object will be used.", "yellow"))
    
    def setStrings(self, str1, str2):
        from termcolor import colored
        self.str1 = str1
        self.str2 = str2
        self.initTable()
        print(colored("NeedlemanWunsch (NW) table is initialized with given texts.", "yellow"))

    def initTable(self):
        import numpy as np
        try:
            row_str = self.str1
            col_str = self.str2
            if not isinstance(row_str, str) or not isinstance(col_str, str):
                raise ValueError("Matrix can be initialized with only 2 provided strings!")
            
            row_length = len(row_str) + 1
            col_length = len(col_str) + 1
            self.table = np.zeros(shape=(row_length, col_length), dtype=int)

        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(e)
    
    def printTable(self):
        import numpy as np
        table_header = np.array(list(" " + self.str2), dtype=object).reshape((1,self.table.shape[1]))
        print(table_header.shape, table_header.dtype)
        table = self.table.astype(object)
        concatenated = np.concatenate( (table_header,table) )
        table_left_header = np.array(list("  " + self.str1), dtype=object).reshape((concatenated.shape[0],1))
        print(table_left_header.shape)
        print(concatenated.shape)
        concatenated = np.concatenate( (table_left_header,concatenated), axis=1 )
        print(concatenated)