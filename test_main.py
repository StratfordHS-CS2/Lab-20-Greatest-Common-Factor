import main

def test_30_105():
    assert main.gcf(30,105) == 15, 'Incorrect result for gcf(30, 105)'

def test_15_20():
    assert main.gcf(15, 20) == 5, 'Incorrect result for gcf(15, 20)'

def test_9_12():
    assert main.gcf(9, 12) == 3, 'Incorrect result for gcf(9,12)'

def test_5_7():
    assert main.gcf(5, 7) == 1, 'Incorrect result for gcf(5, 7)'
