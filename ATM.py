

#1 for deposite Amount 
#2 for withdraw amount 
#3 for current balance 
#0 for exit 
#user given ATM pin (1234)
pin = int (input ("Enter ATM pin number"))
balance = 0.0
if pin == 1234 :
	print ("Welcome to MyBank")
	while True :
		print ("1 for deposite\n2 for Withdraw\n3 for check current balance\n0 for exit ")
		ch = int (input  ("Please Select Any one option "))
		if ch == 1 :
			damount = float (input ("Enter Deposite Amount"))
			balance = balance + damount
		elif ch == 2 :
			wamount = float (input ("Enter withdraw amount"))
			if wamount >= balance :
				print ("Sorry try again")
				exit (0)
			else : 
				balance = balance - wamount 
		elif ch == 3 :
			print ("current balance =", balance )
		elif ch == 0 :
			exit (0)
		else : 
			print ("Your choice is invalid\n Try next Time ")
			exit (0)
else : 
	print ("Invalid ATM pin\n Try Again!!!")




