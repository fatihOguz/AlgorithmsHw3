def removeAssign(arr,num):

	j=0
	length = len(arr[0])
	j=0
	while j < length:
		if(arr[1][j] == num):
			arr[1][j]=-1
		j=j+1
	
	


def jobPeople(job,people):

	

	print("jobs " + str(job))
	print("people " + str(people))
	length = len(job[0])
	
	flag=1

	while flag!=0:
		
		flag=0
		i=0
		while i <  length:
			j=0
			while j < length:

				if(people[1][j]<job[0][i]):
					if(people[0][j]>job[1][i]):
						removeAssign(job,people[0][j])
						removeAssign(people,job[0][i])
						job[1][i]=people[0][j]
						people[1][j]=job[0][i]
						print("jobs " + str(job))
						print("people " + str(people))
						print()
						flag=1
				j=j+1

			i=i+1

			
	print("jobs " + str(job))
	print("people " + str(people))
	print()



job=[[15,13,74,84,78,18,89,75],[0,0,0,0,0,0,0,0]]
people=[[7,3,5,85,17,4,11,8],[0,0,0,0,0,0,0,0]]
job1=[[1,2,3,4],[0,0,0,0]]
people2=[[9,6,7,8],[0,0,0,0]]
jobPeople(job,people)
print("jobs " + str(job[0]))
print("people " + str(job[1]))