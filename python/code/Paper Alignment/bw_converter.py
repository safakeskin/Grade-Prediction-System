class ColorCovert:
    @staticmethod
    def binary_converter(image):
        i = 0
        row_count, col_count = image.shape[0], image.shape[1]
        row_index = col_index = 0

        while row_index < row_count:
            col_index = 0
            while col_index < col_count:
                image[row_index][col_index] = 0 if image[row_index][col_index] < 45 else 255
                col_index += 1
            row_index += 1

        # for row in image:
        #     for cell in row:
        #         if i < 10:
        #             print(cell)
        #         cell = 0 if cell < 128 else 255
        #         i += 1
        #         if i < 10:
        #             print(cell)
        return image