import logging
import os
import xml.etree.ElementTree as ET
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf
from polls.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from xml.dom import minidom
import json as simplejson
import xml.etree.cElementTree as ET
import re
from xml.etree import ElementTree
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, Comment, tostring, XML
import xml.dom.minidom
from django.views.decorators.csrf import csrf_protect

logger = logging.getLogger(__name__)



##############GLOBAL VARIABLES ################################################
PRODUCTS = 'Products\\'
CLASSES = 'Classes\\'
TEMPORARY = 'TEMPORARYFILE'
methods8 = 'Reset\n'
methods11 = 'Reset\n'
methods15 = 'Reset\n'
association8 = 'Public\nPreestablished\nManagement\nLocal Management\nLocal Reading\nLocal Pairing'
associationMethods8 = 'MNGT\npublic\npre'
association11 = 'Public\nPreestablished\nManagement\nLocal Management'
association15 = 'Public\nPreestablished\nManagement\nLocal Management\nLocal Reading\Local Pairing'


################FUNCTIONS ROUTINES############################################

@login_required(login_url="login/")
def home(request):
    return render(request, "home.html")



@csrf_protect
def register(request, template_name="register.html"):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = c['RegistrationForm'] = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                email=form.cleaned_data['email'],
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],

            )
            return HttpResponseRedirect('/success/')
    else:
        form = c['RegistrationForm'] = RegistrationForm()
    return render(request, template_name, {'form': c['RegistrationForm']}, c)

def register_success(request):
    return render(request, "home.html")


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


FileName = ''
tree = {}
def getName(request):
    """get file Name"""
    global FileName
    if request.method == "POST" and request.is_ajax():
        FileName = request.POST['id']
        status = display(FileName)
        return HttpResponse(str(status['fileContent']))
    else:
        status= {'fileContent': 'Fail Loading Content'}
        return HttpResponse(status)


@csrf_protect

def listtree(request, template_name="list.html", path=PRODUCTS):
    """show tree of dictionaries """
    def listtreefunction(path):
        """Browse the tree"""
        result = path.rpartition('\\')[2]
        tree = dict(name=result, children=[])
        try:
            lst = os.listdir(path)
        except OSError:
            pass
        else:
            for name in lst:
                fn = os.path.join(path, name)
                recent = name
                if os.path.isdir(fn):
                    tree['children'].append(listtreefunction(fn))
                else:
                    tree['children'].append(dict(name=recent))
        return tree
    global tree
    tree = listtreefunction(path)
    return render(request, template_name, {'tree': tree,})

def create(request, template_name="list.html"):
    """create XML file"""
    context = {'error': ''}
    if request.method == 'POST':
        if request.POST.__contains__('content'):
            xml_data = request.POST['content']
            tree = ET.fromstring(xml_data)
            DictionaryName = ''.join([literal.text for literal in tree.findall('.//description')])
            # DictionaryClass = ''.join([literal.text for literal in tree.findall('.//class')])
            DictionaryClass = 'X16_Enexis\\objects_dictionary'
            fileName = getNewFileName('\\'.join([DictionaryClass, DictionaryName]))
            writeFile(request.POST['content'], fileName, context)
        else:
            context['error'] += 'Dictionary empty.\n'
    else:
        context['error'] += 'Request type must be POST.\n'

    return listtree(request, template_name)



def getNewFileName(DictionaryPath):
    """get dictionary name (in creation event)"""
    fileName = str(DictionaryPath) + '.xml'
    return os.path.join(PRODUCTS, fileName)


def openFile(context, mode, fileName):
    try:
        fileHandler = open(fileName, mode)
        return {'opened': True, 'handler': fileHandler}
    except IOError:
        context['error'] += 'Unable to open file ' + fileName + '\n'
    except:
        context['error'] += 'Unexpected exception in openFile method.\n'
    return {'opened': False, 'handler': None}

def writeFile(content, fileName, context):
    fileHandler = openFile(context, 'w', fileName)
    if fileHandler['opened']:
        file = File(fileHandler['handler'])
        file.write(content)
        file.flush()
        file.close()


def display(FileName):
    """show xml file content """
    context = {'error': ''}
    readFile1(context, FileName, PRODUCTS)
    return context


def readFile1(context, fileName, pathFile=PRODUCTS):

    fileHandler = openFile1(context, 'r', fileName, pathFile)
    if fileHandler['opened']:
        file = File(fileHandler['handler'])
        readContent(file, context)
        file.close()


def openFile1(context, mode, fileName, filePath):
    Pathfile = os.path.join(filePath, fileName)
    try:
        fileHandler = open(Pathfile, mode)
        return {'opened': True, 'handler': fileHandler}
    except IOError:
        context['error'] += 'Unable to open file '+Pathfile+'\n'
    except:
        context['error'] += 'Unexpected exception in openFile method.\n'
    return {'opened': False, 'handler': None}

def readContent(file, context):
    context['fileContent'] = ''
    for chunk in file.chunks(10):
        context['fileContent'] += chunk


def parseXML(request):
    """parse xml file"""
    status = ""
    methods =''
    if request.method == "POST" and request.is_ajax():
        classId = request.POST['id']
        classsubItem = request.POST['name']
        dictionatyName = classId+'.xml'
        #############
        def getMethods(meth):
            count = 2
            methods = '1-'
            for letter in meth:
                methods += letter
                if letter == "\n":
                    methods += str(count) + '-'
                    count += 1
            return methods
        ##################
        if (str(classsubItem) == '8'):
            methods = getMethods(methods8)
            association = association8
            associationMethods = associationMethods8
        elif (str(classsubItem) == '11'):
            methods = getMethods(methods11)
            association = association11
        elif (str(classsubItem) == '15'):
            methods = getMethods(methods15)
            association = association15
        methods = methods[:-2]
        filePath = os.path.join('Classes', dictionatyName)
        doc = minidom.parse(filePath)
        dictClass = doc.getElementsByTagName('class')
        for dictClass1 in dictClass:
            dictId = dictClass1.getAttribute('id')
            dictVersion = dictClass1.getAttribute('version')
        name = doc.getElementsByTagName('description')[0]
        attrs = doc.getElementsByTagName('attributes')
        for attrs1 in attrs:
            attr = attrs1.getElementsByTagName('attribute')
            for attr1 in attr:
                sid = attr1.getAttribute('id')
                name = attr1.getAttribute('name')
                type = attr1.getAttribute('type')
                size = attr1.getAttribute('size')
                status += "{}- name:{}, type:{}, size:{}".format(sid, name, type, size)+"\n"
        return HttpResponse(simplejson.dumps({'stat': status, 'dictDescription': name, 'dictId': dictId, 'dictVersion': dictVersion, 'methods': methods, 'association': association, 'associationMethods': associationMethods}), content_type='application/json')


def createTemporary(request, template_name="list.html"):
    """create temporary files"""
    global idAttr
    associationList = association8.split('\n')
    if request.method == "POST" and request.is_ajax():
        idAttr = request.POST['idAttr']
        content = request.POST['checks']
        content = content.split('@')
        l = []
        for item in content:
            subl = []
            for subItem in item.split(':'):
                subl.append(subItem)
            l.append(subl)
        l.pop(0)

    top = Element('delimit')
    for item in associationList:
        ops = []
        for element in l:
            if item in element:
                ops.append(element[1])
        if  not ops:
            child = SubElement(top, 'association', name=item, operations='_')
        else:
            ops = '\\'.join(ops)
            child = SubElement(top, 'association', name=item, operations=ops)
    with open(TEMPORARY+'\\'+idAttr+'.xml', 'w') as f:
        el = xml.dom.minidom.parseString(tostring(top))
        pretty_xml_as_string = el.toprettyxml()
        f.write(pretty_xml_as_string.encode('UTF-8'))
    return listtree(request, template_name)

def generate(request):
    """add associates to attributes in XML file and generate final dictionary"""
    context = {'error': ''}
    if request.method == "POST" and request.is_ajax():
        product = request.POST['product']
        classNum = request.POST['classNum']
        # obisCode = request.POST['obisCode']
        # Description = request.POST['Description']
        # version = request.POST['version']
        # textareaContent2 = request.POST['textareaContent2']
        # textareaContent3 = request.POST['textareaContent3']
        #
        name = 'class_' + str(classNum) + '.xml'
        filePath ='Classes\\'+product
        l = os.listdir(TEMPORARY)
        if l != []:
            for file in l:
                context1 = {'error': ''}
                readFile1(context1, str(file), TEMPORARY)
                classBefore = context1['fileContent']
                readFile1(context, name, filePath)
                classAfter = context['fileContent']
                res = ET.fromstring(classAfter)
                for attrs in res.findall('attributes'):
                    for attr in attrs.findall('attribute'):
                        idAttr = int(attr.get('id'))
                        if idAttr == int(file[0]):
                            attr.append((ET.fromstring(classBefore)))
                            filename = filePath+'\\'+name
                            writeFile(tostring(res), filename, context)
                            os.remove(TEMPORARY+'\\'+file)
                for meths in res.findall('methods'):
                    logger.info('kk')
                    idMeth = int(meths.get('id'))
                    if meths == int(file[0]) % 10:
                        def createSection(file, idMeth):
                            """add methods to xml file"""
                            idMeth.append((ET.fromstring(classBefore)))
                            filename = filePath+'\\'+name
                            writeFile(tostring(res), filename, context)
                            os.remove(TEMPORARY + '\\' + file)
                        createSection(file, idMeth)
                else:
                    logger.info(type(res))
                    ET.SubElement(res, 'methods')
                    def createSection(file, idMeth):
                        """add methods to xml file"""
                        idMeth.append((ET.fromstring(classBefore)))
                        filename = filePath + '\\' + name
                        writeFile(tostring(res), filename, context)
                        os.remove(TEMPORARY + '\\' + file)

                    createSection(file, idMeth)

                first_res = ElementTree.tostring(res, 'utf-8')
                rough_string = re.sub(r'<delimit?>', '\n', first_res)
                rough_string = re.sub(r'</delimit?>', '', rough_string)
                rough_string = re.sub('\n+', '', rough_string)
                reparsed = minidom.parseString(rough_string)
                textXML = reparsed.toprettyxml(indent="\t")
                writeFile(textXML, filename, context)

        else:
            readFile1(context, name, filePath)
            textXML = context['fileContent']
    return HttpResponse(textXML)
