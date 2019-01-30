from rest_framework import generics, status, permissions
from rest_framework.response import Response
import csv, requests
import xml.etree.ElementTree as ET

from .models import Data

from .serializers import DataSerializer

xml_url = 'http://feeds.spotahome.com/trovit-Ireland.xml'
xml_file = 'data.xml'

def loadRSS():
    resp = requests.get(xml_url)
    with open(xml_file, 'wb') as f:
        f.write(resp.content)

def validate_input_data(data):
    if not isinstance(data['id_num'], str) :
        return False
    if not isinstance(data['title'], str):
        return False
    if not isinstance(data['link'], str):
        return False
    if not isinstance(data['city'], str):
        return False
    if not isinstance(data['main_image'], str):
        return False
    return True

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()

    instances = []

    for item in root.findall('ad'):
        data = {}

        # If the data is corrupted, we skip this data point.
        try:
            data['id_num'] = item.findall('id')[0].text
            data['link'] = item.findall('url')[0].text
            data['title'] = item.findall('title')[0].text
            data['city'] = item.findall('city')[0].text

            child = item.findall('pictures')[0]
            data['main_image'] = child.findall('picture')[0].findall('picture_url')[0].text
        except:
            continue

        # Validate that the columns have the correct data type entering into them.
        if validate_input_data(data):
            instances.append(data)

    return instances

def delete_existing_backend_instances():
    Data.objects.all().delete()

def create_new_backend_instances(instances):
    for instance in instances:
        temp = Data(
            id_num=instance['id_num'],
            title=instance['title'],
            link=instance['link'],
            city=instance['city'],
            main_image=instance['main_image'])
        temp.save()

class RefreshData(generics.ListAPIView):
    model = Data
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_queryset(self, *args, **kwargs):
        delete_existing_backend_instances()
        loadRSS()
        data_instances = parseXML(xml_file)
        create_new_backend_instances(data_instances)

        queryset = super(RefreshData, self).get_queryset()
        return queryset

class DataList(generics.ListAPIView):
    model = Data
    queryset = Data.objects.all()
    serializer_class = DataSerializer
