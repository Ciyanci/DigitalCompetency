def main():

    print("WIFI USE CASE RECOMMENDATION")

    download=checkNum("Enter download speed (Mbps): ")
    upload=checkNum("Enter upload speed (Mbps): ")
    ping=checkNum("Enter ping (ms): ")

    recommend(download,upload,ping)


def checkNum(message):
    check=0

    while check==0:
        num=input(message)

        if num.isdigit():
            num=int(num)
            check=1
        else:
            print("Error! Please enter a positive number only.")

    return num


def recommend(download,upload,ping):

    print("\n----- WIFI RECOMMENDATION -----")

    if download >= 100 and ping <= 30:
        print("Connection Quality: Excellent")
        print("- 4K streaming")
        print("- Online gaming")
        print("- Video call")
        print("- Multiple devices")

    elif download >= 25 and ping <= 50:
        print("Connection Quality: Good")
        print("- HD streaming")
        print("- Online gaming")
        print("- Video call")

    elif download >= 10:
        print("Connection Quality: Average")
        print("- Web browsing")
        print("- Social media")
        print("- Video streaming")

    elif download >= 5:
        print("Connection Quality: Slow")
        print("- Basic browsing")
        print("- Social media")
        print("- Messaging")

    else:
        print("Connection Quality: Very Slow")
        print("- Basic messaging only")



main()
