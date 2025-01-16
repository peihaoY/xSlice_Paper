import matplotlib.pyplot as plt
data = []

with open('KPM_UE.txt', 'r') as file:
    for line in file:
        line_data = [float(x) for x in line.split()]
        if line_data[0] == 1:
            data.append(line_data)

# for line_data in data:
#    print(line_data)

'''ue_id, DRB_pdcpSduVolumeDL, DRB_pdcpSduVolumeUL, DRB_RlcSduDelayDL, DRB_UEThpDL, DRB_UEThpUL, RRU_PrbTotDL, RRU_PrbTotUL '''
DRB_RlcSduDelayDL = [row[3]/1000 for row in data]
DRB_UEThpDL = [row[4]/1000 for row in data]
DRB_UEThpUL = [row[5]/1000 for row in data]
RRU_PrbTotDL = [row[6]/100 for row in data]
'''RRU_PrbTotUL, RRU_PrbTotUL, DRB_UEThpUL, DRB_UEThpDL, DRB_RlcSduDelayDL,
        DRB_pdcpSduVolumeUL, DRB_pdcpSduVolumeDL'''
#RB_data1 = [row[3] for row in data][::-1]
#print(DRB_UEThpDL)

plt.figure()
plt.plot(DRB_UEThpDL, label='DLThp')
plt.xlabel('Time/s')
plt.title('DRB.DRB_UEThp')
plt.ylabel('Mbps')
plt.legend()
plt.show()

plt.figure()
plt.plot(DRB_RlcSduDelayDL, label='DLDelay')
plt.xlabel('Time/s')
plt.title('DRB.RlcSduDelayDL')
plt.ylabel('ms')
plt.legend()
plt.show()

plt.figure()
plt.plot(RRU_PrbTotDL, label='DL_rbs')
plt.xlabel('Time/s')
plt.title('RRU_PrbTotDL')
plt.ylabel('RBs number')
plt.legend()
plt.show()


