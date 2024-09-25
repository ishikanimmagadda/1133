


##x = Complex(2.7,3)
##y = Complex(-4,0)
##z = Complex(0,-1.5)

##print(x.real)       	# 2.7
##print(x.get_real()) 	# 2.7
##print(y.get_imag()) 	# 0

##x.set_real(6)
##z.set_imag(-2.5)

##print(x.real)       	# 6
##print(x)            	# 6 + 3i
##print(y)            	# -4 + 0i
##print(z)            	# 0 + -2.5i
##print(x+y)          	# 2 + 3i
##print(z+y+x)        	# 2 + 0.5i
##print(y*z)          	# 0.0 + 10.0i
##print(x*z)          	# 7.5 + -15.0i
##print(x*y+x*z)      	# -16.5 + -27.0i
##print(x*(y+z))      	# -16.5 + -27.0i
##print(x == y)       	# False
##print(x*y+x*z == x*(y+z))   # True
