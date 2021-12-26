import pytest
from notepad.src.file_menu.file_menu import FileMenu


@pytest.mark.file
def test_file_new():
    """
    Click the File > New menu item
    """
    app = FileMenu()
    app.file_new()


@pytest.mark.file
def test_file_new_window():
    """
    Click the File > New Window menu item
    """
    app = FileMenu()
    app.file_new_window()


@pytest.mark.file
def test_file_open():
    """
    Click the File > Open menu item
    """
    app = FileMenu()
    app.file_open()


@pytest.mark.file
def test_file_save():
    """
    Click the File > Save menu item
    """
    app = FileMenu()
    app.file_save()


@pytest.mark.file
def test_file_save_as():
    """
    Click the File > Save As menu item
    """
    app = FileMenu()
    app.file_save_as()


@pytest.mark.file
def test_file_page_setup():
    """
    Click the File > Page Setup menu item
    """
    app = FileMenu()
    app.file_page_setup()


@pytest.mark.file
def test_file_print():
    """
    Click the File > Print menu item
    """
    app = FileMenu()
    app.file_print()


@pytest.mark.file
def test_file_exit():
    """
    Click the File > Exit menu item
    """
    app = FileMenu()
    app.file_exit()



