import pytest
import src.matlib as matlib
class Test_Matlib:
    
    #Adition test 
    def test_add(self):
        assert matlib.Add(0,0) == 0
        assert matlib.Add(-3.5,3.5) == 0
        assert matlib.Add(124,1000.52) == 1124.52
        assert matlib.Add(-5,-3) == -8
        assert matlib.Add(-5, 3 ) == -2
        assert matlib.Add(-5, 20) == 15
    
    #substraction test
    def test_sub(self):
        assert matlib.Sub(10,10) == 0
        assert matlib.Sub(100.00, 10.2) == 89.8
        assert matlib.Sub(-100, -100) == 0
        assert matlib.Sub(100, -5) == 105
        assert matlib.Sub(100, 10.21) == pytest.approx(89.79, 10e-20)

    #multiplication test
    def test_mul(self):
        assert matlib.Mul(2,2) == 4
        assert matlib.Mul(3.52, 2.51) == pytest.approx(8.8352, 10e-20)
        assert matlib.Mul(10, -2) == -20
        assert matlib.Mul(-10, -5.2) == 52
        assert matlib.Mul (0.025, 0.0001) == 2.5e-6

    #division test
    def test_div(self):
        assert matlib.Div(0 , 1.54  ) == 0
        assert matlib.Div(9,3) == 3
        assert matlib.Div(0.50, 0.10) == 5
        assert matlib.Div(-5 , -2) == 2.5
        assert matlib.Div(4, 2) == 2
        with pytest.raises(ZeroDivisionError):
            matlib.Div(2,0)
    
    #power test
    def test_pow(self):
        assert matlib.Pow(2,2) == 4
        assert matlib.Pow(-10,2) == 100
        assert matlib.Pow(2,10) == 1024
        assert matlib.Pow(-3.2 , 5) == pytest.approx(-335.54432 , 10e-20)
        assert matlib.Pow(10, 0) == 0
        assert matlib.Pow(0.5, 4) == pytest.approx(0.0625, 10e-20)
         
         # zero pow of zero is undefined
        with pytest.raises(ValueError):
            matlib.Pow(0,0)
    
    #factorial test
    def test_fact(self):
        assert matlib.Fact(5) == 120
        assert matlib.Fact(2) == 2    
        assert matlib.Fact(0) == 1
        assert matlib.Fact(8) == 40320
       
        # factorial is defined only for positive integers
        with pytest.raises(ValueError):
            matlib.Fact(0.123)

        with pytest.raises(ValueError):
            matlib.Fact(-10)    

    #root test
    def test_sqroot(sefl):
        assert matlib.Root(4, 2) == 2
        assert matlib.Root(16, 4) == 2
        assert matlib.Root(0.25, 2) == 0.5
        assert matlib.Root(4, 2) == 2
        assert matlib.Root(0,2) == 0
        assert matlib.Root(10000,4) == 10
        
        #root of negative number is undefined
        with pytest.raises(ValueError):
            matlib.Root(-2,2)

        with pytest.raises(ValueError):
            matlib.Root(-2,5)

        #0-th root is undefined
        with pytest.raises(ValueError):
            matlib.Root(4,0)
                           

#######################################################END OF FILE####################################