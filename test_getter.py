import argparse
from argparse import Namespace
from getter import Getter

class Test_Getter:

    def test_get_input(self):
        dut = Getter()
        key = dut.get_input(['mgc_mebes'], argparse.ArgumentParser())  # namespace obj
        assert key == Namespace(flag='mgc_mebes')