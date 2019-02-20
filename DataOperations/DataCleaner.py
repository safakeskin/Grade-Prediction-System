import numpy as np
import pandas as pd
import functools as ftls

class DataCleaner:
    @staticmethod
    def read_concat_csv( file_path, header_cnt="infer", col_pass_ctr=None, col_take_ctr=None, names=None ):
        f_data = pd.read_csv(file_path,",",header=header_cnt, names=names, dtype=str).values
        # n_size = f_data.shape
        c_data = []
        for row in f_data[:, (col_pass_ctr if col_pass_ctr is not None else 1 ) :]:
            c_data.append(ftls.reduce(lambda x,y: x+y, row))
        
        return np.array(c_data)
    
    @staticmethod
    def write_np_array_to_txt( np_array, target ):
        np.savetxt(t_name, np_array.astype("str"), fmt="%s")
    
    @staticmethod
    def display_np_array(np_array):
        for i, row in enumerate(np_array):
            print(i, row)

if __name__ == "__main__":
    try:
        import sys
        f_path = "../DataSet/tripadvisor_review.csv"
        t_path = "../Clustering/ExampleTexts/"
        if len(sys.argv) == 2 or len(sys.argv) > 3:
            raise ValueError("Zero or Two parameters should be given.")
        if len(sys.argv) == 3:
            f_path = sys.argv[1]
            t_path = sys.argv[2]
        
        f_name = f_path.strip().split("/")[-1].split(".")[0]
        t_name = t_path + f_name + ".txt"

        data = DataCleaner.read_concat_csv(f_path)
        DataCleaner.write_np_array_to_txt( data , t_name )
    except ValueError as ve:
        print(repr(ve))
    except Exception as e:
        print("General Exception: " + repr(e))
