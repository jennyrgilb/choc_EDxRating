import os
import fnmatch
import glob
import subprocess
# /projects/niblab/data/eric_data/W1/imagine
# cope6 = app 
# cope8 = unapp
basedir='/projects/niblab/data/eric_data/W1/imagine'
f=open('clusterize_app.sh','w')
g=open('output_img_app.txt','w')
os.chdir(basedir)
for file in glob.glob('level3_appEDxRate_randomised_tfce_corrp_tstat*.nii.gz'):
	INPUT=os.path.join(basedir,file)
	print(INPUT)
	name=INPUT.split('/')
	#print(name)    
	name2=name[6].strip('.nii.gz')
	print(name2)
	g.write(name2+'\n')
	OUTPUT=os.path.join(basedir, name2)
	call='/projects/niblab/modules/software/fsl/5.0.10/bin/cluster -i '+INPUT+' -t 0.95 '+'-o '+OUTPUT+'_cluster  --scalarname="1-p" > '+OUTPUT+'_info.txt'
	f.write('%s\n' % (call,))
	cluster=subprocess.Popen(["/projects/niblab/modules/software/fsl/5.0.10/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
	output=cluster.stdout.read()
	print output
	g.write(output+'\n')
f.close()
g.close()
