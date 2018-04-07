# from urllib import request
# import json
# import requests
# f = request.urlopen('https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json')
# dat = f.read().decode('UTF-8')
# print('Status:', f.status, f.reason)
# print('headers:', f.getheaders())
# print('dat:', dat)
# jsonDate = json.dumps(dat)
# print(type(jsonDate))

# reaqones = requests.get("www.qq.com");
# reaqones.encoding = "utf-8"
# print(reaqones.text);

from xml.etree import ElementTree as ET
# 直接解析xml文件
tree = ET.parse("../pythonDay2/dataXml.xml")

# 获取xml文件的根节点
root = tree.getroot()
print(root)
# for node in root:
    # print("nodeYear:" + node.find('year').text)
    # print("nodeRank:" + node.find('rank').text)
    # print("nodeGdppc:" + node.find('gdppc').text)
    # print("nodeNeighbor:" + node.attrib.find('direction'))
# for node in root:
#     for node_node in node:
#         print(node_node)
#         print(node_node.find('rank').text)
# 获取xml文件的根节点

# 顶层标签
print(dict(root))

# 遍历XML中所有的year节点
for node in root.iter('year'):
    # 节点的标签名称和内容
    print(node.tag, node.text)
