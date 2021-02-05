

def bit_at(n, bit):
    return (n>>bit) & 1

def find_missing(a, bits):

    indexes = range(len(a))
    missing = 0
    indexes = range(len(a))
    for bit in range(bits):
        ones=[]
        zeroes=[]
       
        ones = [i for i in indexes if bit_at(a[i], bit)==1]
        #for i in indexes:
        #    if bit_at(a[i],bit)==1:
        #        ones.append(a[i])
        zeroes = [i for i in indexes if bit_at(a[i], bit)==0]
        #for i in indexes:
        #    if bit_at(a[i],bit)==0:
        #        zeroes.append(a[i])
        print("ones" + str (ones))
       
        print("zeroes" + str(zeroes))
       
        print()
       
        if len(ones) <= len(zeroes):
            indexes = ones
            missing |= (1<<bit) 
        else:
            indexes = zeroes

    return missing



print([8,11,9,10,12,13,6,15,7,2,3,4,1,5,0])
print()
print ("missing number is " + str(find_missing([8,11,9,10,12,13,6,15,7,2,3,4,1,5,0], 4)))