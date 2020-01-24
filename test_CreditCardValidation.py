execfile("/Users/shahvishakharadhamohan/Documents/CreditCardvalidation.py")
def test_card_Validations():
    assert validate(get_cc_number()) == True

def test_cardExpiry():
    assert validate_date() == True

def test_card_cvv():
    assert validate_cvv() == True

def card_name():
    assert validate_name() == True
