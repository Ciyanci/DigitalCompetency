from speed_test import get_speed



def run_speed_check():
    print("\nTesting your connection speed, please wait 10-30 seconds...")
    download, upload, ping = get_speed()
    print(f"\nDownload: {download:.2f} Mbps")
    print(f"Upload:   {upload:.2f} Mbps")
    print(f"Ping:       {ping:.1f} ms")


def main():
    print("=== Wifi Checker ===")
    print("Test your wifi speed to determine suitability")

    while True:
        print("\n1. Test my connection speed")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            run_speed_check()
        elif choice =="5":
            print("Adios Amigo!")
            break
        else:
            print("Invalid option. Please enter 1, 2, 3 ,4, or 5")

if __name__ == "__main__":
    main()