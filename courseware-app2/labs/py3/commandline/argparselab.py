'''_

For this lab, you can refer to the argparse module docs:

https://docs.python.org/3/library/argparse.html

You are going to create several instances of ArgumentParser. The first
is called "parser1":

>>> type(parser1)
<class 'argparse.ArgumentParser'>

The tests here ask you to add arguments to the parser, properly
configured, using the add_argument() method. parser1 takes two
required arguments:

>>> args1 = parser1.parse_args(["foo", "bar"])
>>> args1.filename
'foo'
>>> args1.destination
'bar'

>>> args1 = parser1.parse_args(["alpha", "beta"])
>>> args1.filename
'alpha'
>>> args1.destination
'beta'


Let's make some other parsers, exercising features like flags and
default arguments.

>>> type(parser2)
<class 'argparse.ArgumentParser'>

>>> args2 = parser2.parse_args(["data.txt", "--type", "json"])
>>> args2.filename
'data.txt'
>>> args2.type
'json'

>>> args2 = parser2.parse_args(["data.txt"])
>>> args2.filename
'data.txt'
>>> args2.type
'text'


>>> args3 = parser3.parse_args(["names.txt", "--limit", "50"])
>>> args3.input
'names.txt'
>>> args3.limit
50

>>> args3 = parser3.parse_args(["names.txt"])
>>> args3.input
'names.txt'
>>> args3.limit
100


>>> args4 = parser4.parse_args(["stocks.csv", "accounts.csv", "--ignore-duplicates"])
>>> args4.input
'stocks.csv'
>>> args4.output
'accounts.csv'
>>> args4.ignore_duplicates
True

>>> args4 = parser4.parse_args(["-i", "stocks.csv", "accounts.csv"])
>>> args4.input
'stocks.csv'
>>> args4.output
'accounts.csv'
>>> args4.ignore_duplicates
True

>>> args4 = parser4.parse_args(["stocks.csv", "accounts.csv"])
>>> args4.input
'stocks.csv'
>>> args4.output
'accounts.csv'
>>> args4.ignore_duplicates
False

'''

# Write your code here:



# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    count, _ = doctest.testmod()
    if count == 0:
        print('*** ALL TESTS PASS ***\nGive someone a HIGH FIVE!')

# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
