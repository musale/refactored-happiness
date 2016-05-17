# Define a procedure, stamps, which takes as its input a positive integer in
# pence and returns the number of 5p, 2p and 1p stamps (p is pence) required 
# to make up that value. The return value should be a tuple of three numbers 
# (that is, your return statement should be followed by the number of 5p,
# the number of 2p, and the nuber of 1p stamps).
#
# Your answer should use as few total stamps as possible by first using as 
# many 5p stamps as possible, then 2 pence stamps and finally 1p stamps as 
# needed to make up the total.
def stamps(num):
	a=num-num%5
	b=num-a-(num-a)%2
	c=num-a-b-(num-a-b)%1
	prtstr = "5p: "+str(a/5)+",2p: "+str(b/2)+",1p: "+str(c)
	print prtstr
	return (a/5,b/2, c)

stamps(4)

