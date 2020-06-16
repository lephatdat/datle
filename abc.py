import csv         #library used for reading and parsing data from CSV file 
import requests    #library used for making REST API calls

#ignore specific warnings
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

#initialize variables with needed info for input file and to make NSX REST API call
nsx_username = "nsxadmin"
nsx_password = "notMyPassword!"
nsx_url = "https://10.100.1.72/api/2.0/services/securitygroup/bulk/globalroot-0"
csv_filename = "security_groups.csv"
myheaders={'content-type':'application/xml'}


try:
    csv_file = open(cv_filename)        #open CSV file for reading
except FileNotFoundError as e:
    print ("Input CSV file not found!")
    
try:   
    csv_data = csv.reader(csv_file)     #get reader object to iterate over lines in CSV file
except IOError as e:
    print ("Error reading CSV file!")

for security_group in cv_data:          #loop through parsed lines read in from CSV file
    #print security_group[0]    #uncomment for debugging - contains Security Group name
    #print security_group[1]    #uncomment for debugging - contains Security Group word to match in VM name

    #create XML payload with Security Group data read in from CSV file
    payload ='''    
    <securitygroup>
      <objectId>securitygroup-1</objectId>
      <objectTypeName>SecurityGroup</objectTypeName>
      <vsmUuid>422B2F08-25CF-AE4D-D78E-9450BA33618F</vsmUuid>
      <nodeId>d4fa9b9f-7973-4971-9ae6-c8f7e693ab30</nodeId>
      <revision>1</revision>
      <type>
        <typeName>SecurityGroup</typeName>
      </type>
      <name>''' +  security_group[0] +  '''</name>
      <description>
      </description>
      <scope>
        <id>globalroot-0</id>
        <objectTypeName>GlobalRoot</objectTypeName>
        <name>Global</name>
      </scope>
      <clientHandle>
      </clientHandle>
      <extendedAttributes/>
      <isUniversal>false</isUniversal>
      <universalRevision>0</universalRevision>
      <inheritanceAllowed>false</inheritanceAllowed>
      <dynamicMemberDefinition>
        <dynamicSet>
          <operator>OR</operator>
          <dynamicCriteria>
            <operator>OR</operator>
            <key>VM.NAME</key>
            <criteria>contains</criteria>
            <value>''' +  security_group[1] +  '''</value>
            <isValid>true</isValid>
          </dynamicCriteria>
        </dynamicSet>
      </dynamicMemberDefinition>
    </securitygroup>'''
    
    #print payload    #uncomment this for debugging - payload for REST API request call
    
    #call NSX REST API to create Security Group with XML payload just created
    try:
        response = requests.post(nsx_url, data=payload, headers=myheaders, auth=(nsx_username,nsx_password), verify=False)
    except requests.exceptions.ConnectionError as e:
        print ("Connection error!")
        
    print (response.text)