###### this is the first .py file ###########

####### write your code here ##########

#parity checking

N=input()               #taking the input string and conveting into binary
N=str(N)

x= N.count('1')              #counting the no of ones in string
if (x % 2) == 0:             #loop for inserting 1 and 0 in the sttring
    print(N+ '1')
else:
    print(N+'0') 		#printing accordingly


#bit stuffing
j=0
while (j<len(N)):
   a=N.find('010')			#finding the location of 010 on the frame if present  
   m='0'
   a=a+2                          #increaisng he index in order to get the output
   n=N[:a]+'0'+N[a:]                	#padding 0 at the end of 010
   j=j+1   



print(n+'0101')         #joining flag in the end


