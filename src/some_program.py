# first development commit
# first feature commit

my_str_var = ""
new_var_feature = ""
another_var_feature = ""

def some_function(mylist=[]):
    _mylist = mylist
    for x in _mylist:
        print(f"x is {x}")

mylist = ['one', 'two', 'three', 'four']

if __name__ == "__main__":
    some_function(mylist=mylist)

