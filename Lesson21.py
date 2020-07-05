# -*- coding: UTF-8
#continue文は、繰り返し処理で、ある条件にあてはまったときにその処理をスキップしたい場合

for i in range(5):
    if i == 3:
        continue
    print(i)