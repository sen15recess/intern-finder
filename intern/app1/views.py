from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from .scrape import search
from pws import Google
from bs4 import BeautifulSoup
import requests
import re
# Create your views here.

def home(request):
	template_path='app1/home.html'
	context={}
	return render(request,template_path,context)

def init_login(request):
	template_path='app1/signin.html'
	context={}
	return render(request,template_path,context)

def login_view(request):

	username = request.POST['username']
	password = request.POST['password']
	user = auth.authenticate(username= username ,password=password)
	if user is not None and user.is_active:
		auth.login(request,user)
		#search()
		template_path='app1/options.html'
		context = {}
		return render(request,template_path,context)
		return HttpResponse("Successfully Logged In")
	else:
		template_path='app1/invalid.html'
		context = {}
		return render(request,template_path,context)
def logout_view(request):
	auth.logout(request)
	return HttpResponse("Logout successful")

def register(request):
	template_path='app1/register.html'
	context = {}
	return render(request,template_path,context)

def register_view(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email= request.POST.get('email')
		password = request.POST.get('password')
		user = User.objects.create_user(username,email,password)
		user.save()
		return HttpResponseRedirect(reverse('init_login',args=[]))
	template_path='app1/register.html'
	context = {}
	return render(request,template_path,context)

def search_se(request):
    url = (Google.search(query='software engineering internships', num=30, start=0, country_code="es"))
    urls = url['url']
    r = requests.get(urls)
    plain_text = r.text
    soup = BeautifulSoup(plain_text,"lxml")
    pattern = re.compile(r"<h3 class=\"r\"><a.*?>(.*?)</a></h3>")
    string=str(pattern)
    match_pattern = re.findall(pattern,plain_text)
    '''for link in match_pattern:  # printing the titles from the above pattern
        print(link)'''
    links=[]
    MAPPING = { 
    	    '%3D': '=',
    	    '%3F': '?',
    	    '%2B': '+',
    	    '%23': '#',
    	}
     
    for i in soup.findAll("a"):  # printing the links
        href = i.get("href")
        if re.search("google|youtube",href):
            pass
        else:
            if re.search("http",href):
                k = re.search("http",href)
                rough = (href[k.start():])
                rough = re.sub('%3D',MAPPING['%3D'],rough)
                rough = re.sub('%3F',MAPPING['%3F'],rough)
                rough = re.sub('%2B',MAPPING['%2B'],rough)
                rough = re.sub('%23',MAPPING['%23'],rough)
                m = re.search("&",rough)
                if m == None:
                    links.append(rough)
                    print(rough)
                else:
                    links.append(rough[:m.start()])
                    print(rough[:m.start()])
    
    data_store = {}
    
    for i in range(len(links)):
        nm = re.search(r'\..*\.',links[i])
        if nm == None :
            name = links[i]
        else:
            name = links[i][nm.start():nm.end()]
        name = re.sub('\.','',name)
        val = []
        val.append(name)
        val.append(links[i])
        data_store[i+1] = val
    template_path='app1/result.html'
    context={}
    return render(request,template_path,context)

def search_elec(request):
    url = (Google.search(query='electrical engineering internships', num=30, start=0, country_code="es"))
    urls = url['url']
    r = requests.get(urls)
    plain_text = r.text
    soup = BeautifulSoup(plain_text,"lxml")
    pattern = re.compile(r"<h3 class=\"r\"><a.*?>(.*?)</a></h3>")
    string=str(pattern)
    match_pattern = re.findall(pattern,plain_text)
    '''for link in match_pattern:  # printing the titles from the above pattern
        print(link)'''
    links=[]
    MAPPING = { 
    	    '%3D': '=',
    	    '%3F': '?',
    	    '%2B': '+',
    	    '%23': '#',
    	}
     
    for i in soup.findAll("a"):  # printing the links
        href = i.get("href")
        if re.search("google|youtube",href):
            pass
        else:
            if re.search("http",href):
                k = re.search("http",href)
                rough = (href[k.start():])
                rough = re.sub('%3D',MAPPING['%3D'],rough)
                rough = re.sub('%3F',MAPPING['%3F'],rough)
                rough = re.sub('%2B',MAPPING['%2B'],rough)
                rough = re.sub('%23',MAPPING['%23'],rough)
                m = re.search("&",rough)
                if m == None:
                    links.append(rough)
                    print(rough)
                else:
                    links.append(rough[:m.start()])
                    print(rough[:m.start()])
    
    data_store = {}
    
    for i in range(len(links)):
        nm = re.search(r'\..*\.',links[i])
        if nm == None :
            name = links[i]
        else:
            name = links[i][nm.start():nm.end()]
        name = re.sub('\.','',name)
        val = []
        val.append(name)
        val.append(links[i])
        data_store[i+1] = val
    template_path='app1/result.html'
    context={}
    return render(request,template_path,context)
        
def search_man(request):
    url = (Google.search(query='management internships', num=30, start=0, country_code="es"))
    urls = url['url']
    r = requests.get(urls)
    plain_text = r.text
    soup = BeautifulSoup(plain_text,"lxml")
    pattern = re.compile(r"<h3 class=\"r\"><a.*?>(.*?)</a></h3>")
    string=str(pattern)
    match_pattern = re.findall(pattern,plain_text)
    '''for link in match_pattern:  # printing the titles from the above pattern
        print(link)'''
    links=[]
    MAPPING = { 
    	    '%3D': '=',
    	    '%3F': '?',
    	    '%2B': '+',
    	    '%23': '#',
    	}
     
    for i in soup.findAll("a"):  # printing the links
        href = i.get("href")
        if re.search("google|youtube",href):
            pass
        else:
            if re.search("http",href):
                k = re.search("http",href)
                rough = (href[k.start():])
                rough = re.sub('%3D',MAPPING['%3D'],rough)
                rough = re.sub('%3F',MAPPING['%3F'],rough)
                rough = re.sub('%2B',MAPPING['%2B'],rough)
                rough = re.sub('%23',MAPPING['%23'],rough)
                m = re.search("&",rough)
                if m == None:
                    links.append(rough)
                    print(rough)
                else:
                    links.append(rough[:m.start()])
                    print(rough[:m.start()])
    
    data_store = {}
    
    for i in range(len(links)):
        nm = re.search(r'\..*\.',links[i])
        if nm == None :
            name = links[i]
        else:
            name = links[i][nm.start():nm.end()]
        name = re.sub('\.','',name)
        val = []
        val.append(name)
        val.append(links[i])
        data_store[i+1] = val
    template_path='app1/result.html'
    context={}
    return render(request,template_path,context)