class NeedleWunsch:
    def __init__(self, str1=None, str2=None, miss_point=None):
        from termcolor import colored
        if type(miss_point) == int:
            print(colored("SmithWaterman (SW) object will be initialized.", "yellow"))
            self.miss = miss_point
        else:
            print(colored("NeedlemanWunsch (NW) object will be initialized.", "yellow"))
            self.miss = -1

        if str1 is not None and str2 is not None:
            self.str1, self.str2 = str1, str2
            print(colored("(SW or NW) object will be initialized with given texts.", "yellow"))
            self.initTable()
            print(colored("(SW or NW) object is initialized with given texts.", "yellow"))
        else:
            self.str1 = self.str2 = self.table = None
            print( colored("(SW or NW) object is empty initialized. Strings need to be provided \
                with \"setStrings\" method before object will be used.", "yellow"))
    
    def __str__(self):
        import numpy as np
        return np.array2string(self.getPrintableTable(), formatter={"object": lambda x: str(x) + "\t"})

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
    
    def getPrintableTable(self):
        import numpy as np
        table_header = np.array(list(" " + self.str2), dtype=object).reshape((1,self.table.shape[1]))
        table = self.table.astype(object)
        concatenated = np.concatenate( (table_header,table) )
        table_left_header = np.array(list("  " + self.str1), dtype=object).reshape((concatenated.shape[0],1))
        concatenated = np.concatenate( (table_left_header,concatenated), axis=1 )
        return concatenated
    
    def run(self):
        try:
            if self.table is None:
                raise ValueError("Table not initialized with strings.")
            str1, str2 = self.str1, self.str2
            for col_index in range(1, len(str2) + 1):
                self.table[0, col_index] = self.table[0, col_index-1] - 1
            for row_index in range(1, len(str1) + 1):
                self.table[row_index, 0] = self.table[row_index-1, 0] - 1

            for row_index in range(1,len(str1) + 1):
                for col_index in range(1, len(str2) + 1):
                    left = self.table[row_index, col_index-1]
                    up   = self.table[row_index-1, col_index]
                    diagonal = self.table[row_index-1, col_index-1]
                    
                    top_score  = self.miss + up
                    left_score = self.miss + left
                    diagonal_score = diagonal + (1 if str1[row_index-1] == str2[col_index -1] else self.miss)
                    self.table[row_index,col_index] = max([top_score, left_score, diagonal_score])
                    
        except Exception as e:
            print(e)