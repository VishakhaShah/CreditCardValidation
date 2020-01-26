# execfile("/Users/shahvishakharadhamohan/Documents/CreditCardvalidation.py")
filename ="CreditCardvalidation.py"
# exec(compile(open(filename, "rb").read(), filename, 'exec'), globals, locals)
exec(open(filename).read())
def test_card_number_Validations():
    assert validate(4591150040397804) == True
    assert validate(459115004039780) == False
    assert validate(4591150040397808) == False
    print("ok")

def test_cardExpiry():
    assert validate_date('2020/12/31') == True
    assert validate_date('2023/1/31') == True
    assert validate_date('2010/12/31') == False
    assert validate_date('2020-12/31') == False
    assert validate_date('2020/16/45') == False


def test_card_cvv():
    assert validate_cvv("324") == True
    assert validate_cvv("3204") == False
    assert validate_cvv("879") == True
    assert validate_cvv("goa") == False

def test_card_name():
    assert validate_name("vishakha") == True
    assert validate_name("vish10192kha") == False
    assert validate_name(129) == False

if __name__ == "__main__":
    test_card_number_Validations()
    test_card_name()
    test_cardExpiry()
    test_card_cvv()

