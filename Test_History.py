import csv
import os
from datetime import datetime

def save_result(download, upload, ping):
    file_exists = os.path.exists("wifi_history.csv")
    
    with open("wifi_history.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        if not file_exists:
            writer.writerow(["Time", "Download", "Upload", "Ping"])
            
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        writer.writerow([current_time, round(download, 2), round(upload, 2), round(ping, 2)])
    print("Result saved to history!")

def show_history():
    if not os.path.exists("wifi_history.csv"):
        print("No history found yet.")
        return

    with open("wifi_history.csv", "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))[1:] # Skip header row
        
        print("\n--- PAST RESULTS ---")
        for index, row in enumerate(rows, 1):
            print(f"Number {index} | Date: {row[0]} | DL: {row[1]} Mbps | UL: {row[2]} Mbps | Ping: {row[3]} ms")

def compare_results(number1, number2):
    with open("wifi_history.csv", "r", encoding="utf-8") as file:
        rows = list(csv.reader(file))[1:]
        
        try:
            test1 = rows[number1 - 1]
            test2 = rows[number2 - 1]
            
            dl_change = ((float(test2[1]) - float(test1[1])) / float(test1[1])) * 100
            ul_change = ((float(test2[2]) - float(test1[2])) / float(test1[2])) * 100
            
            print(f"\nComparing Test {number1} and Test {number2}:")
            print(f"Download speed changed by: {dl_change:+.1f}%")
            print(f"Upload speed changed by: {ul_change:+.1f}%")
            
        except:
            print("Error: That test number doesn't exist.")
