import os

similar=[[0 for i in range(37)] for j in range(37)]
prob=[0 for i in range(37)]
class Threshold:

	def dataread(self,path):
		global similar
		global prob

		if os.path.isfile(path):
			file_object=open(path,'rb')
			count=-1
			for lines in file_object.readlines():
				count=count+1
				if count==0:
					nums=lines[0:-2].split(' ')
					count_num=0
					#print nums
					for num in nums:
						#print num
						prob[count_num]=float(num)
						count_num+=1
				else:
					nums=lines[0:-2].split(' ')
					count_num=0
					#print nums
					for num in nums:
						similar[count-1][count_num]=float(num)
						count_num+=1

			file_object.close()
				
					
	def datasimilar(self):
		global similar
		global prob
		
		for i in range(37):
			for j in range(37):
				similar[i][j]=similar[i][j]/(prob[i]+prob[j]-similar[i][j])
	def datasave(self):
		global similar
		#global prob
		file_object=open('data2similar.txt','w')

		for i in similar:
			for j in i:
				file_object.write(str(j)+' ')
			file_object.write('\n')
		file_object.close()

if __name__=="__main__":
	test=Threshold()
	test.dataread('data2data.txt')
	test.datasimilar()
	test.datasave()

