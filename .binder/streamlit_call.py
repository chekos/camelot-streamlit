from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(["streamlit", "run camelot_app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
