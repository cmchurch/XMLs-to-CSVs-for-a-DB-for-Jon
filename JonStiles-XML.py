# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from xml.etree import ElementTree

# <codecell>

def getAward(l):
    rootpath="./Award/"
    for x,path in enumerate(l):
        node = tree.find(rootpath+path)
        value = node.text
        if value is None:
            award.write("")
        elif path in textInt:
            award.write(str(value))
        else:
            award.write('"'+str(value)+'"')
        if x < (len(l)-1):
            award.write(",")
        else:
            award.write("\n")

# <codecell>

def getInvestigators(l):
    rootpath="./Award/Investigator"
    for i in tree.findall(rootpath):
        investigators.write(str(tree.find("./Award/AwardID").text)+',')
        for x,tag in enumerate(l):
            investigators.write('"'+str(i.find(tag).text)+'"')
            if x < (len(l)-1):
                investigators.write(",")
            else:
                investigators.write("\n")

# <codecell>

aHeaders = '"AwardID","AwardTitle","AwardEffectiveDate","AwardExpirationDate","AwardAmount","AwardInstrument","OrganizationCode","OrganizationDirectorate","OrganizationDivision","ProgramOfficer","AbstractNarration","MindAmdLetterDate","MaxAmdLetterDate","ARRAAmount","InstitutionName","InstitutionCityName","InstitutionZipCode","InstitutionPhoneNum","InstitutionStreetAddress","InstitutionCountryName","InstitutionStateName","InstitutionStateCode","ProgramElementCode","ProgramElementText","ProgramReferenceCode","ProgramReferenceText"\n'
aTags = [ 'AwardID',
          'AwardTitle',
          'AwardEffectiveDate',
          'AwardExpirationDate',
          'AwardAmount',
          'AwardInstrument/Value',
          'Organization/Code',
          'Organization/Directorate/LongName',
          'Organization/Division/LongName',
          'ProgramOfficer/SignBlockName',
          'AbstractNarration',
          'MinAmdLetterDate',
          'MaxAmdLetterDate',
          'ARRAAmount',
          'Institution/Name',
          'Institution/CityName',
          'Institution/ZipCode',
          'Institution/PhoneNumber',
          'Institution/StreetAddress',
          'Institution/CountryName',
          'Institution/StateName',
          'Institution/StateCode',
          'ProgramElement/Code',
          'ProgramElement/Text',
          'ProgramReference/Code',
          'ProgramReference/Text' ]

textInt = ['AwardAmount', 'Organization/Code', 'ARRAAmount','AwardID','ProgramElement/Code','ProgramReference/Code', 'Institution/ZipCode', 'Institution/StateCode']

iHeaders = '"AwardID","FirstName","LastName","EmailAddress","StartDate","EndDate","RoleCode"\n'
iTags = [ 'FirstName',
          'LastName',
          'EmailAddress',
          'StartDate',
          'EndDate',
          'RoleCode' ] 

# <codecell>

import os #allows for path crawling

#variables
path="C:/Users/Church/Desktop/jon-xml/" #set the path that we are going to read through
award = open(path+"award.csv","w")
investigators = open(path+"investigators.csv","w")

award.write(aHeaders)
investigators.write(iHeaders)

for root,dirs,files in os.walk(path):
    for file in files:
        if file.endswith('.xml'):
            with open(path+file, 'rt') as f:
                tree = ElementTree.parse(f)
                getAward(aTags)
                getInvestigators(iTags)
award.close()
investigators.close()


