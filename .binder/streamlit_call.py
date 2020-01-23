from subprocess import Popen

# app name must be last arg
def load_jupyter_server_extension(nbapp):
    """serve the streamlit app"""
    Popen(
        [
            "streamlit",
            "run",
            "--browser.serverAddress=0.0.0.0",
            "--server.enableCORS=False",
            "camelot_app.py",
        ]
    )
