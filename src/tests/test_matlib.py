import pytest
import src.math_lib as matlib

class Test_Matlib:

    #Adition test
    def test_add(self):
        assert matlib.add(0,0) == 0
        assert matlib.add(-3.5,3.5) == 0
        assert matlib.add(124,1000.52) == 1124.52
        assert matlib.add(-5,-3) == -8
        assert matlib.add(-5, 3 ) == -2
        assert matlib.add(-5, 20) == 15
        assert matlib.add(100256, 125.651) == 100381.651
        assert matlib.add(26.26548, 3232.242342) == 3258.507822
        assert matlib.add(22932.12323, 2323.42432) == pytest.approx(25255.54755000000, 10e-10)
        assert matlib.add(-987789.255 ,956.65656) == -986832.59844


    #substraction test
    def test_sub(self):
        assert matlib.sub(10,10) == 0
        assert matlib.sub(100.00, 10.2) == 89.8
        assert matlib.sub(-100, -100) == 0
        assert matlib.sub(100, -5) == 105
        assert matlib.sub(100, 10.21) == pytest.approx(89.79, 10e-20)
        assert matlib.sub(788, 988.25) == pytest.approx(-200.25, 10e-10)
        assert matlib.sub(23.324234, -12.3434) == pytest.approx(35,667634, 10e-10)
        assert matlib.sub(2123.32432, 423432.343) == pytest.approx(-421309.01868, 10e-10)


    #multiplication test
    def test_mul(self):
        assert matlib.mul(2,2) == 4
        assert matlib.mul(3.52, 2.51) == pytest.approx(8.8352, 10e-20)
        assert matlib.mul(10, -2) == -20
        assert matlib.mul(-10, -5.2) == 52
        assert matlib.mul (0.025, 0.0001) == 2.5e-6
        assert matlib.mul(1555,2342.21321) == pytest.approx(3642141.54155, 10e-10)
        assert matlib.mul(2342.324324,332.343) == pytest.approx(778455.092811132, 10e-10)
        assert matlib.mul (0.00, 0.000) == 0.00
        assert matlib.mul (100, 0.000) == 0.00



    #division test
    def test_div(self):
        assert matlib.div(0 , 1.54  ) == 0
        assert matlib.div(9,3) == 3
        assert matlib.div(0.50, 0.10) == 5
        assert matlib.div(-5 , -2) == 2.5
        assert matlib.div(4, 2) == 2
        assert matlib.div(1000000, 50) == 20000
        assert matlib.div(-10, 5.5) == pytest.approx(-1.8181818181818181, 10e-10)
        assert matlib.div(1, 0.001) == 1000
        assert matlib.div(-65.256, 8.36) == pytest.approx(-7.805741627, 10e-10)

        with pytest.raises(ZeroDivisionError):
            matlib.div(2,0)

    #power test
    def test_pow(self):
        assert matlib.pow(2,2) == 4
        assert matlib.pow(-10,2) == 100
        assert matlib.pow(2,10) == 1024
        assert matlib.pow(-3.2 , 5) == pytest.approx(-335.54432 , 10e-10)
        assert matlib.pow(10, 0) == 1
        assert matlib.pow(0.5, 4) == pytest.approx(0.0625, 10e-10)
        assert matlib.pow(1.323, 0) == 1

         # zero pow of zero is undefined
        with pytest.raises(ValueError):
            matlib.pow(0,0)

        with pytest.raises(OverflowError):
            matlib.pow(10000,100000)

    #factorial test
    def test_fact(self):
        assert matlib.fact(5) == 120
        assert matlib.fact(2) == 2
        assert matlib.fact(0) == 1
        assert matlib.fact(8) == 40320
        assert matlib.fact(10) == 3628800

        # factorial is defined only for positive integers
        with pytest.raises(ValueError):
            matlib.fact(0.123)

        with pytest.raises(ValueError):
            matlib.fact(-10)

    #root test
    def test_root(self):
        assert matlib.root(4, 2) == 2
        assert matlib.root(16, 4) == 2
        assert matlib.root(0.25, 2) == 0.5
        assert matlib.root(4, 2) == 2
        assert matlib.root(0,2) == 0
        assert matlib.root(10000,4) == 10
        assert matlib.root(3.52,2) == pytest.approx(1.876166304, 10e-10)
        assert matlib.root(55.23, 2) == pytest.approx(7,431688906, 10e-10)

        #root of negative number is undefined
        with pytest.raises(ValueError):
            matlib.root(-2,2)

        with pytest.raises(ValueError):
            matlib.root(-2,5)

        #0-th root is undefined
        with pytest.raises(ValueError):
            matlib.root(4,0)


#######################################################END OF FILE####################################
