import os

from django.shortcuts import render, redirect
import json
from parsing_json.models import DataRowModel
from parsing_json.forms import DataRowForm


# Create your views here.

# index view
def parsing_json(request):
    if request.POST and request.FILES:
        # upload file in upload folder
        file = handle_uploaded_file(request.FILES['file'], str(request.FILES['file']))
        # open json file from upload folder
        with open(file) as data_file:
            data = json.load(data_file)
        # load data from json file
        list = data['data']
        # add data in database
        for row in list:
            row_data = DataRowForm().save(commit=False)
            row_data.region = row['Область']
            row_data.city = row['Город']
            row_data.value = row['Значение']
            row_data.save()
        # load graph
        return redirect('/graph/')

    return render(request, 'index.html')


# upload and save file in folder
def handle_uploaded_file(file, filename):
    if not os.path.exists('upload/'):
        os.mkdir('upload/')

    with open('upload/' + filename, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    # return file destination
    return destination.name


# graph view
def graph(request, region="Киевская"):
    regions = DataRowModel.objects.values('region').distinct()
    citys = DataRowModel.objects.filter(region=region)
    context = {
        "regions": regions,
        "region": region,
        "citys": citys,
    }
    return render(request, 'graph.html', context)


# delete data from database
def delete_data(request):
    DataRowModel.objects.all().delete()
    return redirect('/')
