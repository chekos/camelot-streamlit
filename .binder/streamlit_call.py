from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(["streamlit", "run", "https://github.com/chekos/camelot-streamlit/blob/master/camelot_app.py", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
