import numpy as np

import pandas as pd

'''
The following code is to help you play with the concept of Dataframe in Pandas.

You can think of a Dataframe as something with rows and columns. It is
similar to a spreadsheet, a database table, or R's data.frame object.

*This playground is inspired by Greg Reda's post on Intro to Pandas Data Structures:
http://www.gregreda.com/2013/10/26/intro-to-pandas-data-structures/
'''

'''
To create a dataframe, you can pass a dictionary of lists to the Dataframe
constructor:
1) The key of the dictionary will be the column name
2) The associating list will be the values within that column.
'''
# Change False to True to see Dataframes in action
if False:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    print football

'''
Pandas also has various functions that will help you understand some basic
information about your data frame. Some of these functions are:
1) dtypes: to get the datatype for each column
2) describe: useful for seeing basic statistics of the dataframe's numerical
   columns
3) head: displays the first five rows of the dataset
4) tail: displays the last five rows of the dataset
'''
# Change False to True to see these functions in action
if True:
    data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
            'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions',
                     'Lions', 'Lions'],
            'wins': [11, 8, 10, 15, 11, 6, 10, 4],
            'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
    football = pd.DataFrame(data)
    # print "Printing Data Type : 1) dtypes: to get the datatype for each column "
    # print football.dtypes
    # print ""
    # print "Printing Description : 2) describe: useful for seeing basic statistics of the dataframe's numerical columns"
    # print football.describe()
    # print ""
    # print "Printing Head :  displays the first five rows of the dataset"
    # print football.head()
    # print ""
    # print "Printing tail : displays the last five rows of the dataset"
    # print football.tail()
    #
    # ########################### select data from cloumn ###################
    #
    # print football['team']
    # print football[['team', 'wins']]
    print "teeeeeeeeeeeeeee"
    print football.items
    print football.iloc[[6]]
    print football.loc[[6]]
    # print football[['year' == 2011] , football['team'] =='Bears']
    # print ""
    # print football[football['wins'] > 10]
    # print ""
    # print football[(football.year == 2011) & (football.wins > 10)]
    # print ""
    # print football[(football.wins > 10) & (football.team == "Packers")]
    # print ""
    # print football[(football) & (football.wins == 6)]