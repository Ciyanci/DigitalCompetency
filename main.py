from speed_test import get_speed



def run_speed_check():
    print("\nTestomg your connection speed, please wait 10-30 seconds...")
    download, upload, ping = get_speed()
    print(f"\nDownload: {download:.2f} Mbps")
    print(f"\nUpload:   {upload:.2f} Mbps")
    print(f"Ping:       {ping:.1f} ms")