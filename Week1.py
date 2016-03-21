import pylab

# pylab.figure(1)
# pylab.plot([1,2,3,4],[1,7,3,5])
# pylab.show()
#
# pylab.figure(2)
# pylab.plot([1,5,3,4],[1,9,8,4])
# pylab.savefig('Figure-Aryan')

# pylab.figure(1)
# pylab.plot([5, 6, 10, 3])x values default to range(len(y))
# pylab.savefig('Figure-Singh')

principal = 10000
interestRate = 0.05
years = 20
values = []

for i in range(years+1):
    values.append(principal)
    principal += principal*interestRate
pylab.plot(range(years+1), values,'ro',linewidth = 20)
pylab.title('Compound Interest at 5%',fontsize = 21)
pylab.xlabel('Years Of Compounding',fontsize = 10)
pylab.ylabel('Value Of Principal ($)',fontsize = 10)
pylab.show()

#.rc file to override defaults

