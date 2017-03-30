from os.path import exists
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

arrayelt = []
arrayeltM=[]
attribut = ""
attributM=""
z = 0 - 1
test = False
nbfich=0
nbfich2=0
nbclic=0
nbclics=0
z2=0-1


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
# *********************************************************************
def generate(request):

    global attribut
    global arrayelt
    global z
    global test
    global nbfich
    global nbclic
    global nbclics

    context = {'error': ''}
    a = request.POST.get('version');
    select = request.POST.get("class_id", None)
    nbligne = request.POST.get("nbligne", None)
    nbclicstructure = request.POST.get("nbclicstructure", None)
    # nbelement = request.POST.get("nbelement", None)
    # nb = request.POST.get("nb", None)
    nb = 0
    compteur=0
    nbs=0
    n=0
    print("file")

    # nbfich += 1
    while exists("C:/Users/g507888/PycharmProjects/PFE/polls/XMLFiles/filename" + str(nbfich) + ".xml"):
        print "nbfich++"
        nbfich+=1
    # z=0
    # indice = request.POST.get("indice", None)
    ind = 0
    nbelement = request.POST.getlist("nbelement", False)
    print ("nbelement" + str(nbelement))
    # for i in range(len(nbelement)):
    #     print nbelement[i]
    # list = nbelement.split("-")
    # print(list)
    if (nbelement != False):
        list = (max(nbelement, key=len))
        print (list)
        z = 0

        listelt = list.split(",")
        print((listelt))
        if (len(listelt)) == 2:
            arrayelt = listelt
        else:

            elt = ""
            for y in (listelt):
                if len(elt) >= len(y):
                    arrayelt.append(elt)
                    elt = y


                else:
                    elt = y
            # if(listelt[len(listelt)-1]) not in arrayelt:
            arrayelt.append(listelt[len(listelt) - 1])
            print "arrayelt"
            print arrayelt

    # elt = (max(listelt, key=len))
    # print elt

    # att_elt=elt.split("-")
    # print att_elt







    # ************************************************
    root = ET.Element("class", id=unicode(select), version=unicode(a))

    doc = ET.SubElement(root, "description")
    doc.text = "clock"
    att = ET.SubElement(root, "attributes")

    nbclicStruct = 0
    at = ET.SubElement(att, "attribute", id="1", name="logical_name", type="octet-string", size="6")
    for i in range(2, (int(nbligne)) + 1):

        cpt = 0
        nbclicStruct = 0
        nbs+=1
        compteur=0
        nbclic=0
        nbclics=0

        print "n="+str(n)

        print("indice for " + str(ind))
        attID = request.POST.get("AttributeID-" + str(i), None)
        attName = request.POST.get("AttributeName-" + str(i), None)
        attType = request.POST.get("attributeType-" + str(i), None)
        # attSize = request.POST.get("attributesize-" + str(i), None)
        at = ET.SubElement(att, "attribute", id=unicode(attID), name=unicode(attName), type=unicode(attType),
                           size="")
        print("attribut" + unicode(attType))
        print("nbligne" + str(nbligne))

        # *************************************************array**************************************************************
        if (unicode(attType) == "array"):
            x = 0
            ind += 1
            nbclic += 1

            print("indice" + str(ind))
            # print("nbclicstructure"+ nbclicstructure)
            attSize = request.POST.get("attributesize-" + str(i), None)

            array = ET.SubElement(at, "array",size=unicode(attSize))
            j = 1
            if (int(attSize) == 0):
                ind += 1

            while (j < (int(attSize)) + 1):

                attributeTypeArray = request.POST.get(
                    "attributeTypeArray-" + str(i) + "-" + str(j) + "-" + str(ind) + "-" + str(nbclicStruct), None)
                print ("attributeTypeArray" + str(i) + "-" + str(j) + "-" + str(ind) + "-" + str(nbclicStruct))
                # print("indice" + str(ind))
                # ind += 1



                cell = ET.SubElement(array, unicode(attributeTypeArray), size="")

                # **************************************************************************************************************
                if (unicode(attributeTypeArray) == "structure"):
                    n += 1
                    print("longeur= " + str(len(arrayelt[z])))
                    print("arrayelt[z]= " + str((arrayelt[z])))
                    print ("cpt" + str(cpt))


                    # if (len(arrayelt[z])<3) & (test==True) :
                    #     print("z if = "  +str(z))
                    #     # z=0-1
                    #     print("len(arrayelt)=" + str(len(arrayelt)))
                    #     if z < (len(arrayelt) -1):
                    #         print("<")
                    #         z += 1
                    #         print "z < (len(arrayelt) -1)"+ str(z)
                    # if(len(arrayelt[z])>2) & (test==True) & cpt != 0 :
                    #     if z < (len(arrayelt) - 1):
                    #         z += 1
                    #         print "(len(arrayelt[z])>2) & (test==True)" + str(z)




                    #
                    # else:
                    #     cpt=0
                    # cpt+=1
                    print ("cpt=" + str(cpt))

                    nbe = 0
                    compteur=0
                    nbclicStruct += 1
                    nb += 1
                    print("nb= "+str(nb))
                    # ind+=1
                    print("struct")

                    print(len(arrayelt))

                    print("z" + str(z))
                    if (len(arrayelt) == 1):

                        attribut = arrayelt[len(arrayelt) - 1].split("-")

                    else:

                        print("arrayelt[z]" + str(arrayelt[z]))
                        attribut = str(arrayelt[z]).split("-")
                        count = 0



                    # print(len(attribut))
                    # while a in range(len((attribut))):
                    nbe = 0
                    print (attribut[cpt])

                    if (attribut[cpt] != ''):

                        while (nbe <= (int(attribut[cpt]) - 1)):
                            # print("count"+str(count))
                            test = False

                            elementtype = request.POST.get(
                                "elementtype-" + str(i) + "-" + str(attSize) + "-" + str(nbe) + "-" + str(nb), None)
                            print("elementType" + str(i) + "-" + str(attSize) + "-" + str(nbe) + "-" + str(nb))
                            structelement = ET.SubElement(cell, unicode(elementtype), size="")

                            structuresize = request.POST.get("attributesize-" + str(i) + "-" + str(j) + "-" + str(nbe),
                                                             None)

                            # count += 1

                            nbe += 1
                        if nbe > int(attribut[cpt]) - 1:
                            test = True

                        nbclicStruct = 0

                    ind += 1
                elif (unicode(attributeTypeArray) != "structure"):

                    nbclicStruct = 0
                    # z += 1








                    ind += 1
                    x += 1
                    if (len(attribut) > 2):
                        cpt = cpt - 1
                    print("elif indice=" + str(ind))
                else:
                    nbclicStruct = 0
                    nbe = 0

                    ind += 1
                    x += 1
                    print("else indice=" + str(ind))
                if len(attribut) > 2:
                    cpt += 1
                j += 1

                print("cpt j" + str(cpt))
                # cpt= -1

            ind -= 1
            print("indice=" + str(ind))
            # if(cpt==0) & z <=len(arrayelt):
            #     z+=1
            if z < len(arrayelt) - 1:
                z += 1
        nbelt = -1

        if (unicode(attType) == "structure"):




            nbelt += 1
            nb+=1
            n+=1

            print "arrayelt[z] struct"
            print arrayelt[z].split("-")
            struct = arrayelt[z].split("-")
            c=0
            print struct[c]

            structuresizes = request.POST.get("structuresize-" + str(i) + "-" + str(nbclics) + "-" + str(0), None)
            print "structuresize-" + str(i) + "-" + str(nbclics) + "-" + str(0)
            print structuresizes
            structure = ET.SubElement(at, "structure", size=unicode(struct[0]))





            while (compteur <= (int(struct[c]) - 1)):
                # print("count"+str(count))
                # test = False


                elementtypes = request.POST.get(
                    "elementtype-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n), None)
                print("elementType" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n))

                eltsize = request.POST.get(
                    "elementsize-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n), None)

                print  "elementsize-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n)
                structelement = ET.SubElement(structure, unicode(elementtypes), size=unicode(eltsize))
                print (eltsize)



                if (unicode(elementtypes)=="array"):
                    nbclics=0


                    j2 = 1


                    while (j2 < (int(eltsize)) + 1):
                        ind += 1
                        print("z="+str(z))

                        elementTypeArray = request.POST.get(
                            "attributeTypeArray-" + str(i) + "-" + str(j2) + "-" + str(ind) + "-" + str(nbclicStruct),
                            None)
                        print ("attributeTypeArray" + str(i) + "-" + str(j2) + "-" + str(ind) + "-" + str(nbclicStruct))
                        print("indice" + str(ind))
                        cell = ET.SubElement(structelement, unicode(elementTypeArray), size="")
                        if(unicode(elementTypeArray)=="structure"):

                            cpt+=1
                            nbes=0
                            nb+=1
                            print("z="+str(z))
                            print "struct array struct"
                            print("cpt="+str(cpt))
                            attribut = str(arrayelt[z]).split("-")
                            print attribut[cpt]
                        #     *****************************
                        if (attribut[cpt] != ''):

                            while (nbes <= (int(attribut[cpt]) - 1)):
                                # print("count"+str(count))
                                test = False

                                elementtype = request.POST.get(
                                    "elementtype-" + str(i) + "-" + str(eltsize) + "-" + str(nbes) + "-" + str(nb), None)
                                print("elementType" + str(i) + "-" + str(eltsize) + "-" + str(nbes) + "-" + str(nb))
                                structelement = ET.SubElement(cell, unicode(elementtype), size="")

                                # structuresize = request.POST.get(
                                #     "attributesize-" + str(i) + "-" + str(j) + "-" + str(nbe),
                                #     None)

                                # count += 1

                                nbes += 1
                        z+=1
                        # ************************************






                        j2 += 1

                compteur += 1





            z+=1
            nbclics += 1







    tree = ET.ElementTree(root)

    print("nbfich"+str(nbfich ))

    tree.write("C:/Users/g507888/PycharmProjects/PFE/polls/XMLFiles/filename"+str(nbfich)+".xml")


    # **************************************************





    return render(request, 'login.html', context)
# **********************************************************************
def generateMethod(request):
    global nbfich2
    global arrayeltM
    global attributM
    global z2
    context = {'error': ''}
    print "method"
    nbligne2 = request.POST.get("nbligne2", None)
    nbelementM = request.POST.getlist("nbelementM", False)
    print ("nbelementM" + str(nbelementM))
    root = ET.Element("class", id="", version="")

    meth = ET.SubElement(root, "methodes")
    nM=0
    nbM=0



    while exists("C:/Users/g507888/PycharmProjects/PFE/polls/XMLFilesMethod/filenameM" + str(nbfich2) + ".xml"):
        print "nbfich++"
        nbfich2 += 1
        indM=1

    if (nbelementM != False):
        listM = (max(nbelementM, key=len))
        print (listM)
        z2 = 0

        listeltM = listM.split(",")
        print((listeltM))
        if (len(listeltM)) == 2:
            arrayeltM = listeltM
        else:

            eltM = ""
            for y in (listeltM):
                if len(eltM) >= len(y):
                    arrayeltM.append(eltM)
                    eltM = y


                else:
                    eltM = y
            # if(listelt[len(listelt)-1]) not in arrayelt:
            arrayeltM.append(listeltM[len(listeltM) - 1])
            print "arrayeltM"
            print arrayeltM
    nbclicStructM=-1
    clics = 1
    for i in range(1, (int(nbligne2))+1):

        indM=1
        cptM=0

        nba=0


        methID = request.POST.get("MethodeID-" + str(i), None)
        methName = request.POST.get("methodName-" + str(i), None)
        methType = request.POST.get("methodType-" + str(i), None)

        methSize = request.POST.get("methodsize-" + str(i), None)
        method = ET.SubElement(meth, "method", id=unicode(methID), name=unicode(methName), type=unicode(methType),
                               size=unicode(methSize))




        if (unicode(methType) == "array"):
            array = ET.SubElement(method, "array", size=unicode(methSize))
            nbclicStructM+=1





            j = 1
            if (int(methSize) == 0):
                indM += 1
            # if (int(methSize) == 2):
            #     print"methsize=2"
            #     attributM = arrayeltM[len(arrayeltM) - 1].split("-")
            #     print attributM

            while (j < (int(methSize)) + 1):
                methodTypeArray = request.POST.get(
                    "methodType-" + str(i) + "-" + str(j) + "-" + str(j) + "-" + str(nbclicStructM), None)
                print ("methodType-" + str(i) + "-" + str(j) + "-" + str(j) + "-" + str(nbclicStructM))
                print methodTypeArray

                cellsize=request.POST.get("structuresize-"+ str(i) + "-" + str(methSize) + "-" + str(clics) , None)
                print "structuresize-"+ str(i) + "-" + str(methSize) + "-" + str(clics)

                cell = ET.SubElement(array, unicode(methodTypeArray), size=unicode(cellsize))

                indM += 1
                if (unicode(methodTypeArray) == "structure"):
                    nM += 1
                    clics+=1

                    print("longeur= " + str(len(arrayeltM[z2])))
                    print("arrayelt[z2]= " + str((arrayeltM[z2])))
                    print ("cptM" + str(cptM))







                    print ("cpt=" + str(cptM))

                    nbe = 0
                    compteur = 0
                    # nbclicStructM += 1
                    nbM += 1
                    print("nb= " + str(nbM))
                    # ind+=1
                    print("struct")

                    print(len(arrayeltM))

                    print("z2" + str(z2))
                    if (len(arrayeltM) == 1) | int(nbligne2)==1:

                        attributM = arrayeltM[len(arrayeltM) - 1].split("-")

                    else:

                        print("arrayelt[z2]" + str(arrayeltM[z2]))
                        attributM = str(arrayeltM[z2]).split("-")
                        count = 0

                    # print(len(attribut))
                    # while a in range(len((attribut))):
                    nbeM = 0
                    print (attributM[cptM])
                    print("cptM"+str(cptM))
                    if (attributM[cptM] != ''):

                        while (nbeM <= (int(attributM[cptM]) - 1)):
                            # print("count"+str(count))
                            test = False

                            elementtype = request.POST.get(
                                "methodType-" + str(i) + "-" + str(methSize) + "-" + str(nbeM) + "-" + str(nbM), None)
                            print("methodTypeElement" + str(i) + "-" + str(methSize) + "-" + str(nbeM) + "-" + str(nbM))
                            structelement = ET.SubElement(cell, unicode(elementtype), size="")

                            # structuresize = request.POST.get("attributesize-" + str(i) + "-" + str(j) + "-" + str(nbe),
                            #                                  None)

                            # count += 1

                            nbeM += 1
                        if nbeM > int(attributM[cptM]) - 1:
                            test = True
                        if len(attributM) > 2:
                            cptM += 1



                    indM += 1
            #     *****************************
                elif (unicode(methodTypeArray) != "structure"):

                    nbclicStructM = 0

                    # indM += 1

                    if (len(attributM) > 2):
                        cptM = cptM - 1
                    print("elif indice=" + str(indM))
                else:
                    nbclicStructM = 0
                    nbeM = 0

                    indM += 1

                    print("else indice=" + str(indM))
                if len(attribut) > 2:
                    cptM += 1
                j += 1

                print("cpt j" + str(cptM))
                # cpt= -1

            indM -= 1
            print("indice=" + str(indM))
            # if(cpt==0) & z <=len(arrayelt):
            #     z+=1
            if z2 < len(arrayeltM) - 1:
                z2 += 1
            nbclicStructM += 1
            print("nbclicstructM"+str(nbclicStructM))
        nbeltM = -1


            # *************************************


    tree = ET.ElementTree(root)
    tree.write("C:/Users/g507888/PycharmProjects/PFE/polls/XMLFilesMethod/filenameM" + str(nbfich2) + ".xml")


    return render(request, 'login.html', context)

# ***********************************************************************

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
