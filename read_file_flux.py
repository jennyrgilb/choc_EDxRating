import os
import glob
import sys
import fnmatch

basedir='/projects/niblab/data/eric_data/design_files/imagine'

ev_name='/projects/niblab/scripts/choc_EDxRating/evs_flux.txt'

#this file has the columns for the mat file
#0 is input
#1 is mean
#2 is weight gain prone group (high app ED, low unapp ED)
#3 is weight gain protected group (low app ED, high unapp ED)
#4 is the BMI intercept
#5 is the interaction of BMI slope in the prone group
#6 is the interaction of BMI slope in the protected group

g=open('input.txt','w')
h=open('mean.txt','w')
j=open('prone_cov.txt','w')
k=open('protect_cov.txt','w')
l=open('BMIinterceptflux_cov.txt','w')
m=open('BMIslope_prone_cov.txt','w')
n=open('BMIslope_protect_cov.txt','w')
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
			prone = line2[2]
			prone = prone.strip('\n')
			protect = line2[3]
			protect = protect.strip('\n')
			BMIintercept = line2[4]
			BMIintercept = BMIintercept.strip('\n')
			BMIslope_prone = line2[4]
                        BMIslope_prone = BMIslope_prone.strip('\n')
                        BMIslope_protect = line2[5]
                        BMIslope_protect = BMIslope_protect.strip('\n')
#			print(name2+' is '+prone+' for prone group ,and is '+protect+' for protect group, and a BMI slope of '+BMIslope+')
			if fnmatch.fnmatch(name2, sub):
#				print('THIS IS THE SUBJECT'+name2)
#				print(sub)
#				print(line2)
				i=i+1
				print('set feat_files('+str(i)+') '+'"'+dir+'/COPE.feat"')
				g.write('set feat_files('+str(i)+') '+'"/projects/niblab/data/eric_data/W1/imagine/level1_grace_edit/'+name2+'++.feat"'+'\n')
				h.write('set fmri(evg'+str(i)+'.1) '+mean+'\n')  
				j.write('set fmri(evg'+str(i)+'.2) '+prone+'\n')  
				k.write('set fmri(evg'+str(i)+'.3) '+protect+'\n')
				l.write('set fmri(evg'+str(i)+'.4) '+BMIintercept+'\n')  
				m.write('set fmri(evg'+str(i)+'.5) '+BMIslope_prone+'\n')
				n.write('set fmri(evg'+str(i)+'.6) '+BMIslope_protect+'\n')
g.close()
h.close()
j.close()
k.close()
l.close()
m.close()
n.close()
