"""
Solutions to exam tasks for module M4
Name:
Code:
"""

import concurrent.futures as future
import statistics

# A9
def get_balance(index):
    """This method opens customers.json and returns the field
    'balance' for the person with the given index.
    Leave this method as is.
    Note that '$' and ',' are removed from 'balance' in the jason file"""
    import json
    with open('customers.json') as f:
        data = json.load(f)
        return float(data[index]['balance'].replace('$', '').replace(',', ''))
def get_total_balance():
    results = []

    with future.ProcessPoolExecutor() as ex:
        index = range(112)
        results = list(ex.map(get_balance,index))
    return sum(results)
    
    
    
# A10

def get_mean_balances():
    """Method that return the mean balance for male and female customes. Gender 
    is set in the field 'gender' ('male' or 'female')"""
    import json
    male = []
    female = []
    for index in range(112):
        with open('customers.json') as f:
            data = json.load(f)
            if data[index]['gender'] == 'male':
                male.append(float(data[index]['balance'].replace('$', '').replace(',', '')))
            elif data[index]['gender'] == 'female':
                female.append(float(data[index]['balance'].replace('$', '').replace(',', '')))
            else:
                print("ERROR!")
    return [statistics.mean(male), statistics.mean(female)]
       
    
# B4
def leapyears(years):
    """A method the returns the leap years of the years in the in argument years"""
    return [n for n in years if (n%4==0 and n%100 != 0) or (n%400 == 0)]


def main():
    """
    print('Test of A9 ')
    print(get_total_balance())
    print('Test of A10 ')
    print(get_mean_balances())
    """
    print('Test of B4 ')
    ly=leapyears(range(1900,2101))
    print(ly)
    if ly != None:
        print(len(ly))
    

if __name__ == "__main__":
    main()
    print('Over and out')
