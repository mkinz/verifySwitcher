import argparse
import io
from pytest import fixture
from argparse import Namespace

from switcher_app import Getter
from switcher_app import Writer

class Test_Getter:

    def test_get_input(self):
        dut = Getter()
        key = dut.get_input(['mgc_mebes'], argparse.ArgumentParser())  # namespace obj
        assert key == Namespace(flag='mgc_mebes')


class Test_Writer:

    @fixture()
    def io_stream(self, mocker):
        return mocker.MagicMock(spec=io.TextIOBase)

    def test_write_mentor_jeol(self, mocker, io_stream):
        mo = mocker.mock_open()
        mo.return_value = io_stream

        # call method
        dut = Writer()

        # mock the open method, patch builtins
        with mocker.mock_module.patch("builtins.open", mo):
            dut.write_list_jeol_file(['MCJ','MLJ'])

        mo.assert_called_once_with('listVrfyRunInfoJEOL', 'a')
        #io_stream.write.assert_called_once_with('MCJ\nMLJ\n')



class Test_Deleter:
    pass

