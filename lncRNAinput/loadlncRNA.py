# import urllib 

# Files = [
# 'RF00635','RF01778','RF01800','RF01871','RF01872','RF01873','RF01874','RF01875','RF01876','RF01877','RF01879','RF01880','RF01881','RF01882','RF01883','RF01884','RF01885','RF01886','RF01887','RF01888','RF01889','RF01890','RF01891','RF01892','RF01894','RF01904','RF01905','RF01906','RF01909','RF01928','RF01929','RF01930','RF01931','RF01932','RF01933','RF01934','RF01935','RF01946','RF01947','RF01948','RF01950','RF01951','RF01952','RF01953','RF01954','RF01955','RF01956','RF01957','RF01962','RF01963','RF01964','RF01965','RF01966','RF01967','RF01968','RF01969','RF01970','RF01971','RF01972','RF01973','RF01974','RF01975','RF01976','RF01977','RF01978','RF01979','RF01981','RF01983','RF01984','RF01985','RF01986','RF01987','RF01992','RF02038','RF02039','RF02040','RF02041','RF02042','RF02043','RF02044','RF02045','RF02046','RF02047','RF02085','RF02086','RF02087','RF02089','RF02090','RF02091','RF02098','RF02101','RF02102','RF02103','RF02104','RF02105','RF02106','RF02107','RF02108','RF02109','RF02110','RF02112','RF02113','RF02114','RF02115','RF02116','RF02117','RF02118','RF02119','RF02120','RF02121','RF02122','RF02123','RF02124','RF02125','RF02126','RF02127','RF02128','RF02129','RF02130','RF02131','RF02132','RF02133','RF02134','RF02135','RF02136','RF02137','RF02138','RF02139','RF02140','RF02141','RF02142','RF02143','RF02145','RF02146','RF02147','RF02148','RF02149','RF02150','RF02151','RF02153','RF02154','RF02155','RF02156','RF02157','RF02158','RF02159','RF02160','RF02161','RF02164','RF02165','RF02166','RF02167','RF02168','RF02169','RF02170','RF02171','RF02172','RF02173','RF02174','RF02175','RF02176','RF02177','RF02178','RF02179','RF02180','RF02181','RF02182','RF02183','RF02184','RF02185','RF02186','RF02187','RF02188','RF02189','RF02190','RF02191','RF02192','RF02193','RF02195','RF02196','RF02197','RF02198','RF02199','RF02200','RF02201','RF02202','RF02203','RF02204','RF02205','RF02206','RF02207','RF02208','RF02209','RF02210','RF02211','RF02212','RF02213','RF02215','RF02216','RF02217','RF02218','RF02219','RF02220','RF02246','RF02247','RF02248','RF02249','RF02250','RF02251','RF02252','RF02255','RF02256','RF02257','RF02258','RF02259','RF02267','RF02272',]
# for each in Files:
# 	filename = each + '.fa.gz'
# 	a = urllib.urlretrieve('ftp://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/', filename)
# 	print a

import shutil
import urllib2
from contextlib import closing


Files = [
'RF00635','RF01778','RF01800','RF01871','RF01872','RF01873','RF01874','RF01875','RF01876','RF01877','RF01879','RF01880','RF01881','RF01882','RF01883','RF01884','RF01885','RF01886','RF01887','RF01888','RF01889','RF01890','RF01891','RF01892','RF01894','RF01904','RF01905','RF01906','RF01909','RF01928','RF01929','RF01930','RF01931','RF01932','RF01933','RF01934','RF01935','RF01946','RF01947','RF01948','RF01950','RF01951','RF01952','RF01953','RF01954','RF01955','RF01956','RF01957','RF01962','RF01963','RF01964','RF01965','RF01966','RF01967','RF01968','RF01969','RF01970','RF01971','RF01972','RF01973','RF01974','RF01975','RF01976','RF01977','RF01978','RF01979','RF01981','RF01983','RF01984','RF01985','RF01986','RF01987','RF01992','RF02038','RF02039','RF02040','RF02041','RF02042','RF02043','RF02044','RF02045','RF02046','RF02047','RF02085','RF02086','RF02087','RF02089','RF02090','RF02091','RF02098','RF02101','RF02102','RF02103','RF02104','RF02105','RF02106','RF02107','RF02108','RF02109','RF02110','RF02112','RF02113','RF02114','RF02115','RF02116','RF02117','RF02118','RF02119','RF02120','RF02121','RF02122','RF02123','RF02124','RF02125','RF02126','RF02127','RF02128','RF02129','RF02130','RF02131','RF02132','RF02133','RF02134','RF02135','RF02136','RF02137','RF02138','RF02139','RF02140','RF02141','RF02142','RF02143','RF02145','RF02146','RF02147','RF02148','RF02149','RF02150','RF02151','RF02153','RF02154','RF02155','RF02156','RF02157','RF02158','RF02159','RF02160','RF02161','RF02164','RF02165','RF02166','RF02167','RF02168','RF02169','RF02170','RF02171','RF02172','RF02173','RF02174','RF02175','RF02176','RF02177','RF02178','RF02179','RF02180','RF02181','RF02182','RF02183','RF02184','RF02185','RF02186','RF02187','RF02188','RF02189','RF02190','RF02191','RF02192','RF02193','RF02195','RF02196','RF02197','RF02198','RF02199','RF02200','RF02201','RF02202','RF02203','RF02204','RF02205','RF02206','RF02207','RF02208','RF02209','RF02210','RF02211','RF02212','RF02213','RF02215','RF02216','RF02217','RF02218','RF02219','RF02220','RF02246','RF02247','RF02248','RF02249','RF02250','RF02251','RF02252','RF02255','RF02256','RF02257','RF02258','RF02259','RF02267','RF02272',]
for each in Files:
	with closing(urllib2.urlopen('ftp://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/fasta_files/'+each+'.fa.gz')) as r:
		with open(each+'.fa.gz', 'wb') as f:
			shutil.copyfileobj(r, f)
			print each