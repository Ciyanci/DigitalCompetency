import speedtest

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download = st.download() / 1000000
    upload = st.upload() / 1000000
    ping = st.results.ping
    return download, upload, ping