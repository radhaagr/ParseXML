
# coding: utf-8

# In[130]:


import os
d='.'
y = [filter(lambda x: os.path.isdir(os.path.join(d, x)), os.listdir(d))]


# In[131]:


d = 'D:/dranziera_protocol/'

alldir = [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]


# In[132]:


#print (alldir)


# In[133]:


allfiles = []
for mypath in alldir:
    curfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
    allfiles.extend(curfiles)


# In[137]:


print (allfiles)


# In[138]:


import xml.etree.ElementTree as ET


# In[139]:


from lxml import etree

utf8_parser = etree.XMLParser(encoding='utf-8', recover=True)

with open("D:/dranziera_protocol/OnlyText.txt",'w',encoding = 'utf-8') as ftext, open("D:/dranziera_protocol/polarity.txt",'w',encoding = 'utf-8') as flabel:
    for file in allfiles:
        root = etree.parse(file, parser=utf8_parser)
        for neighbor in root.iter('sentence'):
            textdata = neighbor.find('text').text
            #print (textdata.strip())
            ftext.write(textdata.strip()+"\n")
            polaritydata = neighbor.find('polarity').text
            flabel.write(polaritydata + "\n")


# In[ ]:


"""from lxml import etree

utf8_parser = etree.XMLParser(encoding='utf-8', recover=True)

with open("D:/dranziera_protocol/textdata.txt",'w',encoding = 'utf-8') as f, open("D:/dranziera_protocol/polarity.txt",'w',encoding = 'utf-8') as flabel:
    for file in allfiles:
        root = etree.parse(file, parser=utf8_parser)
        for neighbor in root.iter('sentence'):
        #print(neighbor.attrib)
            textdata = neighbor.find('text').text
            f.write(textdata)
            polaritydata = neighbor.find('polarity').text
            flabel.write(polaritydata)
            f.write("\n")
            flabel.write("\n")"""


