import threading

import webview
import uvicorn

from main import app

# 启动服务
t = threading.Thread(target=uvicorn.run, args=(app,))
t.daemon = True
t.start()

# 在PyWebview应用程序中加载FastAPI应用程序的URL
webview.create_window('点钞记录系统', 'http://127.0.0.1:8000')
webview.start()
