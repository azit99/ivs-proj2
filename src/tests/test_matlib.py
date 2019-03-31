import pytest
import src.matlib as matlib
class Test_Matlib:
    
    #Adition test 
    def test_add(self):
        assert matlib.add(0,0) == 0
        assert matlib.add(-3.5,3.5) == 0
        assert matlib.add(124,1000.52) == 1124.52
        assert matlib.add(-5,-3) == -8
        assert matlib.add(-5, 3 ) == -2
        assert matlib.add(-5, 20) == 15
    
    #substraction test
    def test_sub(self):
        assert matlib.sub(10,10) == 0
        assert matlib.sub(100.00, 10.2) == 89.8
        assert matlib.sub(-100, -100) == 0
        assert matlib.sub(100, -5) == 105
        assert matlib.sub(100, 10.21) == pytest.approx(89.79, 10e-20)

    #multiplication test
    def test_mul(self):
        assert matlib.mul(2,2) == 4
        assert matlib.mul(3.52, 2.51) == pytest.approx(8.8352, 10e-20)
        assert matlib.mul(10, -2) == -20
        assert matlib.mul(-10, -5.2) == 52
        assert matlib.mul (0.025, 0.0001) == 2.5e-6

    #division test
    def test_div(self):
        assert matlib.div(0 , 1.54  ) == 0
        assert matlib.div(9,3) == 3
        assert matlib.div(0.50, 0.10) == 5
        assert matlib.div(-5 , -2) == 2.5
        assert matlib.div(4, 2) == 2
        assert matlib.div(1000000, 50) == 20000
        assert matlib.div(-10, 5.5) == pytest.approx(1.818181818, 10e-10)
        assert matlib.div(1, 0.001) == 1000
        
        with pytest.raises(ZeroDivisionError):
            matlib.div(2,0)
    
    #power test
    def test_pow(self):
        assert matlib.pow(2,2) == 4
        assert matlib.pow(-10,2) == 100
        assert matlib.pow(2,10) == 1024
        assert matlib.pow(-3.2 , 5) == pytest.approx(-335.54432 , 10e-20)
        assert matlib.pow(10, 0) == 0
        assert matlib.pow(0.5, 4) == pytest.approx(0.0625, 10e-20)
         
         # zero pow of zero is undefined
        with pytest.raises(ValueError):
            matlib.pow(0,0)
    
    #factorial test
    def test_fact(self):
        assert matlib.fact(5) == 120
        assert matlib.fact(2) == 2    
        assert matlib.fact(0) == 1
        assert matlib.fact(8) == 40320

        with pytest.raises(OverflowError):
            matlib.fact(100)
       
        # factorial is defined only for positive integers
        with pytest.raises(ValueError):
            matlib.fact(0.123)

        with pytest.raises(ValueError):
            matlib.fact(-10)    

    #root test
    def test_sqroot(sefl):
        assert matlib.root(4, 2) == 2
        assert matlib.root(16, 4) == 2
        assert matlib.root(0.25, 2) == 0.5
        assert matlib.root(4, 2) == 2
        assert matlib.root(0,2) == 0
        assert matlib.root(10000,4) == 10
        
        #root of negative number is undefined
        with pytest.raises(ValueError):
            matlib.root(-2,2)

        with pytest.raises(ValueError):
            matlib.root(-2,5)

        #0-th root is undefined
        with pytest.raises(ValueError):
            matlib.root(4,0)
                           

#######################################################END OF FILE####################################
