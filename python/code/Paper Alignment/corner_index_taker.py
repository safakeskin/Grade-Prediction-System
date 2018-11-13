import numpy as np
class CIT:
    @staticmethod
    def iterate(image, color, reverse=False):
        def take_updown(image):
            return np.flipud( image )

        def is_color( cell_color, i_color ):
            return  True if cell_color == i_color else False

        if reverse:
            image = take_updown(image)

        row_count, col_count = image.shape[0], image.shape[1]
        row_index = 0
        col_index = 0
        
        while row_index < row_count:
            col_index = 0
            while col_index < col_count:
                cell_value = image[row_index][col_index]
                if is_color( cell_value , color):
                    return (row_index, col_index)   # return y and x
                col_index += 1
            row_index += 1
        
        return (-1, -1) # could not be found
 
    @staticmethod    
    def handle_result (result):
        try:
            if result == (-1,-1):
                raise ValueError('Index not found.')
            return result
        except ValueError:
            print('Desired index could not be found.')
            return None

    @staticmethod
    def get_begin (image, color):
        result = CIT.iterate( image, color )
        return CIT.handle_result(result)
        
    @staticmethod
    def get_end(image, color ):
        result = CIT.iterate( image, color, reverse=True )
        return CIT.handle_result(result)
    
    @staticmethod
    def get_begin_end(image, color):
        begin_indexes   = CIT.get_begin( image, color )
        end_indexes     = CIT.get_end( image, color )
        return [begin_indexes, end_indexes]
