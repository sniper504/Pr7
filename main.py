import json
import pandas as pd
file = open("sw_templates.json", 'r')
data = json.load(file)
data["access+trunk"] = ["switchport mode access",#создается ключ и записывется в конце
    'switchport access vlan',
  'switchport nonegotiate',
  'spanning-tree portfast',
  'spanning-tree bpduguard enable' 'switchport trunk encapsulation dot1q',
'switchport mode trunk',
'switchport trunk native vlan 999',
'switchport trunk allowed vlan']

file.close()
file = open("sw_templates.json", 'w')
json.dump(data,file,sort_keys=True,indent=2)
file.close()


df=pd.read_csv("filename.csv")
df['square']#вывод столбца
df.iloc[0]#вывод строки