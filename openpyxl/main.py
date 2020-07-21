from excel import Excel
from time import process_time

start_time = process_time()

####creating an object 
obj = Excel()  #obj is an instance of the class Excel.

total_credit = (obj.liability + obj.income)
total_debit = (obj.assets + obj.expenses)

print("Debit : {} , Credit : {} ".format(total_debit, total_credit))  

difference = obj.income - obj.expenses


def main():
    user_input = input("Please enter your Profit Amount : ")
    try:
        profit_Amount = int(user_input)
        if profit_Amount == (difference) and obj.liability == obj.assets:
            print("Successfully done")
        else:
            print("Your Profit amount must match the difference of income and expenses, Please try Again!")
            main()

    except ValueError:
        print("Amount must be in numbers")
        main()    

if __name__ == '__main__':
    main()


end_time = process_time()
print("Time taken for execution : ", end_time, start_time)


