import src.identifier.identifier as identifier
class Testclass:
    def test_identifier1(self):
        assert identifier.identifier("a123456") == False
    def test_identifier2(self):
        assert identifier.identifier("78787848484") == False
    def test_identifier3(self):
        assert identifier.identifier("a1") == True
    def test_identifier4(self):
        assert identifier.identifier("") == False
    def test_identifier5(self):
        assert identifier.identifier("a12345") == True
    def test_identifier6(self):
        assert identifier.identifier("a*") == False