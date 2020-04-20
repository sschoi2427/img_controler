# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 19:27:28 2019

@author: admin
"""

# 초성 리스트. 00 ~ 18 / 중성 리스트. 00 ~ 20 / 종성 리스트. 00 ~ 27 + 1(1개 없음)
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ',
                'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ',
                'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ',
                 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ',
                 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

JONGSUNG_LIST = ['', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ',
                 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ',
                 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 변환
CHOSUNG_DICT = {'ㄱ':'r', 'ㄲ':'rr', 'ㄴ':'s', 'ㄷ':'e', 'ㄸ':'ee', 'ㄹ':'f',
                'ㅁ':'a', 'ㅂ':'q', 'ㅃ':'qq', 'ㅅ':'t', 'ㅆ':'tt', 'ㅇ':'d',
                'ㅈ':'w', 'ㅉ':'ww', 'ㅊ':'c', 'ㅋ':'z', 'ㅌ':'x', 'ㅍ':'v', 'ㅎ':'g'}

JUNGSUNG_DICT = {'ㅏ':'k', 'ㅐ':'o', 'ㅑ':'i','ㅒ':'oo', 'ㅓ':'j', 'ㅔ':'p',
                 'ㅕ':'u', 'ㅖ':'pp', 'ㅗ':'h', 'ㅘ':'hk', 'ㅙ':'ho', 'ㅚ':'hl',
                 'ㅛ':'y', 'ㅜ':'n', 'ㅝ':'nj', 'ㅞ':'np', 'ㅟ':'nl', 'ㅠ':'b',
                 'ㅡ':'m', 'ㅢ':'ml', 'ㅣ':'l'}

JONGSUNG_DICT = {'ㄱ':'r', 'ㄲ':'rr', 'ㄳ':'rt', 'ㄴ':'s', 'ㄵ':'sw',
                 'ㄶ':'sg', 'ㄷ':'e', 'ㄹ':'f', 'ㄺ':'fr', 'ㄻ':'fa',
                 'ㄼ':'fq', 'ㄽ':'ft', 'ㄾ':'fx', 'ㄿ':'fv', 'ㅀ':'fg',
                 'ㅁ':'a', 'ㅂ':'q', 'ㅄ':'qt', 'ㅅ':'t',  'ㅆ':'tt',
                 'ㅇ':'d', 'ㅈ':'w', 'ㅊ':'c', 'ㅋ':'z', 'ㅌ':'x',
                 'ㅍ':'v', 'ㅎ':'g', ' ':'', '':''}

# 디렉토리 주소 지정
import os
WORK_PATH = os.getcwd().replace('\\','/')    # 현재폴더 설정
DATA_PATH = WORK_PATH + "/data/"     # raw데이터를 복사한 copy폴더 설정
RESULT_PATH = WORK_PATH + "/result/"


# 필요한 빈 리스트 지정        
dir_name_list = []
dir_addr_list= []
dir_counter = len([iq for iq in os.scandir(DATA_PATH)]) # 폴더의 개수 저장
img_name_list = []
img_count_list = []

LIST = os.listdir(DATA_PATH)
r_list = []
for i in range(len(LIST)):
    for w in list(LIST[i].strip()):
        if '가'<=w<='힣':
            ch1 = (ord(w) - ord('가'))//588 # 21*28=588개 마다 초성이 바뀜. 
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28 # 중성은 총 28가지 종류
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_list.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
            dir_name_list.append(LIST[i])    # 디렉토리의 이름 저장
            DATA_ADDR = DATA_PATH + LIST[i]
            dir_addr_list.append(DATA_ADDR + "/")   # 디렉토리 주소 저장
        else:
            pass
        
        
print("1번째 폴더 이름 :", dir_name_list[0])    
print("1번째 폴더 주소 :", dir_addr_list[0])
print(r_list)




for i in range(len(r_list)):
    for j in range(3):
        ch1 = CHOSUNG_DICT.get(r_list[i][0])
        ch2 = JUNGSUNG_DICT.get(r_list[i][1])
        ch3 = JONGSUNG_DICT.get(r_list[i][2])
        new_dir_name = ch1+ch2+ch3
    print(dir_name_list[i], "=>", new_dir_name)
    
    file1 = DATA_PATH + dir_name_list[i] + "/"
    file2 = DATA_PATH + new_dir_name + "/"
    file3 = RESULT_PATH + dir_name_list[i] + "/"
    file4 = RESULT_PATH + new_dir_name + "/"
    print(file1)
    print(file2)
    print(file3)
    print(file4)
    
    
    os.rename(str(file1), str(file2))
    os.rename(str(file3), str(file4))
    
   


print("=== 3번 코드 종료 ===")
print("★ 엑셀에 작업해주세요 ★")








