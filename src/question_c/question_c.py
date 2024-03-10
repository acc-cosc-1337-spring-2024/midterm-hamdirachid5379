#write functions here, don't add input('') statements here!

def is_prime(number):
    is_prime = True
    if number > 1:
        for i in range(2, number):
            if(number % i) == 0:
                print(i, "is a factor")
                is_prime = False

            elif is_prime:
                print(number, "is prime")
            else :
                print("Number need to be > 1")
                