"""1.  Create a class Complex Number with data members as real and imag and add following methods : 
a. Constructor 
b. Destructor 
c. Overload +,-  operator"""

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def __del__(self):
        print(f"Complex Number {self.real} + {self.imag} is being deleted.")

    def __add__(self, other):
        real_part = self.real + other.real
        imag_part = self.imag + other.imag

        return ComplexNumber(real_part, imag_part)
    
    def __sub__(self, other):
        real_part = self.real - other.real
        imag_part = self.imag - other.imag

        return ComplexNumber(real_part, imag_part)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        
        else:
            return f"{self.real} - {abs(self.imag)}i"

imgNum = ComplexNumber(3, 2)
imgNum2 = ComplexNumber(1, 7)
sumNum = imgNum + imgNum2
diffNum = imgNum - imgNum2
print("Sum:", sumNum)
print("Difference:", diffNum)
