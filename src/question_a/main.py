#Prompt the user for a number and display the total of the even values


def get_sum_of_evens(num):
        sum = get_sum_of_evens
        sum = 0
        for i in range(2, num+1, 2):
            sum += i
        return sum

number = int(input("Enter a number: "))
result = get_sum_of_evens(number)
print("Sum of even numbers up to", number, "is:", result)

