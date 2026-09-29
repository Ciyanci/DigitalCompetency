import urllib.request as urec
import time
from speed_test import get_speed
from test_history import compare_results, save_result, show_history
from use_case import wifiUse

def run_speed_check():
    print("\nTesting your connection speed, please wait 10-30 seconds...")
    download, upload, ping = get_speed()
    print(f"\nDownload: {download:.2f} Mbps ({download / 8:.2f} MB/s)")
    print(f"Upload:   {upload:.2f} Mbps ({upload / 8:.2f} MB/s)")
    print(f"Ping:       {ping:.1f} ms")
    
    wifiUse(download,upload,ping)
    save_result(download, upload, ping)
# Verifying if user is connected to internet
def check_internet():
    host = "http://www.google.com"
    try:
        urec.urlopen(host)
        return True
    except:
        return False



def main():
    print("=== Wifi Checker ===")
    print("Test your wifi speed to determine suitability")

    while True:
        print("\n1. Test my connection speed")
        print("2. Show speed test history")
        print("3. Compare two past tests")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            if check_internet():
                run_speed_check()
            else:
                print("\nPlease connect to the internet first")
                time.sleep(2)

        elif choice == "2":
            show_history()

       elif choice == "3":
            show_history()
            try:
                num1 = int(input("\nEnter first test number: "))
                num2 = int(input("Enter second test number: "))
                compare_results(num1, num2)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                break 
                
        elif choice =="5":
            print("Adios Amigo!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3 ,4, or 5")

if __name__ == "__main__":
    main()
