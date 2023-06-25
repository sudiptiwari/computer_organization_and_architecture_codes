def AND(input1, input2):
    if(input1 == '1' and input2 == '1'):
        return '1'
    else:
        return '0'
    
    
def OR(input1, input2):
    if(input1 == '1' or input2 == '1'):
        return '1'
    else:
        return '0'
    
    
def NOT(input1):
    if(input1 == '0'):
        return '1'
    else:
        return '0'
    
    
def XOR(input1, input2):
    if(input1 == input2):
        return '0'
    else:
        return '1'
    
    
def addition(num1, num2, n):
    num1 = num1.zfill(n)
    num2 = num2.zfill(n)
    reversed_num1 = num1[::-1]
    reversed_num2 = num2[::-1]
    cin = '0' # initial carry in = 0
    SUM = ''
    for i in range(n):
        SUM = SUM + XOR(XOR(reversed_num1[i],reversed_num2[i]),cin)
        intermediate_xor = XOR(reversed_num1[i], reversed_num2[i])
        intermediate_and = AND(reversed_num1[i], reversed_num2[i])
        cin = OR(intermediate_and, AND(intermediate_xor,cin))
#     cin = OR(AND(reversed_num1[i],reversed_num2[i]),AND(XOR(reversed_num1[i],reversed_num2[i]),cin))

    SUM = SUM[::-1]
    return SUM, cin
