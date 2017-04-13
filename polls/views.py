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
association=''
# associationMethods8 = 'MNGT\npublic\npre'


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

@login_required(login_url="login/")
def welcome(request):
    """Welcome page"""
    return render(request, "welcome.html")


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
        # ###
        FileName = re.sub(r'\\\\', r'\\', FileName)
        filePath = PRODUCTS + FileName
        tree = ET.ElementTree(file=filePath)
        count = 0
        dict1 = {}
        iter_ = tree.getiterator()
        for elem in iter_:
            count += 1
            dict1[count] = [elem.tag, elem.attrib, elem.text ]

        return HttpResponse(simplejson.dumps({'stat': str(status['fileContent']), 'dict': dict1, 'length': len(dict1)}), content_type='application/json')
    else:
        status= {'fileContent': 'Fail Loading Content'}
        return HttpResponse(status)


@csrf_protect
@login_required(login_url="login/")
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
            nameFile = request.POST['nameFile']
            pathFile = request.POST['pathFile']
            tree = ET.fromstring(xml_data)
            DictionaryDescription = ''.join([literal.text for literal in tree.findall('.//description')])
            # DictionaryClass = ''.join([literal.text for literal in tree.findall('.//class')])
            DictionaryClass = pathFile + '\\objects_dictionary'
            if nameFile == '':
                nameFile = DictionaryDescription
            fileName = getNewFileName('\\'.join([DictionaryClass, nameFile]))
            if (not os.path.isfile(fileName)):
                writeFile(request.POST['content'], fileName, context)
                pretty_print = lambda f: '\n'.join( [line for line in xml.dom.minidom.parse(open(f)).toprettyxml(indent=' ' * 2).split('\n') if line.strip()])
                str1 = pretty_print(fileName)
                logger.info(str1)
                with open(fileName, 'w') as f:
                    f.write(str1)
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
    global meth1, description
    global association
    status = ''
    association = ''
    if request.method == "POST" and request.is_ajax():
        classId1 = request.POST['id']
        classsubItem = request.POST['name']
        pathAssociation = os.path.join(PRODUCTS, classId1, 'EMeterF.xml')
        docAss = minidom.parse(pathAssociation)
        assocs = docAss.getElementsByTagName('clientAdress')
        for assocs1 in assocs:
            assoc = assocs1.getElementsByTagName('client')
            for assoc1 in assoc:
                sid = assoc1.getAttribute('adress')
                name = assoc1.getAttribute('associationName')
                association += "{}-{}".format(sid, name)+"\n"
            association = association[:-1]
        ###########
        classId = classId1 + "\\class_" + classsubItem
        dictionatyName = classId+'.xml'
        # if (str(classsubItem) == '8'):
        #     # association = association8
        #     associationMethods = associationMethods8
        # elif (str(classsubItem) == '11'):
        #     association = association11
        # elif (str(classsubItem) == '15'):
        #     association = association15
        filePath = os.path.join('Classes', dictionatyName)
        doc = minidom.parse(filePath)
        dictClass = doc.getElementsByTagName('class')
        for dictClass1 in dictClass:
            dictId = dictClass1.getAttribute('id')
            dictVersion = dictClass1.getAttribute('version')
        description = doc.getElementsByTagName('description')
        description = description[0].firstChild.nodeValue
        attrs = doc.getElementsByTagName('attributes')
        meths = doc.getElementsByTagName('methods')
        for attrs1 in attrs:
            attr = attrs1.getElementsByTagName('attribute')
            for attr1 in attr:
                sid = attr1.getAttribute('id')
                name = attr1.getAttribute('name')
                type = attr1.getAttribute('type')
                size = attr1.getAttribute('size')
                status += "{}- {}, {}, {}".format(sid, name, type, size)+"\n"
        methods= ''
        for meths1 in meths:
            meth = meths1.getElementsByTagName('method')
            for meth1 in meth:
                sid = meth1.getAttribute('id')
                name = meth1.getAttribute('name')
                methods += "{}-{}".format(sid, name)+"\n"
        return HttpResponse(simplejson.dumps({'stat': status, 'dictDescription': description, 'dictId': dictId, 'dictVersion': dictVersion, 'methods': methods, 'association': association, 'associationMethods': association}), content_type='application/json')


def createTemporary(request, template_name="list.html"):
    """create temporary files"""
    global idAttr
    associationList = association.split('\n')
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
            child = SubElement(top, 'association', name=item[2:], operations='_')
        else:
            ops = '\\'.join(ops)
            child = SubElement(top, 'association', name=item[2:], operations=ops)
    with open(TEMPORARY+'\\'+idAttr+'.xml', 'w') as f:
        el = xml.dom.minidom.parseString(tostring(top))
        pretty_xml_as_string = el.toprettyxml()
        f.write(pretty_xml_as_string.encode('UTF-8'))
    return listtree(request, template_name)

def generateXML(request):
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
        filename = filePath + '\\' + name
        l = os.listdir(TEMPORARY)
        readFile1(context, name, filePath)
        classAfter = context['fileContent']
        if l != []:
            for file in l:
                filename = filePath + '\\' + name
                context1 = {'error': ''}
                readFile1(context1, str(file), TEMPORARY)
                classBefore = context1['fileContent']
                res = ET.fromstring(classAfter)
                if (file[0]=='a'):
                    for attrs in res.findall('attributes'):
                        for attr in attrs.findall('attribute'):
                            idAttr = int(attr.get('id'))
                            f = file[1:-4]
                            f = int(f)
                            if idAttr == f :
                                for association in attr.findall('association'):
                                    attr.remove(association)
                                attr.append((ET.fromstring(classBefore)))
                                classAfter = tostring(res)
                                os.remove(TEMPORARY + '\\' + file)
                if (file[0]=='m'):
                    for meths in res.findall('methods'):
                        for meth in meths.findall('method'):
                            idMerth = int(meth.get('id'))
                            f = file[1:-4]
                            f = int(f)
                            if idMerth == f:
                                for association in meth.findall('association'):
                                    meth.remove(association)
                                meth.append((ET.fromstring(classBefore)))
                                classAfter = tostring(res)
                                os.remove(TEMPORARY + '\\' + file)

                first_res = ElementTree.tostring(res, 'utf-8')
                rough_string = re.sub(r'<delimit?>', '', first_res)
                rough_string = re.sub(r'</delimit?>', '', rough_string)
                rough_string = re.sub('\n+', '', rough_string)
                reparsed = minidom.parseString(rough_string)
                textXML = reparsed.toprettyxml(indent="\t")
                textXML = re.sub('\n+', '\n', textXML)
        else:
            readFile1(context, name, filePath)
            textXML = context['fileContent']
    return HttpResponse(textXML)
import json
def update(request):
    """update object dictionaries"""
    brand_category = request.POST.get('parameter[]')
    Lbrand_category = json.loads(brand_category)
    sep0 = '#'
    sep1  = '\n'
    sep2 = '@'
    sep3 = '\t'
    # sep4 = '&'
    for D in Lbrand_category:
        content = D['val']
        fileName = content[:content.find(sep0)]
        tag = content[content.find(sep2) + 1:content.find(sep3)]
        attribute = content[content.find(sep3) + 1:content.find(sep1)]
        value = content[content.find(sep1) + 1:]
        occur = tag[0]
        occur1 = tag[2]

        fileName = re.sub(r'\\\\', r'\\', fileName)
        path = os.path.join(PRODUCTS, fileName)
        tree = ET.parse(path)
        root = tree.getroot()
        k = tag[tag.find(occur1)+1:] + '[' + occur1 + ']'
        logger.info(k)
        for attrs in root.findall('attributes'):
                tag1 = attrs.find(k)
                if occur == '0':
                    tag1.set(attribute, value)
                else:
                    occur1 = tag[2]
                    l = 'attribute[' + occur1 + ']'
                    logger.info(l)
                    for item in attrs.findall(l):
                        k = tag[tag.find(occur1)+1:] + '[' + occur + ']'
                        logger.info(k)
                        assoc = item.findall(k)
                        for element in assoc:
                            element.set(attribute, value)
        # else:
        #     tag1 = root.find(k)
        #     if tag1 is not None:
        #         tag1.set(attribute, value)
        #     else:
        #         occur1 = tag[2]
        #         l = 'attribute[' + occur1 + ']'
        #         for item in root.findall(l):
        #             k = tag[tag.find(occur1) + 1:] + '[' + occur + ']'
        #             logger.info(k)
        #             for assocs in item.findall('dlmsAttribute[0]'):
        #                 assoc = assocs.find(k)
        #                 assoc.set(attribute, value)
        #             else:
        #                 assoc = item.find(k)
        #                 assoc.set(attribute, value)
        with open(path, 'w') as f:
            f.write(tostring(root))


    return HttpResponse(0);