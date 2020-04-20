# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:35:38 2019

@author: admin
"""

q = input("""로우 데이터로 실행하지 마시고, 로우데이터를 복사한 후 data폴더 안에 붙여넣어 실행해주세요.
y를 입력하면 소스가 실행되고, n을 입력하면 취소됩니다.\n : """)

if q == "n":
    print("취소완료")

elif q == "y":
    
    # 디렉토리 주소 지정
    import os
    WORK_PATH = os.getcwd().replace('\\','/')    # 현재폴더 설정
    DATA_PATH = WORK_PATH + "/data/"     # raw데이터를 복사한 copy폴더 설정

    
    # 필요한 빈 리스트 지정     
    dir_name_list = []
    dir_addr_list= []
    dir_counter = len([iq for iq in os.scandir(DATA_PATH)]) # 폴더의 개수 저장
    img_name_list = []
    img_count_list = []


    dir_list = os.listdir(DATA_PATH)
    for file_name_reader in dir_list:
        dir_name_list.append(file_name_reader)    # 디렉토리의 이름 저장
        DATA_ADDR = DATA_PATH + file_name_reader
        dir_addr_list.append(DATA_ADDR + "/")   # 디렉토리 주소 저장
        img_name_list.append(os.listdir(DATA_ADDR))    # 이미지 이름 저장
        DATA_COUNT = len([iq for iq in os.scandir(DATA_ADDR)])
        img_count_list.append(DATA_COUNT)    # 이미지 개수 저장

    print("-"*50)
    print("폴더이름 예시 1개 : "); print(dir_name_list[0]); print("-"*50)
    print("폴더주소 예시 1개 : "); print(dir_addr_list[0]); print("-"*50)
    print("폴더개수 : "); print(dir_counter); print("-"*50)
    print("이미지이름 예시 1개 : "); print(img_name_list[0][0:1]); print("-"*50)
    print("이미지파일개수 예시 1개 : "); print(img_count_list[0])
    print("-"*50)
    print("data폴더에 저장됩니다. \n")
    
     
    FNE= ".png"
    FNE2= ".jpg"  # 확장자(File Name Extension) 설정


    for i in range(dir_counter):
        dir_name = dir_name_list[i]
        print(str(i+1)+ "개 완료 : " + dir_name_list[i])    # 개수와 이름 출력
        
        new_filename_list = []
    
        for j in range(0, img_count_list[i]):
            if j < 10 : 
                new_filename = dir_name_list[i] + "_000" + str(j) + FNE2
                new_filename_list.append(new_filename)
            elif j < 100 :
                new_filename = dir_name_list[i] + "_00" + str(j) + FNE2
                new_filename_list.append(new_filename)
            elif j < 1000 :
                new_filename = dir_name_list[i] + "_0" + str(j) + FNE2
                new_filename_list.append(new_filename)
            else :
                new_filename = dir_name_list[i] + "_" + str(j) + FNE2
                new_filename_list.append(new_filename)

            file1 = dir_addr_list[i] + img_name_list[i][j]
            file2 = dir_addr_list[i] + new_filename_list[j]

            os.rename(file1, file2)
        
        print("마지막 파일 : [" + img_name_list[i][j] + "]", " ==> ",
              "[" + new_filename_list[j] + "]")
        
else :
    print("y와 n만 입력해주세요.")

print("=== 1번 코드 종료 ===")
print("★ 엑셀에 작업해주세요 ★")