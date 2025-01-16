import sqlite3
import numpy as np

conn = sqlite3.connect('xapp_db_')
cursor = conn.cursor()

''' wb_cqi INT  CHECK(wb_cqi >= 0 AND wb_cqi < 256 ),
dl_mcs1 INT  CHECK(dl_mcs1>= 0 AND dl_mcs1 < 256),
ul_mcs1  INT CHECK(ul_mcs1 >=  0 AND ul_mcs1 < 256),
dl_mcs2  INT CHECK(dl_mcs2 >= 0 AND dl_mcs2 < 256),
ul_mcs2 INT CHECK(ul_mcs2 >= 0 AND ul_mcs2 < 256),
phr INT CHECK(phr > -24 AND  phr < 41),
bsr INT CHECK(bsr >= 0 AND  bsr < 4294967296),
dl_bler REAL CHECK(dl_bler  >= 0 AND dl_bler < 4294967296),
ul_bler REAL CHECK(ul_bler  >= 0 AND ul_bler < 4294967296)'''

'''dl_sched_rb,ul_sched_rb,pusch_snr,pucch_snr,dl_aggr_prb,ul_aggr_prb,
   wb_cqi,phr,bsr, dl_bler, ul_bler, dl_mcs1, ul_mcs1 '''

#rnti

cursor.execute("SELECT * FROM MAC_UE limit 1")  #WHERE rnti = 2
dl_bler = cursor.fetchall()
print(dl_bler)

'''
new_cqi = []  #3&4 的公倍数是12，求12个数的平均数可以
for i in range(0, len(dl_bler), 1):
    if i + 0 < len(dl_bler):
        avg = np.mean(dl_bler[i:i+1])
        new_cqi.append(avg)'''

'''cursor.execute("SELECT phr FROM MAC_UE WHERE rnti = 1")
ul_bler = cursor.fetchall()'''

'''
new_phr = []
for i in range(0, len(ul_bler), 1):
    if i + 0 < len(ul_bler):
        avg = np.mean(ul_bler[i:i+1])
        new_phr.append(avg)'''

cursor.execute("SELECT pusch_snr FROM MAC_UE ") #WHERE rnti = 1
pusch_snr = cursor.fetchall()
cursor.execute("SELECT pucch_snr FROM MAC_UE ") #WHERE rnti = 1
pucch_snr = cursor.fetchall()
cursor.execute("SELECT wb_cqi FROM MAC_UE")   #WHERE rnti = 1
wb_cqi = cursor.fetchall()
cursor.execute("SELECT phr FROM MAC_UE ")#WHERE rnti = 1
phr = cursor.fetchall()
cursor.execute("SELECT dl_mcs1 FROM MAC_UE")   #WHERE rnti = 1
dl_mcs1 = cursor.fetchall()
cursor.execute("SELECT ul_mcs1 FROM MAC_UE ")#WHERE rnti = 1
ul_mcs1 = cursor.fetchall()
cursor.execute("SELECT dl_bler FROM MAC_UE")   #WHERE rnti = 1
dl_bler = cursor.fetchall()
cursor.execute("SELECT ul_bler FROM MAC_UE ")#WHERE rnti = 1
ul_bler = cursor.fetchall()
length = len(ul_bler)
import matplotlib.pyplot as plt

'''
for i in range(26000, 28000):
    value = pusch_snr[i][0]
    if value > 40:
        pusch_snr[i] = (value - 20,)

for i in range(31000, 35000):
    value = pusch_snr[i][0]
    if value > 40:
        pusch_snr[i] = (value - 20,)
'''

x = np.arange(0, length, 1)
x = x/1000
plt.figure()
plt.subplot(511)
plt.plot(x, phr,linewidth=2)
plt.ylabel('PHR',fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.subplot(512)
plt.plot(x, wb_cqi,linewidth=2)
plt.ylabel('CQI',fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
#plt.gca().yaxis.set_major_locator(plt.MaxNLocator(integer=True))
plt.yticks([13, 15])
plt.subplot(513)
plt.plot(x, pusch_snr,linewidth=2)
plt.ylabel('PUSCH SNR',fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.subplot(514)
plt.plot(x, dl_mcs1,linewidth=2)
plt.ylabel('DL MCS',fontsize=16)
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.subplot(515)
plt.plot(x, dl_bler,linewidth=2)
plt.ylabel('DL BLER',fontsize=16)
plt.xlabel('Time/s',fontsize=16)
plt.tight_layout()
plt.tick_params(axis='x', labelsize=14)
plt.tick_params(axis='y', labelsize=14)
plt.show()



cursor.execute("SELECT ul_sched_rb FROM MAC_UE ") #WHERE rnti = 1
ul_sched_rb = cursor.fetchall()
cursor.execute("SELECT dl_sched_rb FROM MAC_UE ") #WHERE rnti = 1
dl_sched_rb = cursor.fetchall()

plt.figure()
plt.subplot(211)
plt.plot(ul_sched_rb)
#plt.ylim(0, 1.0)
plt.title('ul_sched_rb DL Plot')  #DL_BLER
plt.subplot(212)
plt.plot(dl_sched_rb)
plt.title('dl_sched_rb UL Plot')#UL_BLER
plt.xlabel('Time/ms')
#plt.ylabel('First Column Data')
plt.tight_layout()
plt.show()



conn.close()
