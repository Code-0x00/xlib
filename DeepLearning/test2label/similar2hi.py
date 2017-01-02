import os

similar=[[0 for i in range(37)] for j in range(37)]

class Threshold:

	def dataread(self,path):
		global similar
		
		if os.path.isfile(path):
			
			file_object=open(path,'rb')
			count=0
			for lines in file_object.readlines():
				nums=lines[0:-2].split(' ')
				count_num=0
				for num in nums:
					similar[count][count_num]=float(num)
					count_num+=1
				count+=1
			file_object.close()
				
					
	def data2hi(self):
		global similar
		accuracy=[0 for i in range(5)]
		classfi=[0 for i in range(5)]
		file_label=0
		file_object=open('data.log','rb')
		file_write=open('data2hi.txt','w')
		count=-1
		for lines in file_object.readlines():
			count+=1
			if count>=6:
				count=0
				hi=0
				for i in range(5):
					hi+=accuracy[i]*similar[classfi[i]][file_label]
					#print accuracy[i]
					#print similar[classfi[i]][file_label]
				file_write.write(path[3]+'\n')
				file_write.write(str(file_label)+'\n')
				file_write.write(str(hi)+'\n')
			if count==0:
				path=lines.split(' ')
				#print path[3]

				label=lines.split('/')
				class_=label[5].split('d') 
				#print class_[1]
				file_label=int(class_[1])-1
				
			else:
				label=lines.split('-')
				accuracy[count-1]=float(label[0])
				#print accuracy[count-1]
				tmp=label[1].split('"')
				classfi[count-1]=int(tmp[1])
				#print accuracy
				#print classfi
		file_object.close()
		file_write.close()
		
	def datasave(self):
		global similar
		file_object=open('similar2hi.txt','w')
	
		for i in similar:
			for j in i:
				file_object.write(str(j)+' ')
			file_object.write('\n')
		file_object.close()

if __name__=="__main__":
	test=Threshold()
	test.dataread('data2similar.txt')
	test.data2hi()

