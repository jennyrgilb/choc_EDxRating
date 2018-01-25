import os
import fnmatch
import glob
import subprocess
# /projects/niblab/data/eric_data/W1/gng/level3_grace_edit/randomised
# cope10_randomized_tfce_corrp_tstat1.nii.gz
basedir='/projects/niblab/data/eric_data/W1/imagine'
f=open('clusterize.sh','w')
g=open('output_img.txt','w')
os.chdir(basedir)
for file in glob.glob('level3_grace_edit/level3_thr.gfeat/cope*.gfeat/stats/zstat1.nii.gz'):
	INPUT=os.path.join(basedir,file)
	print(INPUT)
	name=INPUT.split('/')
	#print(name)    
	name2=name[10].strip('.nii.gz')
	print(name2)
	g.write(name2+'\n')
	OUTPUT=os.path.join(basedir,'level3_grace_edit', name2)
	call='/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster -i '+INPUT+' -t 0.95 '+'-o '+OUTPUT+'_cluster  --scalarname="1-p" > '+OUTPUT+'_info.txt'
	f.write('%s\n' % (call,))
	cluster=subprocess.Popen(["/usr/share/Modules/software/RHEL-6.5/fsl/5.0.9/bin/cluster","-i",INPUT,"-t","3","-o",OUTPUT+"_cluster"],stdout=subprocess.PIPE)
	output=cluster.stdout.read()
	print output
	g.write(output+'\n')
f.close()
g.close()
