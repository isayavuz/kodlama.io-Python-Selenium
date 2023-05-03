--PyTest decorator--

@pytest.mark.parametrize:
Bir testin parametrelendirilmesi, testi birden fazla girdi kümesine karşı çalıştırmak için yapılır. Bunu parametrize işaretçiyi kullanarak yapabiliriz.
Örnek Kod:
    
    import pytest

    @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
    def test_multiplication_11(num, output):
    assert 11*num == output

Burada test bir girişi 11 ile çarpar ve sonucu beklenen çıktı ile karşılaştırır. Testin 4 girdi seti vardır, her birinin 2 değeri vardır biri 11 ile çarpılacak sayı, diğeri beklenen sonuçtur.

Çıktı:
    test_multiplication.py::test_multiplication_11[1-11] PASSED
    test_multiplication.py::test_multiplication_11[2-22] PASSED
    test_multiplication.py::test_multiplication_11[3-35] FAILED
    test_multiplication.py::test_multiplication_11[4-44] PASSED
    ============================================== FAILURES
    ==============================================
    _________________ test_multiplication_11[3-35] __________________
    num = 3, output = 35
    @pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
    def test_multiplication_11(num, output):
    >  assert 11*num == output
    E  assert (11 * 3) == 35
    test_multiplication.py:5: AssertionError
    ============================== 1 failed, 3 passed, 8 deselected in 0.08 seconds
    ==============================

@pytest.fixture:
Uygulandığı her test fonksiyonundan önce çalışacak fonksiyonlardır. fixture, veritabanı bağlantıları, test edilecek URL'ler ve bir tür girdi verileri gibi bazı verileri testlere beslemek için kullanılır. Bu nedenle, her test için aynı kodu çalıştırmak yerine, testlere fixture işlevi ekleyebiliriz ve her testi gerçekleştirmeden önce çalışır ve verileri teste döndürür.
Örnek Kod:
    
    import pytest

    @pytest.fixture
    def input_value():
    input = 39
    return input

    def test_divisible_by_3(input_value):
    assert input_value % 3 == 0

    def test_divisible_by_6(input_value):
    assert input_value % 6 == 0

Burada, testlere girdi sağlayan input_value adında bir fixture fonksiyonumuz var . fixture işlevine erişmek için testlerin, fixture adını giriş parametresi olarak belirtmesi gerekir.
Pytest, test yürütülürken, giriş parametresi olarak fixture adını görecektir. Daha sonra fixture işlevini yürütür ve döndürülen değer, test tarafından kullanılabilen giriş parametresinde saklanır.

Çıktı:
    test_div_by_3_6.py::test_divisible_by_3 PASSED
    test_div_by_3_6.py::test_divisible_by_6 FAILED
    ============================================== FAILURES
    ==============================================
    ________________________________________ test_divisible_by_6
    _________________________________________
    input_value = 39
    def test_divisible_by_6(input_value):
    >  assert input_value % 6 == 0
    E  assert (39 % 6) == 0
    test_div_by_3_6.py:12: AssertionError
    ========================== 1 failed, 1 passed, 6 deselected in 0.07 seconds
    ==========================

@pytest.mark.skip:
skip Bir test işlevini atlamanın en basit yolu, onu isteğe bağlı olarak geçirilebilecek dekoratörle işaretlemektir.
Örnek Kod:
    
    @pytest.mark.skip(reason="no way of currently testing this")
    def test_the_unknown():
     ...

@pytest.mark.skipif:
Koşullu olarak bir şeyi atlamak istiyorsanız, bunun skipif yerine kullanabilirsiniz. Python3.10'dan önceki bir yorumlayıcıda çalıştırıldığında atlanacak bir test işlevini işaretlemenin bir örneğini aşağıda bulabilirsiniz.
Örnek Kod:
    
    @pytest.mark.skipif(sys.version_info < (3, 10), reason="requires python3.10 or higher")
    def test_function():
     ...
