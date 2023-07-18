# import csv
# import json
# import requests
# from colorama import init, Fore, Back, Style
# from src.score_distribution import plot_score_distribution, calculate_average_score

# init(autoreset=True)

# def crawl_data():
#     start_sbd = int(input("Start SBD: "))
#     end_sbd = int(input("End SBD: "))
#     with open('data.csv', 'w', newline='') as file:
#         writer = csv.writer(file)
#         for sbd in range(start_sbd, end_sbd + 1):
#             try:
#                 url = f"https://dantri.com.vn/thpt/1/0/99/{sbd}/2023/0.2/search-gradle.htm"
#                 response = requests.get(url)

#                 if response.status_code == 200:
#                     json_data = response.json()

#                     if json_data:
#                         student_data = json_data["student"]

#                         row_data = [
#                             student_data.get('sbd'),
#                             student_data.get('toan'),
#                             student_data.get('van'),
#                             student_data.get('ngoaiNgu'),
#                             student_data.get('vatLy'),
#                             student_data.get('hoaHoc'),
#                             student_data.get('sinhHoc'),
#                             student_data.get('diemTBTuNhien'),
#                             student_data.get('lichSu'),
#                             student_data.get('diaLy'),
#                             student_data.get('gdcd'),
#                             student_data.get('diemTBXaHoi')
#                         ]
#                         writer.writerow(row_data)

#                         print(f"{Fore.GREEN}[CRAWL] {sbd} thành công")

#                 if sbd == end_sbd:
#                     print(f"{Fore.CYAN}Complete: Data crawling and export complete.")

#             except Exception as e:
#                 print(f"{Fore.RED}[CRAWL] {sbd} không thành công")

# def search_score():
#     sbd = int(input("SBD: "))
#     url = f"https://dantri.com.vn/thpt/1/0/99/{sbd}/2023/0.2/search-gradle.htm"
#     response = requests.get(url)

#     if response.status_code == 200:
#         json_data = response.json()

#         if json_data:
#             student_data = json_data["student"]
#             scores = ''
#             for subject, score in student_data.items():
#                 if score is not None:
#                     scores += f"{subject}: {score}\n"
#             print(f"{Fore.YELLOW}{scores}")
#     else:
#         print(f"{Fore.RED}[SEARCH] {sbd} không thành công")

# print(f"{Back.BLUE}{Fore.WHITE}")
# print("""
#    ████████╗██╗  ██╗██████╗ ████████╗ ██████╗  ██████╗               
#    ╚══██╔══╝██║  ██║██╔══██╗╚══██╔══╝██╔═══██╗██╔════╝       
#       ██║   ███████║██████╔╝   ██║   ██║   ██║██║  ███╗        
#       ██║   ██╔══██║██╔═══╝    ██║   ██║▄▄ ██║██║   ██║      
#       ██║   ██║  ██║██║        ██║   ╚██████╔╝╚██████╔╝              
#       ╚═╝   ╚═╝  ╚═╝╚═╝        ╚═╝    ╚══▀▀═╝  ╚═════╝            
# """)
# print(f"{Style.RESET_ALL}")

# print("1. Crawl Data")
# print("2. Tra cứu điểm thi")
# print("3. Phổ điểm các khối")
# print("4. Exit")

# while True:
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         crawl_data()
#     elif choice == "2":
#         search_score()
#     elif choice == "3":
#         print("1. Khối A")
#         print("2. Khối A1")
#         print("3. Khối B")
#         print("4. Khối C")
#         print("5. Khối D")
#         khối_choice = input("Chọn khối: ")

#         if khối_choice == "1":
#             scores_A = {
#                 "1": 0,
#                 "2": 0,
#                 "3": 0,
#                 "4": 0,
#                 "5": 2,
#                 "6": 11,
#                 "7": 39,
#                 "8": 125,
#                 "9": 226,
#                 "10": 567,
#                 "11": 1018,
#                 "12": 1877,
#                 "13": 2992,
#                 "14": 5364,
#                 "15": 7307,
#                 "16": 12148,
#                 "17": 15462,
#                 "18": 23632,
#                 "19": 28053,
#                 "20": 38956,
#                 "21": 40331,
#                 "22": 46940,
#                 "23": 38241,
#                 "24": 32547,
#                 "25": 17333,
#                 "26": 8898,
#                 "27": 2932,
#                 "28": 811,
#                 "29": 89,
#                 "30": 0
#             }

#             average_score, total_students = calculate_average_score(scores_A)

#             print(f"Điểm trung bình: 20.77")
#             print(f"Tổng số thí sinh: {total_students}")

#             plot_score_distribution(scores_A, "Phổ điểm khối A")
#         elif khối_choice == "2":
#             scores_A1 = {
#                 "1": 0,
#                 "2": 0,
#                 "3": 0,
#                 "4": 0,
#                 "5": 1,
#                 "6": 7,
#                 "7": 29,
#                 "8": 98,
#                 "9": 266,
#                 "10": 633,
#                 "11": 1201,
#                 "12": 2636,
#                 "13": 4187,
#                 "14": 7512,
#                 "15": 10255,
#                 "16": 16621,
#                 "17": 19848,
#                 "18": 28436,
#                 "19": 30826,
#                 "20": 37909,
#                 "21": 34288,
#                 "22": 35477,
#                 "23": 27789,
#                 "24": 25365,
#                 "25": 16755,
#                 "26": 10576,
#                 "27": 3603,
#                 "28": 776,
#                 "29": 51,
#                 "30": 1
#             }

#             average_score, total_students = calculate_average_score(scores_A1)

#             print(f"Điểm trung bình: 20.28")
#             print(f"Tổng số thí sinh: {total_students}")

#             plot_score_distribution(scores_A1, "Phổ điểm khối A1")
#         elif khối_choice == "3":
#             scores_B = {
#                 "1": 0,
#                 "2": 0,
#                 "3": 0,
#                 "4": 1,
#                 "5": 0,
#                 "6": 6,
#                 "7": 8,
#                 "8": 37,
#                 "9": 76,
#                 "10": 222,
#                 "11": 482,
#                 "12": 1134,
#                 "13": 2039,
#                 "14": 4173,
#                 "15": 6496,
#                 "16": 11905,
#                 "17": 16460,
#                 "18": 26240,
#                 "19": 32344,
#                 "20": 44842,
#                 "21": 46779,
#                 "22": 50314,
#                 "23": 35942,
#                 "24": 25223,
#                 "25": 11539,
#                 "26": 5723,
#                 "27": 1896,
#                 "28": 588,
#                 "29": 76,
#                 "30": 9
#             }

#             average_score, total_students = calculate_average_score(scores_B)

#             print(f"Điểm trung bình: 20.60")
#             print(f"Tổng số thí sinh: {total_students}")

#             plot_score_distribution(scores_B, "Phổ điểm khối B")
#         elif khối_choice == "4":
#             scores_C = {
#                 "1": 1,
#                 "2": 2,
#                 "3": 2,
#                 "4": 16,
#                 "5": 17,
#                 "6": 132,
#                 "7": 195,
#                 "8": 834,
#                 "9": 1148,
#                 "10": 3770,
#                 "11": 4113,
#                 "12": 12378,
#                 "13": 12404,
#                 "14": 33387,
#                 "15": 29426,
#                 "16": 66870,
#                 "17": 50431,
#                 "18": 94215,
#                 "19": 59374,
#                 "20": 94766,
#                 "21": 50848,
#                 "22": 69700,
#                 "23": 31518,
#                 "24": 35910,
#                 "25": 13143,
#                 "26": 12132,
#                 "27": 3198,
#                 "28": 1707,
#                 "29": 83,
#                 "30": 1
#             }

#             average_score, total_students = calculate_average_score(scores_C)

#             print(f"Điểm trung bình: 20.60")
#             print(f"Tổng số thí sinh: {total_students}")

#             plot_score_distribution(scores_C, "Phổ điểm khối C")
#         elif khối_choice == "5":
#             scores_D = {
#                 "1": 0,
#                 "2": 0,
#                 "3": 0,
#                 "4": 2,
#                 "5": 21,
#                 "6": 134,
#                 "7": 500,
#                 "8": 1699,
#                 "9": 3481,
#                 "10": 7810,
#                 "11": 12601,
#                 "12": 22269,
#                 "13": 29115,
#                 "14": 43429,
#                 "15": 50222,
#                 "16": 67170,
#                 "17": 70733,
#                 "18": 85709,
#                 "19": 80157,
#                 "20": 87488,
#                 "21": 74411,
#                 "22": 73829,
#                 "23": 57403,
#                 "24": 51205,
#                 "25": 32820,
#                 "26": 19512,
#                 "27": 5362,
#                 "28": 595,
#                 "29": 0,
#                 "30": 0
#             }

#             average_score, total_students = calculate_average_score(scores_D)

#             print(f"Điểm trung bình: 18.90")
#             print(f"Tổng số thí sinh: {total_students}")

#             plot_score_distribution(scores_D, "Phổ điểm khối D")
#         else:
#             print("Khối không hợp lệ. Vui lòng chọn lại.")
#     elif choice == "4":
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice. Please try again.")
