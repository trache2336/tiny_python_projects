from password import clean, ransom, l33t
import secrets


# --------------------------------------------------
def test_clean():
    """Test clean"""

    assert clean('') == ''
    assert clean("states,") == 'states'
    assert clean("Don't") == 'Dont'


# --------------------------------------------------
def test_ransom():
    """Test ransom"""

    state = secrets.SystemRandom().getstate()
    secrets.SystemRandom().seed(1)
    assert (ransom('Money') == 'moNeY')
    assert (ransom('Dollars') == 'DOLlaRs')
    secrets.SystemRandom().setstate(state)


# --------------------------------------------------
def test_l33t():
    """Test l33t"""

    state = secrets.SystemRandom().getstate()
    secrets.SystemRandom().seed(1)
    assert l33t('Money') == 'moNeY{'
    assert l33t('Dollars') == 'D0ll4r5`'
    secrets.SystemRandom().setstate(state)
