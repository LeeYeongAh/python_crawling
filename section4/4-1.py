import pickle #객체, 텍스트 직렬화, 역직렬화

#파일 이름과 데이터
bfilename = 'c:/section4/test.bin'
tfilename = 'c:/section4/test.txt'

data1=77
data2='hello world!'
data3=['dog','cat','good']

#바이너리
with open(bfilename,'wb') as f:
    pickle.dump(data1,f) #dump : 문자열 직렬화
    pickle.dump(data2,f)
    pickle.dump(data3,f)


#텍스트
with open(tfilename,'wt') as f:
    f.write(str(data1))
    f.write('\n')
    f.write(str(data2))
    f.write('\n')
    f.writelines('\n'.join(data3))
    f.write('\n')


with open(bfilename,'rb') as f:
    b = pickle.load(f) #문자열 역직렬화
    print(type(b), 'binary read1 | ',b)
    b = pickle.load(f) #문자열 역직렬화
    print(type(b), 'binary read2 | ',b)
    b = pickle.load(f) #문자열 역직렬화
    print(type(b), 'binary read3 | ',b)

with open(tfilename,'rt') as f:
    for i, line in enumerate(f,1):
        print(type(line), 'Text Read'+str(i)+'|', line, end='')
