def add(a,b):
	print("Answer is ",a+b)

def sub(a,b):
	print("Answer is ",a-b)

def multy(a,b):
	print("Answer is ",a*b)

def divide(a,b):
	print("Answer is ",a/b)


def banner():
	print("")
	print("██████╗        █████╗  █████╗ ██╗")
	print("██╔══██╗      ██╔══██╗██╔══██╗██║")
	print("██████╔╝█████╗██║  ╚═╝███████║██║")
	print("██╔══██╗╚════╝██║  ██╗██╔══██║██║")
	print("██║  ██║      ╚█████╔╝██║  ██║███████╗")
	print("╚═╝  ╚═╝       ╚════╝ ╚═╝  ╚═╝╚══════╝")
	print("       Tool by - Razor Kenway")
	print("          SL Android "       )
	print("")
	print(' [1] ADD')
	print(' [2] SUB')
	print(' [3] MULTIPLY')
	print(' [4] DIVIDE')
	print('')


def main ():
	x=int(input( "Enter your Choise : "))
	a=int(input( "Enter First No : "))
	b=int(input( "Enter Second No : "))

	if x==1:
		add(a,b)
	elif x==2:
		sub(a,b)
	elif x==3:
		multy(a,b)
	elif x==4:
		divide(a,b)
	else:
		print("error")


banner()
main()
