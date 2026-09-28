import speedtest

def get_speed():
    st = speedtest.Speedtest()
    st.get_best_server() #get fastest server
    download = st.download() / 1000000 #converts bits per second into mbps
    upload = st.upload() / 1000000 #converts bits per second into mbps
    ping = st.results.ping
    return download, upload, ping