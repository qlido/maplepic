import os
import shutil
import sys
import time

wus = os.path.join(os.path.expanduser('~'))
arr = list()
if os.path.isfile(wus + "\\witch.txt"):
    f = open(wus + "\\witch.txt", 'r')
    line = f.readline()
    f.close()
    for f_name in os.listdir(os.path.join(os.path.expanduser('~'), 'Desktop')):
        if f_name.endswith('.jpg') and f_name.startswith('Maple') or f_name.startswith('maple'):
            arr.append(f_name)

    for move in arr:
        shutil.move(os.path.join(os.path.expanduser('~'), 'Desktop\\') + move, line)
        print(arr)
        print('이동 완료')
        time.sleep(5)
        sys.exit()


else:
    ld = input("파일이 이동될 위치를 정해주세요 : ")
    ld = ld.replace("\\", "/")
    f = open(wus + "\\witch.txt", 'w')
    f.write(ld)
    f.close()
    print("다시 켜주세요")
    time.sleep(0.2)
    sys.exit()
