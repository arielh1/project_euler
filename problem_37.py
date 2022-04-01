def is_prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def main():
    number=11
    Truncatable_primes=[]
    while len(Truncatable_primes)<13:
        if is_prime(number):

            number_str=str(number)
            number_r=number_str[0:-1]
            number_l=number_str[1:]
            while True:
                if not is_prime(int(number_r)):
                    break
                if not is_prime(int(number_l)):
                    break

                number_r = number_r[0:-1]
                number_l = number_l[1:]
                if len(number_l)==0 and len(number_r)==0:
                    Truncatable_primes.append(number)
                    print(Truncatable_primes)
                    break
        number+=2


if __name__ == "__main__":
    main()