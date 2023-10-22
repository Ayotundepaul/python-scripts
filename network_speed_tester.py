import speedtest

def test_network_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / (10**6)  # Convert from bits to megabits
    upload_speed = st.upload() / (10**6)      # Convert from bits to megabits
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")

test_network_speed()
