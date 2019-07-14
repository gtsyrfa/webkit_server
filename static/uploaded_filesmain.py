def browser_upload():
    from PyQt5.QtWidgets import QApplication
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtGui import QIcon
    import sys
    url = 'http://127.0.0.1:5000/'

    app = QApplication(sys.argv)

    browser = QWebEngineView()
    # print (dir(browser))
    browser.load(QUrl(url))
    browser.setFixedSize(400, 286)
    browser.setWindowTitle("Погрузи-ка")
    browser.setWindowIcon(QIcon("icon.jpg"))
    browser.page().profile().cookieStore().deleteAllCookies()
    browser.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    browser_upload()
	
	