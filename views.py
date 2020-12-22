from django.shortcuts import render
import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "6755de5c6dmsh5a66fd6124077c3p1a807ajsn3c85ac7bd0d9",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

def helloworldview(request):
    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):

        mylist.append(response['response'][x]['country'])
    if request.method == "POST":
       selectedcountry = request.POST['selectedcountry']
       noofresults = int(response['results'])
       for x in range(0,noofresults):
            if selectedcountry == response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered =response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) -int(recovered)
       context = {'selectedcountry' : selectedcountry,'mylist' : mylist,'new' : new,'active' : active,'critical' : critical,'recovered' : recovered,'deaths' : deaths,'total' : total}
       return render(request,'helloworld.html',context)

    noofresults = int(response['results'])
    mylist = []
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])
    context = {'mylist' : mylist}
    return render(request,'helloworld.html', context)
