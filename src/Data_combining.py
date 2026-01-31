import pandas as pd  


df1 = pd.read_csv(r'Path_to\Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv')
df2 = pd.read_csv(r'Path_to\Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX.csv')
df3 = pd.read_csv(r'Path_to\Friday-WorkingHours-Morning.pcap_ISCX.csv')
df4 = pd.read_csv(r'Path_to\Monday-WorkingHours.pcap_ISCX.csv')
df5 = pd.read_csv(r'Path_to\Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX.csv')
df6 = pd.read_csv(r'Path_to\Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX.csv')
df7 = pd.read_csv(r'Path_to\Tuesday-WorkingHours.pcap_ISCX.csv')
df8 = pd.read_csv(r'Path_to\Wednesday-workingHours.pcap_ISCX.csv')


combined_df = pd.concat([df1,df2,df3,df4,df5,df6,df7,df8], axis= 0 , ignore_index=True )
print(combined_df.shape)
combined_df.to_csv("cic_ids2017_combined.csv", index=False)
