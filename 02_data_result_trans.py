# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:58:35 2019

@author: admin
"""

# 디렉토리 주소 지정
import os
WORK_PATH = os.getcwd().replace('\\','/')    # 현재폴더 설정
DATA_PATH = WORK_PATH + "/data/"     # data폴더 설정
RESULT_PATH = WORK_PATH + "/result"    # result폴더 설정


# 만약 result폴더가 없으면 생성
dir_name = 'result'
if not os.path.exists('./result/'):    
    os.mkdir(WORK_PATH + '/' + dir_name + '/')
    
    
    
# 필요한 빈 리스트 지정     
dir_name_list = []
dir_addr_list= []
dir_counter = len([iq for iq in os.scandir(DATA_PATH)]) # 폴더의 개수 저장
img_name_list = []
img_count_list = []



# 각 폴더마다 해당 내용을 읽어서 리스트로 지정
dir_list = os.listdir(DATA_PATH)
for file_name_reader in dir_list:
    dir_name_list.append(file_name_reader)    # 디렉토리의 이름 저장

    for data_addr_and_count in file_name_reader:
        DATA_ADDR = DATA_PATH + file_name_reader    
        DATA_COUNT = len([iq for iq in os.scandir(DATA_ADDR)])
        dir_addr_list.append(DATA_ADDR + "/")   # 디렉토리 주소 저장
        img_name_list.append(os.listdir(DATA_ADDR))    # 이미지 이름 저장
        img_count_list.append(DATA_COUNT)    # 이미지 개수 저장


# 사용된 변수        
# dir_name_list
# dir_addr_list
# dir_counter
# img_name_list[폴더][파일]
# int(img_count_list)
        
print("-"*50)
print("폴더이름 예시 1개 : "); print(dir_name_list[0]); print("-"*50)
print("폴더주소 예시 1개 : "); print(dir_addr_list[0]); print("-"*50)
print("폴더개수 : "); print(dir_counter); print("-"*50)
print("이미지이름 예시 1개 : "); print(img_name_list[0][0:1]); print("-"*50)
print("이미지파일개수 예시 1개 : "); print(img_count_list[0])
print("-"*50)




# result폴더안에 데이터가 담긴 폴더이름이 없으면, 해당하는 폴더를 만들고,
# 그 폴더 안에 각 텍스트 파일을 생성 (0,0,28,28,"가"로 입력)

FNE= ".png" 
FNE2= ".jpg"  # 확장자(File Name Extension) 설정

for i in range(dir_counter):
    dir_name = dir_name_list[i]
    print(str(i+1)+ "개 완료 : " + dir_name_list[i])    # 개수와 이름 출력
    
    if not os.path.exists('./result/' + dir_name):    
        os.mkdir(RESULT_PATH + '/' + dir_name)


    FINAL_SAVE_PATH = RESULT_PATH + '/' + dir_name +"/"
    
    for j in range(0, img_count_list[i]):
        f = open(FINAL_SAVE_PATH + str(img_name_list[i][j]).replace(FNE2,"") #파일저장
                + ".txt", 'w', encoding="UTF-8")
        f.write('0,0,28,28,"' + dir_name_list[i] + '"\n')
        f.close()

        



print("=== 2번 코드 종료 ===")
