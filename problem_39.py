#check if p is the perimeter of a right angle triangle with integral length sides, {a, b, c}
def is_right_angle(a, b, c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
#check if p=a+b+c
def is_perimeter(p,a, b, c):
    if a+b+c == p:
        return True
    else:
        return False
#get number and check if is square  root is integer
def is_square_root(n):
    if n**0.5 % 1 == 0:
        return True
    else:
        return False

def main():
    #dic to store the results size 1000 initialized to 0
    max_index=0
    max_length=0
    result = [0]*1001


    for p in range(1000,1,-1):
        for a in range(1,p):
           for b in range( 1,p):
                c=a*a+b*b
                if is_square_root(c):
                    if p==a+b+c**0.5:
                        if(a>b):
                            key=(b,a,c)
                        else:
                            key=(a,b,c)
                        if result[p]!=0:
                            if key not in result[p]:
                                result[p].append(key)
                        else:
                            result[p]=[key]
                        if len(result[p])>max_length:
                            max_length=len(result[p])
                            max_index=p
                            print(max_index)
                            print(max_length)
    print(max_index)
    print(max_length)
    return result[max_index]




if __name__ == "__main__":
    main()
