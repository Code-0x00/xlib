import os


class Threshold:

	def dataread(self,path):
		#print 'dataread'
		
		if os.path.isfile(path):
			#print 'path'
			file_object=open(path,'rb')
			file_write=open('hi2label.label','w')
			count=0
			for lines in file_object.readlines():
				if count>=3:
					count=0
				if count==0:
					file_path=lines[0:-1]
				if count==1:
					file_class=int(lines[0:-1])
				if count==2:
					acc=float(lines[0:-1])
					if acc>0.2:
						file_write.write(file_path+' '+str(file_class)+'\n')
				count+=1
			file_write.close()
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

if __name__=="__main__":
	test=Threshold()
	test.dataread('data2hi.txt')
	#test.data2hi()

