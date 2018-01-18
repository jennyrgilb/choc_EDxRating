import os
import glob
import sys
import fnmatch

basedir='/projects/niblab/data/eric_data/design_files/imagine'

ev_name='/projects/niblab/scripts/choc_EDxRating/evs.txt'

#this file has the columns for the mat file
#0 is input
#1 is mean
#2 is appEDxRating score, demeaned
#3 is the unappEDxRating score, demeaned
#4 is the BMI intercept, demeaned
#5 is the BMI slope, demeaned
#6 is the interaction term for app, demeaned
#7 is the interaction term for unapp, demeaned

g=open('input.txt','w')
h=open('mean.txt','w')
j=open('appEDxRate_cov.txt','w')
k=open('unappEDxRate_cov.txt','w')
l=open('BMIintercept_cov.txt','w')
m=open('BMIslope_cov.txt','w')
n=open('interactionappBMIslope_cov.txt', 'w')
o=open('interactionunappBMIslope_cov.txt', 'w')
i=0 

#start the function 
for dir in glob.glob('/projects/niblab/data/eric_data/W1/imagine/level1_grace_edit/cs*.feat'):	
	sub0=dir.split('/')
	sub=sub0[8].strip('++.feat')
#	print(sub)
	with open(ev_name, 'r') as search2:
		for line2 in search2:
			line2 = line2.split('\t')
			print line2	
			name2 = line2[0]
#			print(name2)
			mean = line2[1]
			mean = mean.strip('\n')
			appEDxRate2 = line2[2]
			appEDxRate = appEDxRate2.strip('\n')
			unappEDxRate = line2[3]
			unappEDxRate = unappEDxRate.strip('\n')
#			print(appEDxRate)
			BMIintercept = line2[4]
			BMIintercept = BMIintercept.strip('\n')
			BMIslope = line2[5]
			BMIslope = BMIslope.strip('\n')
			interactionapp = line2[6]
			interactionapp = interactionapp.strip('\n')
			interactionunapp = line2[7]
			interactionunapp = interactionunapp.strip('\n')
#			print(name2+' has a combination score of '+appEDxRate+' ,BMI intercept of '+BMIintercept+' , and a BMI slope of '+BMIslope)
			if fnmatch.fnmatch(name2, sub):
#				print('THIS IS THE SUBJECT'+name2)
#				print(sub)
#				print(line2)
				i=i+1
				print('set feat_files('+str(i)+') '+'"'+dir+'/COPE.feat"')
				g.write('set feat_files('+str(i)+') '+'"/projects/niblab/data/eric_data/W1/imagine/level1_grace_edit/'+name2+'++.feat"'+'\n')
				h.write('set fmri(evg'+str(i)+'.1) '+mean+'\n')  
				j.write('set fmri(evg'+str(i)+'.2) '+appEDxRate+'\n')  
				k.write('set fmri(evg'+str(i)+'.2) '+unappEDxRate+'\n')
				l.write('set fmri(evg'+str(i)+'.4) '+BMIintercept+'\n')
				m.write('set fmri(evg'+str(i)+'.5) '+BMIslope+'\n')
				n.write('set frmi(evg'+str(i)+'.6) '+interactionapp+'\n')
				o.write('set frmi(evg'+str(i)+'.6) '+interactionunapp+'\n')  
g.close()
h.close()
