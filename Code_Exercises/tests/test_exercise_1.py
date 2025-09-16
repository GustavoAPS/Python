# Implement here the solution
def func(x):
    return "_".join(x)


def test_answer():
    names = ['Edward', 'Bella', 'Alice']
    assert func(names) == 'Edward_Bella_Alice'
