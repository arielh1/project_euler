
def check_if_is_a_fraction(num,den):
    if int(num) ==int(den) :
        return False
    if num[0] == den[1]:
        if int(num[1])/int(den[0])==int(num)/int(den):
            print(num,"/",den)
            return True
    if num[1] == den[0]:
        if int(num[0])/int(den[1])==int(num)/int(den):
            print(num,"/",den)
            return True
    return False


def problem_33():

    lst=[]
    result=1
    for i in range(1,9):
        for j in range(1,10):
            str_num = str(i)+str(j)
            for k in range(1,10):
                for q in range(1,10):
                    str_num2 = str(k)+str(q)
                    if check_if_is_a_fraction(str_num,str_num2):
                        temp=int(str_num)/int(str_num2)
                        if(temp<1):
                            result *= temp



                        lst.append((str_num,str_num2))
    print(result**-1)
    return result



if __name__ == "__main__":
    problem_33()