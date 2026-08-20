class A:
    var1 = "welcome class A"

class B:
    var2 = "welcome class B"    

class C(A, B):
    var3   = "welcome class C" 

cl = C()
print(cl.var1) 
print(cl.var2)
print(cl.var3)