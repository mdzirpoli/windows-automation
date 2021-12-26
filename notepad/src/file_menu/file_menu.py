from pywinauto import application


app = application.Application()


class FileMenu:
    """
    All File menu dropdown selections
    """

    @staticmethod
    def file_new():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->New")
        except Exception as e:
            print(e)

    @staticmethod
    def file_new_window():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->New Window")
        except Exception as e:
            print(e)

    @staticmethod
    def file_open():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Open...")
        except Exception as e:
            print(e)

    @staticmethod
    def file_save():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Save")
        except Exception as e:
            print(e)

    @staticmethod
    def file_save_as():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Save As...")
        except Exception as e:
            print(e)

    @staticmethod
    def file_page_setup():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Page Setup...")
        except Exception as e:
            print(e)

    @staticmethod
    def file_print():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Print...")
        except Exception as e:
            print(e)

    @staticmethod
    def file_exit():
        try:
            app.start("Notepad.exe")
            app.Notepad.menu_select("File->Exit")
        except Exception as e:
            print(e)


