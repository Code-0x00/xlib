import os

similar=[[0 for i in range(37)] for j in range(37)]
prob=[0 for i in range(37)]
class Threshold:

	def dataread(self,path):
		global similar
		global prob
		
		classfi=[0 for i in range(5)]

		if os.path.isfile(path):
			file_object=open(path,'rb')
			count=-1
			for lines in file_object.readlines():
				count=count+1
				if count>=6:
					count=0
					for i in range(5):
						for j in range(5):
							similar[classfi[i]][classfi[j]]+=1
				if count==0:

					label=lines.split('/')
					class_=label[5].split('d') 
					#print class_[1]
					num=int(class_[1])
					#print test
				else:
					label=lines.split('-')
					#print label[0]
					accuracy=float(label[0])
					tmp=label[1].split('"')
					classfi[count-1]=int(tmp[1])
					prob[classfi[count-1]]+=1
					#print classfi[1]

			file_object.close()
				
					
	def dataclass(self,path):
		global total
		total=30;
		print total
		
		if os.path.isfile(path):
			file_object=open(path,'rb')
			count=-1
			for lines in file_object.readlines():
				count=count+1
				if count>=6:
					count=0
				if count==0:
					label=lines.split('/')
					class_=label[5].split('d')
					#print class_[1]
					num=int(class_[1])
					test=num+1
					#print test
				else:
					label=lines.split('-')
					#print label[0]
					accuracy=float(label[0])
					classfi=label[1].split('"')
					#print classfi[1]
	def datasave(self):
		global similar
		global prob
		file_object=open('return.txt','w')
		#print prob
		for i in prob:
			file_object.write(str(i)+' ')
			#print i
		file_object.write('\n')
		for i in similar:
			for j in i:
				file_object.write(str(j)+' ')
			file_object.write('\n')
		file_object.close()

if __name__=="__main__":
	test=Threshold()
	test.dataread('test.log')
	test.datasave()

