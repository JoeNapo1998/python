for i in range (1, 1000):
    psif1 = (i / 100)
    boith = (i % 100)
    psif2 = (boith / 10)
    psif3 = (boith % 10)
    athrisma_psif = (psif1 + psif2 + psif3)
    if (psif1 == 0):
        psif1 = 1
        if (psif2 == 0) :
            psif2 = 1

    ginomeno = psif1 * psif2 * psif3
    if (i % athrisma_psif == 0):
       print "The number  " ,i, "is Harshad "
    if not(ginomeno ==0):
	   if (i % ginomeno == 0):
			print "The number   " ,i, "is being divided perfectly by  the product of its digits"
print "The number  1000 is Harshad "
