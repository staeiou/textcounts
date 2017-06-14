import pandas as pd
import textcounts
def test_core():
    test_list = pd.Series(["this is a test", "THIS IS A TEST", "This is a Test"])

    assert textcounts.prop_mentions(test_list, ["test", "this"]) == 1
    assert textcounts.prop_mentions(test_list, ["test"]) == 1
    assert textcounts.prop_mentions(test_list, ["test"], exclude="a test") == 0
    assert textcounts.prop_mentions(test_list, ["test", "this"], exclude="a test") == 1
