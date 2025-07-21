from LoginWINDOW import LoginWindow

def logout(current_window):
    login_window = LoginWindow()
    login_window.show()
    current_window.close()