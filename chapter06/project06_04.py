"""
Table Printer
Write a function named printTable() that takes a list of lists of strings
and displays it in a well-organized table with each column right-justified.
Assume that all the inner lists will contain the same number of strings.

For example, the value could look like this:

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

Your printTable() function would print the following:

   apples Alice  dogs
  oranges   Bob  cats
 cherries Carol moose
   banana David goose

Hint: your code will first have to find the longest string in each of the inner lists
so that the whole column can be wide enough to fit all the strings.
You can store the maximum width of each column as a list of integers.
The printTable() function can begin with colWidths = [0] * len(tableData),
which will create a list containing the same number of 0 values as the number of inner lists in tableData.
That way, colWidths[0] can store the width of the longest string in tableData[0],
colWidths[1] can store the width of the longest string in tableData[1], and so on.
You can then find the largest value in the colWidths list
to find out what integer width to pass to the rjust() string method.
"""

from typing import List


def print_table(table_data: List[List[str]]):
    if table_data:
        # determine rows and columns count
        cols = len(table_data)
        rows = len(table_data[0])

        # determine each column max width based on longest string contained
        col_widths = [0] * cols
        for i in range(cols):
            # make sure rows length is same
            if len(table_data[i]) != rows:
                raise ValueError("Inconsistent table rows length.")
            col_widths[i] = len(max(table_data[i], key=len))

        # rjust table data
        for col in range(cols):
            for row in range(rows):
                table_data[col][row] = table_data[col][row].rjust(col_widths[col])

        # rotate table
        rjust_table = list()
        for row in range(rows):
            rjust_table.append(list())
            for col in range(cols):
                rjust_table[row].append(table_data[col][row])

        # print table
        for row in rjust_table:
            print(" ".join(row))


if __name__ == '__main__':
    table_data = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose'],
    ]
    print_table(table_data)
