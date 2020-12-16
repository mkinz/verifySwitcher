import pytest
from copier import Copier
import os


class TestCopier:
    def test_copier_function(self):
        dut = Copier()
        dut.copier_test() #bs test method
        assert os.path.isfile('total_test_bs_file.py')
        os.remove('total_test_bs_file.py')

    def test_copier_filenotfounderror(self):
        dut = Copier()
        with pytest.raises(FileNotFoundError):
            dut.copy_prod_machine_files_to_verify() #this is failing to raise an error, why??

    def test_copier_permissionerror(self):
        pass