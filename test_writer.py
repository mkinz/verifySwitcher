import pytest
import io
import builtins
from unittest.mock import patch
from pytest import fixture
from writer import Writer

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










