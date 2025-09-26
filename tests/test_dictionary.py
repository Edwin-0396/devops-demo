from app.dictionary import Dictionary

def test_dictionary():
    d = Dictionary()
    d.newentry("Apple", "Fruit")
    assert d.look("Apple") == "Fruit"
    assert "Banana" in d.look("Banana")
