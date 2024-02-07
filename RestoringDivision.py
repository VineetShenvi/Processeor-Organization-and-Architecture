def one_complement(s):
    ans = []
    for bit in s:
        if bit == '0':
            ans.append("1")
        else:
            ans.append("0")
    return ''.join(ans)    

def left_shift(s):
    ans= []
    for bit in range(1, len(s)):
        ans.append(s[bit])
    nbits = int(len(ans)//2)
    A = ans[0:nbits+1]
    Q = ans[nbits+1: len(ans)]
    return ''.join(A), Q


def single_bit_addition(b0, b1, carry):
    sum = "0"
    if b0 == "0" and b1 == "0" and carry == "0":
        sum = "0"
        carry = "0"
    elif b0 == "0" and b1 == "1" and carry == "0":
        sum = "1"
        carry = "0"
    elif b0 == "1" and b1 == "0" and carry == "0":
        sum = "1"
        carry = "0"
    elif b0 == "1" and b1 == "1" and carry == "0":
        sum = "0"
        carry = "1"
    elif b0 == "0" and b1 == "0" and carry == "1":
        sum = "1"
        carry = "0"
    elif b0 == "0" and b1 == "1" and carry == "1":
        sum = "0"
        carry = "1"
    elif b0 == "1" and b1 == "0" and carry == "1":
        sum = "0"
        carry = "1"
    elif b0 == "1" and b1 == "1" and carry == "1":
        sum = "1"
        carry = "1"
    return sum, carry

def binaryaddition(a, b):
    carry = "0"
    ans = []

    for i in range(len(b)):
        ans.append("0")

    for i in reversed(range(len(b))):
        sum, carry = single_bit_addition(a[i], b[i], carry)
        ans[i] = sum
    return (''.join(ans))
        
def two_complement(s):
    one = []
    for i in range(len(s)-1):
        one.append("0")
    one.append("1")
    s = one_complement(s) 
    ans = binaryaddition(s, one)
    return ''.join(ans)

def restoringdivision(M, Q):
    count = len(M)
    A = []

    for i in range(len(M)):
        A.append("0")
    for i in range(count-1):
        A, Q = left_shift(''.join(A)+''.join(Q))
        A = binaryaddition(A, two_complement(M))
        if(A[0] == '1'):
            A = binaryaddition(A, M)
            Q.append('0')
        else:
            Q.append('1')
    rem = ''.join(A)
    quo = ''.join(Q)
    return rem, quo

def binary_to_decimal(binary):
    decimal = 0
    for i in range(len(binary)):
        decimal += (pow(2, (len(binary)-1)-i)*int(binary[i]))
    return decimal

if __name__ == '__main__':
    print("Vineet Shenvi     60004220012")
    print("Enter two numbers:")
    a = input()
    b = input()
    rem, quo = restoringdivision(a, b)
    print("Quotient: " + quo + " (" + str(binary_to_decimal(quo)) + ")")
    print("Remainder: " + rem + " (" + str(binary_to_decimal(rem)) + ")")


