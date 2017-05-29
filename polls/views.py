import json as simplejson
import logging
import os
import re
import sys
import xml.dom.minidom
import xml.etree.ElementTree as ET
import xml.etree.cElementTree as ET
from os.path import exists
from xml.dom import minidom
from xml.dom import minidom
from xml.etree.ElementTree import Element, SubElement, tostring

import serial
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.core.files import File
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from polls.forms import *
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect, csrf_exempt
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
import os, stat
import xml.etree.cElementTree as ET
import shutil
from stat import S_IWUSR  # Need to add this import to the ones above

from polls.forms import *
import easygui
from django.core.files.storage import FileSystemStorage
import sys
import serial

logger = logging.getLogger(__name__)



####################### GLOBAL VARIABLES ################################################
PRODUCTS = 'Products\\'
TESTCASES= 'C:\\Users\\g507888\\PycharmProjects\\MTT_Background\\'
CLASSES = 'Classes\\'
TEMPORARY = 'TEMPORARYFILE'
methods8 = 'Reset\n'
methods11 = 'Reset\n'
methods15 = 'Reset\n'
association=''


arrayelt = []
arrayeltM=[]
attribut = ""
attributM=""
z = - 1
test = False
nbfich=0
nbfich2=0
nbclic=0
nbclics=0
z2=-1


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
    return render(request, "welcome.html")
from django.conf.urls import include
@login_required(login_url="login/")
def welcome(request):
    """Welcome page"""
    return render(request, "welcome.html")

# @login_required(login_url="login/")
# def admin(request):
#     return redirect('/admin/')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

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
   

    # nbfich += 1
    while exists("polls/XMLFile/filename" + str(nbfich) + ".xml"):
       
        nbfich+=1
    # z=0
    # indice = request.POST.get("indice", None)
    ind = 0
    nbelement = request.POST.getlist("nbelement", False)
    # print ("nbelement" + str(nbelement))
    # for i in range(len(nbelement)):
    #     print nbelement[i]
    # list = nbelement.split("-")
    # print(list)
    if (nbelement != False):
        list = (max(nbelement, key=len))
        # print (list)
        z = 0

        listelt = list.split(",")
        # print((listelt))
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
            # print "arrayelt"
            # print arrayelt

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

        # print "n="+str(n)
        #
        # print("indice for " + str(ind))
        attID = request.POST.get("AttributeID-" + str(i), None)
        attName = request.POST.get("AttributeName-" + str(i), None)
        attType = request.POST.get("attributeType-" + str(i), None)
        # attSize = request.POST.get("attributesize-" + str(i), None)
        at = ET.SubElement(att, "attribute", id=unicode(attID), name=unicode(attName), type=unicode(attType),
                           size="")
        # print("attribut" + unicode(attType))
        # print("nbligne" + str(nbligne))

        # *************************************************array**************************************************************
        if (unicode(attType) == "array"):
            x = 0
            ind += 1
            nbclic += 1

            # print("indice" + str(ind))
            # print("nbclicstructure"+ nbclicstructure)
            attSize = request.POST.get("attributesize-" + str(i), None)

            array = ET.SubElement(at, "array",size=unicode(attSize))
            j = 1
            if (int(attSize) == 0):
                ind += 1

            while (j < (int(attSize)) + 1):

                attributeTypeArray = request.POST.get(
                    "attributeTypeArray-" + str(i) + "-" + str(j) + "-" + str(ind) + "-" + str(nbclicStruct), None)
                # print ("attributeTypeArray" + str(i) + "-" + str(j) + "-" + str(ind) + "-" + str(nbclicStruct))
                # print("indice" + str(ind))
                # ind += 1



                cell = ET.SubElement(array, unicode(attributeTypeArray), size="")

                # **************************************************************************************************************
                if (unicode(attributeTypeArray) == "structure"):
                    n += 1
                    # print("longeur= " + str(len(arrayelt[z])))
                    # print("arrayelt[z]= " + str((arrayelt[z])))
                    # print ("cpt" + str(cpt))


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
                    # print ("cpt=" + str(cpt))

                    nbe = 0
                    compteur=0
                    nbclicStruct += 1
                    nb += 1
                    # print("nb= "+str(nb))
                    # # ind+=1
                    # print("struct")
                    #
                    # print(len(arrayelt))
                    #
                    # print("z" + str(z))
                    if (len(arrayelt) == 1):

                        attribut = arrayelt[len(arrayelt) - 1].split("-")

                    else:

                        # print("arrayelt[z]" + str(arrayelt[z]))
                        attribut = str(arrayelt[z]).split("-")
                        count = 0



                    # print(len(attribut))
                    # while a in range(len((attribut))):
                    nbe = 0
                    # print (attribut[cpt])

                    if (attribut[cpt] != ''):

                        while (nbe <= (int(attribut[cpt]) - 1)):
                            # print("count"+str(count))
                            test = False

                            elementtype = request.POST.get(
                                "elementtype-" + str(i) + "-" + str(attSize) + "-" + str(nbe) + "-" + str(nb), None)
                            # print("elementType" + str(i) + "-" + str(attSize) + "-" + str(nbe) + "-" + str(nb))
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
                    # print("elif indice=" + str(ind))
                else:
                    nbclicStruct = 0
                    nbe = 0

                    ind += 1
                    x += 1
                    # print("else indice=" + str(ind))
                if len(attribut) > 2:
                    cpt += 1
                j += 1

                # print("cpt j" + str(cpt))
                # cpt= -1

            ind -= 1
            # print("indice=" + str(ind))
            # if(cpt==0) & z <=len(arrayelt):
            #     z+=1
            if z < len(arrayelt) - 1:
                z += 1
        nbelt = -1

        if (unicode(attType) == "structure"):




            nbelt += 1
            nb+=1
            n+=1

            # print "arrayelt[z] struct"
            # print arrayelt[z].split("-")
            struct = arrayelt[z].split("-")
            c=0
            # print struct[c]

            structuresizes = request.POST.get("structuresize-" + str(i) + "-" + str(nbclics) + "-" + str(0), None)
            # print "structuresize-" + str(i) + "-" + str(nbclics) + "-" + str(0)
            # print structuresizes
            structure = ET.SubElement(at, "structure", size=unicode(struct[0]))





            while (compteur <= (int(struct[c]) - 1)):
                # print("count"+str(count))
                # test = False


                elementtypes = request.POST.get(
                    "elementtype-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n), None)
                # print("elementType" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n))

                eltsize = request.POST.get(
                    "elementsize-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n), None)

                # print  "elementsize-" + str(i) + "-" + str(nbclics) + "-" + str(compteur) + "-" + str(n)
                structelement = ET.SubElement(structure, unicode(elementtypes), size=unicode(eltsize))
                # print (eltsize)



                if (unicode(elementtypes)=="array"):
                    nbclics=0


                    j2 = 1


                    while (j2 < (int(eltsize)) + 1):
                        ind += 1
                        # print("z="+str(z))

                        elementTypeArray = request.POST.get(
                            "attributeTypeArray-" + str(i) + "-" + str(j2) + "-" + str(ind) + "-" + str(nbclicStruct),
                            None)
                        # print ("attributeTypeArray" + str(i) + "-" + str(j2) + "-" + str(ind) + "-" + str(nbclicStruct))
                        # print("indice" + str(ind))
                        cell = ET.SubElement(structelement, unicode(elementTypeArray), size="")
                        if(unicode(elementTypeArray)=="structure"):

                            cpt+=1
                            nbes=0
                            nb+=1
                            # print("z="+str(z))
                            # print "struct array struct"
                            # print("cpt="+str(cpt))
                            attribut = str(arrayelt[z]).split("-")
                            # print attribut[cpt]
                        #     *****************************
                        if (attribut[cpt] != ''):

                            while (nbes <= (int(attribut[cpt]) - 1)):
                                # print("count"+str(count))
                                test = False

                                elementtype = request.POST.get(
                                    "elementtype-" + str(i) + "-" + str(eltsize) + "-" + str(nbes) + "-" + str(nb), None)
                                # print("elementType" + str(i) + "-" + str(eltsize) + "-" + str(nbes) + "-" + str(nb))
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

    # print("nbfich"+str(nbfich ))

    tree.write("polls/XMLFile/filename"+str(nbfich)+".xml")


    # **************************************************





    return render(request, 'login.html', context)
# ***********************************************************************
#  added by farah***********************************************************************************
FileName1 = ''
tree1 = {}
def getNameF(request):
    """get file Name"""
    logger.info("information")
    global FileName1
    if request.method == "POST" and request.is_ajax():
        FileName1 = request.POST['id']
        logger.info(FileName1)
        # status = display(FileName1)
        status=''

        path="Products\\"+FileName1
        doc = minidom.parse(path)
        productFile = doc.getElementsByTagName('Product')
        for pdt in productFile:
            deviceType = pdt.getAttribute('deviceType')
            productName = pdt.getAttribute('name')
        # print productName
        soft = doc.getElementsByTagName('softwareVersion')
        for so in soft:
            software = so.getAttribute('value')

        serial = doc.getElementsByTagName('SerialNumber')
        for s in serial:
            serialNumber = s.getAttribute('value')
        manufacturer= doc.getElementsByTagName('manufacturer')
        for m in manufacturer:
            manu = m.getAttribute('value')
        description = doc.getElementsByTagName('description')
        for d in description:
            desc = d.getAttribute('value')
        equipementId=doc.getElementsByTagName('equipement_identifier')
        for e in equipementId:
            eqID = e.getAttribute('value')
        MeterIP=doc.getElementsByTagName('MeterIP')
        for meter in MeterIP:
             meID= meter.getAttribute('value')
        MeterPort = doc.getElementsByTagName('MeterPort')
        for meterP in MeterPort:
            meterP = meterP.getAttribute('value')
        ServerAdress = doc.getElementsByTagName('ServerAdress')
        for server in ServerAdress:
            serverA = server.getAttribute('adress')
        firmware= doc.getElementsByTagName('firmware')
        for firm in firmware:
            firmware = firm.getAttribute('value')
        TCP=doc.getElementsByTagName('TCP')
        for t in TCP:
            TcpTime = t.getElementsByTagName('TCP_timeout')
            for tt in TcpTime:
                tcpTimeOut = tt.getAttribute('value')

        HDLC = doc.getElementsByTagName('HDLC')
        for h in HDLC:
            HdlcTime = h.getElementsByTagName('HDLC_timeout')
            for hh in HdlcTime:
                hdlcTimeOut = hh.getAttribute('value')

            HDLC_maxTransmit = h.getElementsByTagName('HDLC_maxTransmit')
            for hmax in HDLC_maxTransmit:
                HDLC_maxT = hmax.getAttribute('value')


            HDLC_maxReceive = h.getElementsByTagName('HDLC_maxReceive')
            for hmaxR in HDLC_maxReceive:
                HDLC_maxR = hmaxR.getAttribute('value')


            HDLC_Adress = h.getElementsByTagName('HDLC_Adress')
            for hAdd in HDLC_Adress:
                HDLC_Adr = hAdd.getAttribute('adress')


            baudrate = h.getElementsByTagName('Baudrate')
            for b in baudrate:
                bau = b.getAttribute('value')




        mode_e = doc.getElementsByTagName('ModeE')
        for m in mode_e:
            mode = m.getAttribute('adress')


        ClientAdress = doc.getElementsByTagName('ClientAdress')
        for c in ClientAdress:
            ClientAdr = c.getElementsByTagName('client')
            i=0;
            for cc in ClientAdr:

                client_adr = cc.getAttribute('adress')
                association_name = cc.getAttribute('associationName')
                status += client_adr+','+ association_name + "/"
                i+=1





        MasterKey = doc.getElementsByTagName('MasterKey')
        for Mkey in MasterKey:
            Mas_key = Mkey.getAttribute('value')

        GlobalKey = doc.getElementsByTagName('GlobalKey')
        for Gkey in GlobalKey:
            global_key = Gkey.getAttribute('value')


        AuthentificationKey = doc.getElementsByTagName('AuthentificationKey')
        for Akey in AuthentificationKey:
            Authen_key = Akey.getAttribute('value')


        LLSAuthentification=doc.getElementsByTagName('LLSAuthentification')
        for Lkey in LLSAuthentification:
           L_key = Lkey.getAttribute('value')


        HLS_Secret = doc.getElementsByTagName('HLS_Secret')
        for Hkey in HLS_Secret:
            H_key = Hkey.getAttribute('value')

        logger.info(H_key)



        return HttpResponse(simplejson.dumps({'stat': status,'software':software,'deviceType': deviceType,'productName':productName,'serialNumber':serialNumber,'manu':manu,
                                              'desc':desc,'eqID':eqID,'meID':meID,'meterP':meterP,'serverA':serverA,'firmware':firmware,'tcpTimeOut':tcpTimeOut,
                                              'hdlcTimeOut':hdlcTimeOut,'HDLC_maxT':HDLC_maxT,'HDLC_maxR':HDLC_maxR,'HDLC_Adr':HDLC_Adr,'bau':bau,'mode':mode,'Mas_key':Mas_key,
                                              'global_key':global_key,'Authen_key':Authen_key,'L_key':L_key,'H_key':H_key,'serverA':serverA,'i':i}), content_type='application/json')



    else:
        status= {'fileContent': 'Fail Loading Content'}
        return HttpResponse(status)
# ****
def generateMethod(request):
    global nbfich2
    global arrayeltM
    global attributM
    global z2
    # generate(request)

    context = {'error': ''}
    # print "method"
    nbligne2 = request.POST.get("nbligne2", None)

    nbelementM = request.POST.getlist("nbelementM", False)
    # print ("nbelementM" + str(nbelementM))
    root = ET.Element("class", id="", version="")

    meth = ET.SubElement(root, "methodes")
    nM=0
    nbM=0



    while exists("polls/XMLFilesMethod/filenameM" + str(nbfich2) + ".xml"):
        # print "nbfich2 ++"
        nbfich2 += 1
        indM=1

    if (nbelementM != False):
        listM = (max(nbelementM, key=len))
        # print (listM)
        z2 = 0

        listeltM = listM.split(",")
        # print((listeltM))
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
            # print "arrayeltM"
            # print arrayeltM
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
        # print ("methodSIze"+str(methSize))
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
                # print ("methodType-" + str(i) + "-" + str(j) + "-" + str(j) + "-" + str(nbclicStructM))
                # print methodTypeArray

                cellsize=request.POST.get("structuresize-"+ str(i) + "-" + str(methSize) + "-" + str(clics) , None)
                # print "structuresize-"+ str(i) + "-" + str(methSize) + "-" + str(clics)

                cell = ET.SubElement(array, unicode(methodTypeArray), size=unicode(cellsize))

                indM += 1
                if (unicode(methodTypeArray) == "structure"):
                    nM += 1
                    clics+=1

                    # print("longeur= " + str(len(arrayeltM[z2])))
                    # print("arrayelt[z2]= " + str((arrayeltM[z2])))
                    # print ("cptM" + str(cptM))
                    #
                    #
                    #
                    #
                    #
                    #
                    #
                    # print ("cpt=" + str(cptM))

                    nbe = 0
                    compteur = 0
                    # nbclicStructM += 1
                    nbM += 1
                    # print("nb= " + str(nbM))
                    # # ind+=1
                    # print("struct")
                    #
                    # print(len(arrayeltM))
                    #
                    # print("z2" + str(z2))
                    if (len(arrayeltM) == 1) | int(nbligne2)==1:

                        attributM = arrayeltM[len(arrayeltM) - 1].split("-")

                    else:

                        # print("arrayelt[z2]" + str(arrayeltM[z2]))
                        attributM = str(arrayeltM[z2]).split("-")
                        count = 0

                    # print(len(attribut))
                    # while a in range(len((attribut))):
                    nbeM = 0
                    # print (attributM[cptM])
                    # print("cptM"+str(cptM))
                    if (attributM[cptM] != ''):

                        while (nbeM <= (int(attributM[cptM]) - 1)):
                            # print("count"+str(count))
                            test = False

                            elementtype = request.POST.get(
                                "methodType-" + str(i) + "-" + str(methSize) + "-" + str(nbeM) + "-" + str(nbM), None)
                            # print("methodTypeElement" + str(i) + "-" + str(methSize) + "-" + str(nbeM) + "-" + str(nbM))
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
                    # print("elif indice=" + str(indM))
                else:
                    nbclicStructM = 0
                    nbeM = 0

                    indM += 1

                    # print("else indice=" + str(indM))
                if len(attribut) > 2:
                    cptM += 1
                j += 1

                # print("cpt j" + str(cptM))
                # cpt= -1

            indM -= 1
            # print("indice=" + str(indM))
            # if(cpt==0) & z <=len(arrayelt):
            #     z+=1
            if z2 < len(arrayeltM) - 1:
                z2 += 1
            nbclicStructM += 1
            # print("nbclicstructM"+str(nbclicStructM))
        nbeltM = -1


            # *************************************


    tree = ET.ElementTree(root)

    tree.write("polls/XMLFilesMethod/filenameM" + str(nbfich2) + ".xml")








    return render(request, 'login.html', context)



# **
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

        logger.info(dict1)

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
        pathAssociation = os.path.join(PRODUCTS, classId1, 'product_config.xml')
        logger.info(pathAssociation)
        docAss = minidom.parse(pathAssociation)
        assocs = docAss.getElementsByTagName('clientAdress')
        for assocs1 in assocs:
            assoc = assocs1.getElementsByTagName('client')
            for assoc1 in assoc:
                sid = assoc1.getAttribute('adress')
                name = assoc1.getAttribute('associationName')
                association += "{}".format(name)+"\n"
            association = association[:-1]
        ###########
        classId = classId1 + "\\class_" + classsubItem
        dictionatyName = classId+'.xml'
      
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
                logger.info(status)
        methods= ''
        for meths1 in meths:
            meth = meths1.getElementsByTagName('method')
            for meth1 in meth:
                sid = meth1.getAttribute('id')
                name = meth1.getAttribute('name')
                x = ' '
                methods += "{}-{}".format(sid, name)+"\n"
        return HttpResponse(simplejson.dumps({'stat': status, 'dictDescription': description, 'dictId': dictId, 'dictVersion': dictVersion, 'methods': methods, 'association': association, 'associationMethods': association}), content_type='application/json')


def createTemporary(choices, methods):
    """create temporary files"""
    rough_string = ''
    rough_string1 = ''
    sep0 = '@'
    # sep1 = ':'
    # sep2 = '&'
    global idAttr
    if choices != '':
        content = {}
        i = 0
        chaine = str(choices)
        chaine = chaine[chaine.find(sep0) + 1:]
        associationList = association.split('\n')
        while(chaine.find('@') != -1):
            content[i] = chaine[:chaine.find(sep0)]
            chaine = chaine[chaine.find(sep0)+1:]
            i += 1
        content[i] = chaine
        i = 0
        l = []
        while (i< len(content)):
            element = content[i].split('#')
            temp = element[1]
            temp2 = element[0]
            element.pop(1)
            element.pop(0)
            element.append(temp2[1])
            element.append(temp.split(':'))
            i += 1
            l.append(element)
        newResult = []
        x = []

        oldResult = l
        for itemL in l:

            element = []
            x=[]
            for itemN in oldResult:
                if (itemL[0] == itemN[0]):
                    s = itemL[1]
                    t = itemN[1]
                    if (s[0] == t[0]) and (s[1] != t[1]):
                        x.append(itemN)
                        s[1] += '/' + t[1]
                        element = [itemL[0], s]
            if element == []:
                element = itemL
            if element not in newResult:
                newResult.append(element)
            for elem in x:
                l.remove(elem)

        l = newResult



        top = Element('delimit')
        sid  = -1
        for component in l:
            if component[0] != sid:
                child1 = SubElement(top, 'attribute', id=component[0])
                for item in associationList:
                    child = SubElement(child1, 'association', name=item, operations='_')

            for item in associationList:
                ops = []
                if item in component[1]:
                    x= component[1]
                    ops.append(x[1])
                if ops:
                    ops = '\\'.join(ops)
                    for a in child1.iter('association'):
                        if a.get('name', ops) == item:
                            a.set('operations', ops)
            sid = component[0]
        rough_string = re.sub(r'<delimit?>', '', tostring(top))
        rough_string = re.sub(r'</delimit?>', '', rough_string)
        logger.info(rough_string)
    ##################################
    if methods != '':
        content = {}
        i = 0
       
        chaine = str(methods)
        chaine = chaine[chaine.find(sep0) + 1:]
        associationList = association.split('\n')
        while(chaine.find('@') != -1):
            content[i] = chaine[:chaine.find(sep0)]
            chaine = chaine[chaine.find(sep0)+1:]
            i += 1
        content[i] = chaine
       
        i = 0
        l = []
        while (i< len(content)):
            element = content[i].split('#')
            temp = element[1]
            temp2 = element[0]
            element.pop(1)
            element.pop(0)
            element.append(temp2[1])
            element.append(temp.split(':'))
            i +=1
            l.append(element)
        newResult = []
        x = []

        oldResult = l
        for itemL in l:

            element = []
            x=[]
            for itemN in oldResult:
                if (itemL[0] == itemN[0]):
                    s = itemL[1]
                    t = itemN[1]
                    if (s[0] == t[0]) and (s[1] != t[1]):
                        x.append(itemN)
                        s[1] += '/' + t[1]
                        element = [itemL[0], s]
            if element == []:
                element = itemL
            if element not in newResult:
                newResult.append(element)
            for elem in x:
                l.remove(elem)

        l = newResult

        top = Element('delimit')
        sid  = -1
        for component in l:
            if component[0] != sid:
                child1 = SubElement(top, 'attribute', id=component[0])
                for item in associationList:
                    child = SubElement(child1, 'association', name=item, operations='_')

            for item in associationList:
                ops = []
                if item in component[1]:
                    x= component[1]
                    ops.append(x[1])
                if ops:
                    ops = '\\'.join(ops)
                    for a in child1.iter('association'):
                        if a.get('name', ops) == item:
                            a.set('operations', ops)
            sid = component[0]
        rough_string1 = re.sub(r'<delimit?>', '', tostring(top))
        rough_string1 = re.sub(r'</delimit?>', '', rough_string1)
    forEmpty = Element('delimit')
    child1 = SubElement(forEmpty, 'attribute')
    for item in associationList:
        child = SubElement(child1, 'association', name=item, operations='_')
    rough_string2 = re.sub(r'<delimit?>', '', tostring(forEmpty))
    rough_string2 = re.sub(r'</delimit?>', '', rough_string2)

    return (rough_string, rough_string1, rough_string2)

def generateXML(request):
    """add associates to attributes in XML file and generate final dictionary"""
    context = {'error': ''}
    if request.method == "POST" and request.is_ajax():
        choices = request.POST['checks']
        methods = request.POST['methods1']
        product = request.POST['product']
        classNum = request.POST['classNum']
        # obisCode = request.POST['obisCode']
        # Description = request.POST['Description']
        # version = request.POST['version']
        # textareaContent2 = request.POST['textareaContent2']
        # textareaContent3 = request.POST['textareaContent3']
        #
        z, y, x= createTemporary(choices, methods)
        logger.info(y)
        name = 'class_' + str(classNum) + '.xml'
        filePath ='Classes\\'+product
        filename = filePath + '\\' + name
      
        readFile1(context, name, filePath)
        classAfter = context['fileContent']
        classAfter1 = ''
        classAfter2 = ''
        if z != '' or y != '':
            if z != '':
                filename = filePath + '\\' + name
                classBefore = z.split('</attribute>')
                res = ET.fromstring(classAfter)
                if y != '':
                    for element in res.findall('methods'):
                        res.remove(element)
                for attrs in res.findall('attributes'):
                    for attr in attrs.findall('attribute'):
                        idAttr = attr.get('id')
                        exist = False
                        for item in classBefore:
                            if (item.find(idAttr) != -1):
                                exist = True
                                addElement = item[item.find('>')+1:]
                                addElement = '<delimit>\n'+addElement+'\n</delimit>'
                                logger.info(addElement)
                                attr.append((ET.fromstring(addElement)))

                        if not exist:
                            logger.info(x)
                            addElement = x[x.find('>') + 1:]
                            addElement = re.sub(r'</attribute?>', '', addElement)
                            addElement = '<delimit>\n' + addElement + '\n</delimit>'
                            attr.append(ET.fromstring(addElement))
                classAfter1 = tostring(res)

            if y != '':
                filename = filePath + '\\' + name
                classBefore = y.split('</method>')
                res = ET.fromstring(classAfter)
                if z != '':
                    for element in res.findall('attributes'):
                        res.remove(element)
                for attrs in res.findall('methods'):
                    for attr in attrs.findall('method'):
                        idAttr = attr.get('id')
                        exist = False
                        for item in classBefore:
                            if (item.find(idAttr) != -1):
                                exist = True
                                addElement = item[item.find('>') + 1:]
                                addElement = re.sub(r'</attribute?>', '', addElement)
                                addElement = '<delimit>\n' + addElement + '\n</delimit>'
                                attr.append(ET.fromstring(addElement))
                        if not exist:
                            addElement = x[x.find('>') + 1:]
                            addElement = re.sub(r'</attribute?>', '', addElement)
                            addElement = '<delimit>\n' + addElement + '\n</delimit>'
                            attr.append(ET.fromstring(addElement))
                classAfter2 = tostring(res)

            if classAfter1 != '' and classAfter2 !='':
                result = classAfter1[:classAfter1.rfind('\n')]
                result += '\n' + classAfter2.split('\n', 1)[1];
            else:
                result = classAfter1 + classAfter2
            rough_string = re.sub(r'<delimit?>', '', result)
            rough_string = re.sub(r'</delimit?>', '', rough_string)
            rough_string = re.sub('\n+', '\n', rough_string)
            reparsed = minidom.parseString(rough_string)
            textXML = reparsed.toprettyxml(indent="\t")
            textXML = re.sub('\n+', '\n', textXML)
            textXML = rough_string
        else:
            readFile1(context, name, filePath)
            textXML = context['fileContent']
    return HttpResponse(textXML)


# **********************************************modif farah

def addProduct(request, template_name="listProduct.html"):
    print ""
    return render(request, template_name)
# ******************************************************

def generateProduct(request,template_name="listProduct.html"):
    
    nbclient=request.POST.get("nbclient",None)


    deviceType=request.POST.get("deviceType",None)

    productName = request.POST.get("productName", None)


    serialNumber = request.POST.get("serialNumber", None)


    softwareVersion = request.POST.get("softwareVersion", None)

    manufacturer = request.POST.get("Manufacturer", None)

    description = request.POST.get("description", None)

    equipementIdentifier = request.POST.get("equipementIdentifier", None)

    meterIP = request.POST.get("meterIP", None)


    serverAdress = request.POST.get("serverAdress", None)

    meterPort = request.POST.get("meterPort", None)


    firmwareFile = request.FILES['firmware']


    tcpTimeout = request.POST.get("tcpTimeout", None)

    hdlcTimeout = request.POST.get("hdlcTimeout", None)

    hdlcMaxReceive = request.POST.get("hdlcMaxReceive", None)

    hdlcMaxTransmit = request.POST.get("hdlcMaxTransmit", None)

    hdlcAdress = request.POST.get("hdlcAdress", None)

    baudrate = request.POST.get("baudrate", None)

    modeEadress = request.POST.get("modeEadress", None)

    masterKey = request.POST.get("masterKey", None)

    globalKey = request.POST.get("globalKey", None)

    authentificationKey = request.POST.get("authentificationKey", None)

    hlsSecret = request.POST.get("hlsSecret", None)

    llsAuth = request.POST.get("llsAuth", None)

    # ***************************xml File*************************************
    root = ET.Element("Product",name=unicode(productName),deviceType=unicode(deviceType))
    serial = ET.SubElement(root, "SerialNumber",value=unicode(serialNumber))
    software = ET.SubElement(root, "softwareVersion", value=unicode(equipementIdentifier))
    manu = ET.SubElement(root, "manufacturer", value=unicode(manufacturer))
    desc = ET.SubElement(root, "description", value=unicode(description))
    equipement=ET.SubElement(root, "equipement_identifier", value=unicode(softwareVersion))
    ip = ET.SubElement(root, "MeterIP", value=unicode(meterIP))

    meter_port = ET.SubElement(root, "MeterPort", value=unicode(meterPort))
    serverAdd = ET.SubElement(root, "ServerAdress", adress=unicode(serverAdress))
    firmware = ET.SubElement(root, "firmware", value=unicode(firmwareFile))
    tcp = ET.SubElement(root, "TCP")
    tcpT=ET.SubElement(tcp, "TCP_timeout",value=unicode(tcpTimeout))
    hdlc = ET.SubElement(root, "HDLC")
    hdlcT = ET.SubElement(hdlc, "HDLC_timeout", value=unicode(hdlcTimeout))
    hdlcMaxT = ET.SubElement(hdlc, "HDLC_maxTransmit", value=unicode(hdlcMaxTransmit))
    hdlcMaxR = ET.SubElement(hdlc, "HDLC_maxReceive", value=unicode(hdlcMaxReceive))
    hdlcAdd = ET.SubElement(hdlc, "HDLC_Adress", value=unicode(hdlcAdress))
    baud = ET.SubElement(hdlc, "Baudrate", value=unicode(baudrate))
    modeE = ET.SubElement(root, "ModeE", adress=unicode(modeEadress))
    clientA = ET.SubElement(root, "ClientAdress")
    for i in range(1, (int(nbclient)) + 1):
        clientAdress=request.POST.get("clientAdress-" + str(i), None)
        associationName=request.POST.get("associationName-" + str(i), None)
        client = ET.SubElement(clientA, "client", adress=unicode(clientAdress),associationName=unicode(associationName))
    masterK = ET.SubElement(root, "MasterKey", value=unicode(masterKey))
    globalK = ET.SubElement(root, "GlobalKey", value=unicode(globalKey))
    authentificationK = ET.SubElement(root, "AuthentificationKey", value=unicode(authentificationKey))
    lls = ET.SubElement(root, "LLSAuthentification", value=unicode(llsAuth))
    hls = ET.SubElement(root, "HLS_Secret", value=unicode(hlsSecret))

    newpath = "Products\\" + str(productName)
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    tree = ET.ElementTree(root)
    tree.write(newpath + "/"+ str(productName) + ".xml")
    os.makedirs(newpath+ "/objects_dictionary ")


    return treeListF(request)
# *******************************************
pathXml=""
filePDt=""
@csrf_protect

def editProduct(request,template_name="listProduct.html"):
    global pathXml
    global filePDt
    NewclientAdress=[]
    NewAssociationName=[]
    clientAdressAdded=[]
    assocNameAdded=[]
    checkedButton=[]
    checkedButton2 = []
    OldproductName = request.POST.get("OldproductName", None)
    NewproductName = request.POST.get("productName", None)

    OldDeviceType = request.POST.get("OldDeviceType", None)
    NewDeviceType = request.POST.get("deviceType", None)

    OldSerialNumber = request.POST.get("OldSerialNumber", None)
    NewserialNumber = request.POST.get("serialNumber", None)

    OldEquipement = request.POST.get("OldEquipement", None)
    Newequipement = request.POST.get("equipement", None)

    OldSoft = request.POST.get("OldSoft", None)
    NewSoft = request.POST.get("softwarevesrion", None)

    Oldmanu = request.POST.get("Oldmanu", None)
    Newmanu = request.POST.get("Manufacturer", None)

    Olddesc = request.POST.get("Olddesc", None)
    NewDesc = request.POST.get("description", None)

    OldMeterIp = request.POST.get("OldMeterIp", None)
    NewMeterIp = request.POST.get("meterIP", None)


    OldMeterPort = request.POST.get("OldMeterPort", None)
    NewMeterPort = request.POST.get("meterPort", None)


    OldServerAdd = request.POST.get("OldServerAdd", None)
    NewServerAdd = request.POST.get("serverAdress", None)


    OldFirmware = request.POST.get("OldFirmware", None)
    NewFirmware = request.POST.get("filename", None)


    OldTcpTime= request.POST.get("OldTcpTime", None)
    NewTcpTime = request.POST.get("tcpTimeout", None)


    OldHdlcTime = request.POST.get("OldHdlcTime", None)
    NewHdlcTime = request.POST.get("hdlcTimeout", None)


    OldHdlcMaxTransmit = request.POST.get("OldHdlcMaxTransmit", None)
    NewHdlcMaxTransmit = request.POST.get("hdlcMaxTransmit", None)


    OldHdlcMaxR = request.POST.get("OldHdlcMaxR", None)
    NewhdlcMaxReceive = request.POST.get("hdlcMaxReceive", None)

    OldHdlcAddr = request.POST.get("OldHdlcAddr", None)
    NewhdlcAdress = request.POST.get("hdlcAdress", None)

    Oldbaudrate = request.POST.get("Oldbaudrate", None)
    Newbaudrate = request.POST.get("baudrate", None)

    Oldmode = request.POST.get("Oldmode", None)
    Newmode = request.POST.get("modeEadress", None)

    OldMas_keyt = request.POST.get("OldMas_keyt", None)
    NewmasterKey = request.POST.get("masterKey", None)

    Oldglobal_key = request.POST.get("Oldglobal_key", None)
    NewglobalKey = request.POST.get("globalKey", None)

    OldAuth = request.POST.get("OldAuth", None)
    NewAuth = request.POST.get("authentificationKey", None)

    OldhlsSecret = request.POST.get("OldhlsSecret", None)
    NewhlsSecret = request.POST.get("hlsSecret", None)

    OldllsAuth = request.POST.get("OldllsAuth", None)
    NewllsAuth = request.POST.get("llsAuth", None)

    nbclientAffich = request.POST.get("nbclient", None)
    NumberOFAddedClientID=request.POST.get("NumberOFAddedClientID", None)



    BeginNumberClient=request.POST.get("BeginNumberClient", None)

    # *****Get clients ADDED************************************
    if ( BeginNumberClient!= None):
        for i in range(int(BeginNumberClient)+1,(int(NumberOFAddedClientID))+1):
            clientAdressAdded.append(request.POST.get("clientAdress-" + str(i), None))
            assocNameAdded.append(request.POST.get("associationName-"+str(i), None))


    #********Get client ******************
    if(nbclientAffich!=None):
        print  "nbclient"+nbclientAffich
        for i in range(int(nbclientAffich)):
            NewclientAdress.append((request.POST.get("clientAdress-" + str(i), None)))
            NewAssociationName.append((request.POST.get("associationName-" + str(i), None)))
            checkedButton.append((request.POST.get("remove-" + str(i), None)))
      




    pathXml = "Products\\" + OldproductName + "\\" + OldproductName + ".xml"


    if (NewproductName != OldproductName) | (OldDeviceType != NewDeviceType) |(NewserialNumber!=OldSerialNumber) |(OldEquipement != Newequipement )|(OldSoft!=NewSoft) |(Oldmanu!=Newmanu) |(Olddesc!=NewDesc)|(OldMeterIp!=NewMeterIp)\
            |(OldMeterPort != NewMeterPort) |(OldServerAdd!=NewServerAdd) |( OldFirmware!= NewFirmware) |(OldTcpTime != NewTcpTime)|(OldHdlcTime!=NewHdlcTime)|(OldHdlcMaxTransmit!=NewHdlcMaxTransmit)\
            |(OldHdlcMaxR!=NewhdlcMaxReceive)|(OldHdlcAddr!=NewhdlcAdress)|(Oldbaudrate != Newbaudrate) |(Oldmode!=Newmode)|(OldMas_keyt!=NewmasterKey)|(Oldglobal_key!= NewglobalKey)|(OldAuth!=NewAuth)|(OldhlsSecret!=NewhlsSecret)\
            |(OldllsAuth!=NewllsAuth):
        for file in os.listdir("Products\\"):
            if file == OldproductName:
                status = ''
                os.chmod(pathXml, 0o777)
                filePDt =open(pathXml, "r+")

                tree = ET.parse(filePDt)
                root = tree.getroot()
                root.set('name', NewproductName)
                root.set('deviceType',NewDeviceType)
                SerialXML=root.find('SerialNumber')
                SerialXML.set('value',NewserialNumber)

                EqIdXml=root.find('equipement_identifier')
                EqIdXml.set('value',Newequipement)

                softXml=root.find('softwareVersion')
                softXml.set('value',NewSoft)

                manuXml = root.find('manufacturer')
                manuXml.set('value', Newmanu)

                descXml = root.find('description')
                descXml.set('value', NewDesc)

                meterIPXml = root.find('MeterIP')
                meterIPXml.set('value', NewMeterIp)

                meterPortXml = root.find('MeterPort')
                meterPortXml.set('value', NewMeterPort)

                ServerAddXml = root.find('ServerAdress')
                ServerAddXml.set('adress', NewServerAdd)

                FirmwareXml = root.find('firmware')
                FirmwareXml.set('value', NewFirmware)

                TcpXml = root.find('TCP')
                TcpTO=TcpXml.find('TCP_timeout')
                TcpTO.set('value', NewTcpTime)

                HDLCXml = root.find('HDLC')
                HdlcTO = HDLCXml.find('HDLC_timeout')
                HdlcTO.set('value', NewHdlcTime)
                HdlcMaxT = HDLCXml.find('HDLC_maxTransmit')
                HdlcMaxT.set('value', NewHdlcMaxTransmit)
                HdlcMaxR = HDLCXml.find('HDLC_maxReceive')
                HdlcMaxR.set('value', NewhdlcMaxReceive)
                HdlcAddr = HDLCXml.find('HDLC_Adress')
                HdlcAddr.set('adress', NewhdlcAdress)
                baud = HDLCXml.find('Baudrate')
                baud.set('value', Newbaudrate)

                modeEXml = root.find('ModeE')
                modeEXml.set('adress', Newmode)

                MasterKeyXML = root.find('MasterKey')
                MasterKeyXML.set('value', NewmasterKey)

                globalKeyXML = root.find('GlobalKey')
                globalKeyXML.set('value', NewglobalKey)

                AuthentificationKeyXML = root.find('AuthentificationKey')
                AuthentificationKeyXML.set('value', NewAuth)

                HLS_SecretXMl = root.find('HLS_Secret')
                HLS_SecretXMl.set('value', NewhlsSecret)

                LLSAuthentificationXML = root.find('LLSAuthentification')
                LLSAuthentificationXML.set('value', NewllsAuth)

                i=0

                if (NewclientAdress != []):
                    for client in root.iter('client'):
                        client.set('adress',NewclientAdress[i])
                        client.set('associationName',NewAssociationName[i])
                        i+=1
                clt=root.find('ClientAdress')

                for clientAdd,assocAdd in zip(clientAdressAdded,assocNameAdded):
                    client = ET.SubElement(clt, "client", adress=unicode(clientAdd),
                                       associationName=unicode(assocAdd))


                # ******************remove elements
                for check in checkedButton:
                    if check != None:
                        print "ckeck"+ str(check)

                        for client in root.iter('ClientAdress'):

                            for clt in client.iter('client'):
                                print "clt" + str(clt.get('adress'))
                                if clt.get('adress') == NewclientAdress[int(check)]:
                                    client.remove(clt)






                filePDt.close()
                # modif du fichier******************************************
                filePDt = open(pathXml, "w+")
                filePDt.write(tostring(root))
                filePDt.close()

        os.rename("Products\\" + OldproductName + "\\" + OldproductName + ".xml","Products\\" + OldproductName + "\\" + NewproductName + ".xml")
        os.rename("Products\\" + OldproductName, "Products\\" +NewproductName)



    manufacturer = request.POST.get("Manufacturer", None)


    description = request.POST.get("description", None)


    equipementIdentifier = request.POST.get("equipement", None)


    meterIP = request.POST.get("meterIP", None)


    serverAdress = request.POST.get("serverAdress", None)


    meterPort = request.POST.get("meterPort", None)

    # firmwareFile = request.FILES['firmware']
    filename=request.POST.get("filename", None)

    tcpTimeout = request.POST.get("tcpTimeout", None)


    hdlcTimeout = request.POST.get("hdlcTimeout", None)


    hdlcMaxReceive = request.POST.get("hdlcMaxReceive", None)



    hdlcMaxTransmit = request.POST.get("hdlcMaxTransmit", None)


    hdlcAdress = request.POST.get("hdlcAdress", None)


    baudrate = request.POST.get("baudrate", None)


    modeEadress = request.POST.get("modeEadress", None)


    masterKey = request.POST.get("masterKey", None)


    globalKey = request.POST.get("globalKey", None)



    authentificationKey = request.POST.get("authentificationKey", None)


    hlsSecret = request.POST.get("hlsSecret", None)


    llsAuth = request.POST.get("llsAuth", None)

    easygui.msgbox("YourProductFile has been modified successfully!", title="information")
    return treeListF(request)



# *********************************************
@csrf_protect

def treeListF(request, template_name="listProduct.html", path=PRODUCTS):
    """show tree of products """
    def listtreeFfunction(path):
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
                    if recent != 'objects_dictionary':
                        tree['children'].append(listtreeFfunction(fn))
                else:
                    tree['children'].append(dict(name=recent))
        return tree
    global tree
    tree = listtreeFfunction(path)
    return render(request, template_name, {'tree': tree,})

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
     
        for attrs in root.findall('attributes'):
                tag1 = attrs.find(k)
                if occur == '0':
                    tag1.set(attribute, value)
                else:
                    occur1 = tag[2]
                    l = 'attribute[' + occur1 + ']'
                  
                    for item in attrs.findall(l):
                        k = tag[tag.find(occur1)+1:] + '[' + occur + ']'
                       
                        assoc = item.findall(k)
                        for element in assoc:
                            element.set(attribute, value)

        with open(path, 'w') as f:
            f.write(tostring(root))
    return HttpResponse(0);
# **************************************Test Cases****
@csrf_protect

def TestCasesTree(request, template_name="listTestCases.html", path=TESTCASES):
    # productName=request.POST.get('pr')
    # print ('product'+str(productName))
    """show tree of testcases """
    def listtreeFfunction(path):
        """Browse the tree"""
        result = path.rpartition('\\')[2]
        # print result
        tree = dict(name=result, children=[])

        try:
            lst = os.listdir(path)

        except OSError:
            pass
        else:
            for name in lst:
                fn = os.path.join(path, name)

                recent = name
                print recent

                if( os.path.isdir(fn) )& (recent=='TestCases'):


                    tree['children'].append(listtreeFfunction(fn))




                    # tree['children'].append(dict(name=recent))
                else:

                    if (os.path.isdir(fn)==False) and path=='C:\Users\g507888\PycharmProjects\MTT_Background\TestCases':

                        tree['children'].append(dict(name=recent))

        return tree

    def listtreeFfunction2(path):
        """Browse the tree"""
        result = path.rpartition('\\')[2]
        treeP = dict(name=result, children=[])
        try:
            lst = os.listdir(path)
        except OSError:
            pass
        else:
            for name in lst:
                fn = os.path.join(path, name)
                recent = name
                if os.path.isdir(fn):
                    treeP['children'].append(listtreeFfunction2(fn))
                else:
                    treeP['children'].append(dict(name=recent))
        return treeP


    global tree
    global treeP
    tree = listtreeFfunction(path)
    treeP = listtreeFfunction2(PRODUCTS)


    return render(request, template_name, {'tree': tree,'treeP': treeP})
# **************************************************************************
def getNameTest(request):
    """get file Name"""
    logger.info("information")
    global FileName1
    if request.method == "POST" and request.is_ajax():
        FileName1 = request.POST['id']
        logger.info(FileName1)
        # status = display(FileName1)
        status=''

        path="Products\\G1product\\objects_dictionary"+FileName1
        doc = minidom.parse(path)
        File = doc.getElementsByTagName('class')
        for pdt in File:
            id = pdt.getAttribute('id')

        print File

        return HttpResponse(simplejson.dumps({'stat': status,'id':id}), content_type='application/json')



    else:
        status= {'fileContent': 'Fail Loading Content'}

        return HttpResponse(status)
#     *************************************************************
def generateTest(request,template_name="DictionnaryObject.html"):
    product=request.POST.get("ProductList")
    AssociationName=request.POST.get("AssociationName")


    action = request.POST.get("action")
    access = request.POST.get("access")
    firm=request.POST.get("firm")
    check = request.POST.get("check")

    print product
    print action
    pathO="Products\\"+str(product)

    def listtreeFfunction(pathO):
        """Browse the tree"""
        result = pathO.rpartition('\\')[2]
        tree = dict(name=result, children=[])
        try:
            lst = os.listdir(pathO)
        except OSError:
            pass
        else:
            for name in lst:
                fn = os.path.join(pathO, name)
                recent = name
                recent=recent.split('.')
                recent=recent[0]


                if os.path.isdir(fn):
                    tree['children'].append(listtreeFfunction(fn))
                else:
                    tree['children'].append(dict(name=recent))
        return tree


    global tree

    tree = listtreeFfunction(pathO)


    return render(request,template_name,{'tree': tree,'action' :action,'product':product,'access':access,'firm':firm,'AssociationName':AssociationName,'check':check})
# *******************************************************************************************
@csrf_exempt
def getAttributes (request,template_name="DictionnaryObject.html"):
    action = request.POST.get("action")

    path = request.POST.get("path")
    print ("path" + str(path))
    pdt = request.POST.get("pdt")



    print ("pdt" + str(pdt))
    ObjectFile = request.POST.get("ObjectList")
    logger.info("information")
    global FileName1
    if request.method == "POST" and request.is_ajax():
        FileName1 = request.POST['id']
        FileName1=FileName1+'.xml'
        logger.info(FileName1)
        # status = display(FileName1)
        status = ''
        statusM = ''
        idAtt=''
        type=''
        idMeth=''
        associationNameMNG=''
        associationNamePublic=''
        associationNamePre=''
        asName=''
        operation=''
        operationN=''
        asso=''

        res1=''
        res2=''
        res3=''
        res=''
        MNGT=''
        public=''
        pre=''
        getAssocM=''
        getAssocPu = ''
        getAssocPr = ''
        ch1=''
        ch2=''
        att=''
        meth=''
        nb=0
        assoM=''
        method_id = ''

        path = "Products\\" + FileName1
        doc = minidom.parse(path)
        File = doc.getElementsByTagName('dictionnary')
        object = doc.getElementsByTagName('object')



        for a in object:
            attr = doc.getElementsByTagName('attribute')
            method = doc.getElementsByTagName('method')
            ch1=''
            nbatt=0
            for name in attr:
                att += name.getAttribute('name')+','
                type+=name.getAttribute('type')+','
                idAtt += name.getAttribute('id')+','
                nbatt+=1


            nb=att.count(',')



            for name in attr:

                dlmsAttribute = doc.getElementsByTagName('dlmsAttribute')
                attName = name.getAttribute('name')

                attType=name.getAttribute('type')

                j=-1
                for assoc in dlmsAttribute:

                    res=''

                    association = assoc.getElementsByTagName('association')



                    for i in association:




                        assoName = i.getAttribute('name')
                        operationName=i.getAttribute('operations')


                        res+= assoName + ':' + operationName + "|"





                    if j<nbatt-1:
                        j+=1
                        ch1+=(att.split(','))[j]+':'+(type.split(','))[j]+':'+(idAtt.split(','))[j]+"="+res+"\n"
                    # print (att.split(','))[j]
                break



                status += attName + "\n"

                idAtt+= attId +"/"
                type+= attType +"/"

        nbmeth=0

        for b in object:

            method = doc.getElementsByTagName('method')
            for name in method:
                meth += name.getAttribute('name') + ','
                method_id += name.getAttribute('id') + ','
                print method_id

                nbmeth+=1
            methAtt=att+meth
            nba = methAtt.count(',')


            ch2 = ''
            for methodName in method:
                dlmsAttributeM = doc.getElementsByTagName('dlmsAttribute')
                methName = methodName.getAttribute('name')
               

                z = -1
                for assoc in dlmsAttributeM:


                    res2 = ''

                    association = assoc.getElementsByTagName('association')

                    for i in association:
                        assoM = i.getAttribute('name')

                        operationN = i.getAttribute('operations')

                        res2 += assoM + ':' + operationN + "|"




                    if z<nba-1:
                        z+=1
                        ch2 += (methAtt.split(','))[z] +"=" + res2 + "\n"



                break









        list=res.split("|||")





        for i in list:
            i=str(i)
            # print i
            if i!='':
                index=i.index(':')

                action=i[0:index]

                if action=="MNGT":
                    MNGT+=i[index+1:len(i)]+"&"

                elif action=="pre":
                    pre+=i[index+1:len(i)]+"&"
                else:
                    public+=i[index+1:len(i)]+"&"

        # print res1
        # print "getAssoc"
        # print getAssocM

        print ch2



        return HttpResponse(
            simplejson.dumps({'att': att, 'meth': meth,'ident':idAtt,'idMeth':idMeth,'type':type, 'path': path, 'pdt': pdt, 'action': action,"file":FileName1,'method_id':method_id,
                            'operation':operation,'MNGT':MNGT,'pre':pre,'public':public,'getAssocM':getAssocM,'getAssocPu':getAssocPu,'getAssocPr':getAssocPr,'ch1':ch1,'ch2':ch2,'nbatt':nbatt,'nbmeth':nbmeth }),
            content_type='application/json')


    else:
        status = {'fileContent': 'Fail Loading Content'}

        return HttpResponse(status)
# **********************************************

nbTest=0
def getXML(request,template_name="welcome.html"):
    global nbTest
    newpath = "TestCases\\"
    firm = request.POST.get("firm")
    print ("firm"+str(firm))


    while exists(newpath +"test_"+str(nbTest) + ".xml"):

        nbTest+=1


    logger.info ("generatexml")
    action = request.POST.get("operationS")
    print action
    file = request.POST.get("filename")
    print "filename"+file
    chainefile=file.split('\\')
    fileSelected=chainefile[len(chainefile)-1]

    FileO=fileSelected.split('.')
    ObjectSelected =FileO[0]



    # *****getting values*********************

    stepId = request.POST.get("stepId")
    exValue=request.POST.get("exValue")
    purpose=request.POST.get("purpose")
    desc = request.POST.get("desc")
    product=request.POST.get('prdt')
    

    # ******************************setting values**
    stepId = request.POST.get("stepId")
    inValue = request.POST.get("inValue")
    purpose = request.POST.get("purpose")
    desc = request.POST.get("desc")
    expected = request.POST.get("expected")

    # ************************************Action values******

    stepId = request.POST.get("stepId")

    purpose = request.POST.get("purpose")
    desc = request.POST.get("desc")
    expected = request.POST.get("expected")
    # ******************************************wait values

    stepId = request.POST.get("stepId")
    inValue = request.POST.get("inValue")
    purpose = request.POST.get("purpose")
    desc = request.POST.get("desc")

    # ******************************************
    if action=="Get":
        attributSelectedId = request.POST.get("attName")


        AttributChar = attributSelectedId.split(':')

        actionName="ReadRequest"
        root = ET.Element("action", id=unicode(stepId ),description=unicode(desc))
        data_link = ET.SubElement(root, "data_link", name="DLMS_ANY1")
        funct = ET.SubElement(root, "function")
        paramAsXMl = ET.SubElement(root, "paramAsXml")
        result = ET.SubElement(root, "result")
        ok = ET.SubElement(result, "ok", ret="ok")
        default = ET.SubElement(result, "default", ret="nok")

        funct.text = actionName
        service = ET.SubElement(paramAsXMl, unicode(actionName))
        purposee = ET.SubElement(service, "purpose")
        purposee.text=purpose

        object = ET.SubElement(service, "object")
        objectName = ET.SubElement(object, "objectName")
        objectName.text = ObjectSelected
        attributId = ET.SubElement(object, "AttributID")

        attributId.text=AttributChar[2]
        checks = ET.SubElement(service, "checks")
        check = ET.SubElement(checks, "checks1", type="execute_result")
        typeVar= ET.SubElement(check, unicode(AttributChar[1]), name=unicode(AttributChar[0]),value=unicode(exValue))


    elif action=="Set":
        attributSelectedId = request.POST.get("attName")
        AttributChar = attributSelectedId.split(':')
        actionName = "WriteRequest"
        root = ET.Element("action", id=unicode(stepId ),description=unicode(desc))
        data_link = ET.SubElement(root, "data_link", name="DLMS_ANY1")
        funct = ET.SubElement(root, "function")
        funct.text = actionName



        paramAsXMl = ET.SubElement(root, "paramAsXml")
        result = ET.SubElement(root, "result")
        ok = ET.SubElement(result, "ok", ret="ok")
        default = ET.SubElement(result, "default", ret="nok")

        service = ET.SubElement(paramAsXMl, unicode(actionName))
        purposee = ET.SubElement(service, "purpose")
        purposee.text = purpose

        object = ET.SubElement(service, "object")
        objectName = ET.SubElement(object, "objectName")
        objectName.text = ObjectSelected
        attributId = ET.SubElement(object, "AttributID")
        attributId.text = AttributChar[2]
        checks = ET.SubElement(service, "checks")
        check = ET.SubElement(checks, "checks1", type="execute_result")
        check.text=unicode(expected)

        values=ET.SubElement(service, "values")
        value1=ET.SubElement(values, "value1", Description="DLMS structure")
        typeValue=ET.SubElement(value1, unicode(AttributChar[1]), name=unicode(AttributChar[0]), value=unicode(inValue))

    elif action == "Action":
        methodselected = request.POST.get("methName")

        MethodChar = methodselected.split(':')
        actionName = "ActionRequest"
        root = ET.Element("action", id=unicode(stepId ),description=unicode(desc))
        data_link = ET.SubElement(root, "data_link", name="DLMS_ANY1")
        funct = ET.SubElement(root, "function")
        funct.text = actionName
        paramAsXMl = ET.SubElement(root, "paramAsXml")
        result = ET.SubElement(root, "result")
        ok = ET.SubElement(result, "ok", ret="ok")
        default = ET.SubElement(result, "default", ret="nok")
        service = ET.SubElement(paramAsXMl, unicode(actionName))
        purposee = ET.SubElement(service, "purpose")
        purposee.text = purpose
        object = ET.SubElement(service, "object")
        objectName = ET.SubElement(object, "objectName")
        objectName.text = ObjectSelected
        methodId = ET.SubElement(object, "methodID")
        methodId.text=MethodChar[1]
        checks = ET.SubElement(service, "checks")
        check = ET.SubElement(checks, "checks1", type="execute_result")
        check.text = unicode(expected)
    else:
        actionName = "TimeSleep"
        root = ET.Element("action", id=unicode(stepId ),description=unicode(desc))
        data_link = ET.SubElement(root, "data_link", name="DLMS_ANY1")
        funct = ET.SubElement(root, "function")
        funct.text = actionName
        paramAsXMl = ET.SubElement(root, "paramAsXml")
        result = ET.SubElement(root, "result")
        ok = ET.SubElement(result, "ok", ret="ok")
        default = ET.SubElement(result, "default", ret="nok")
        service = ET.SubElement(paramAsXMl, unicode(actionName))
        purposee = ET.SubElement(service, "purpose")
        purposee.text = purpose
        values = ET.SubElement(service, "values")
        value1 = ET.SubElement(values, "value1", Description="time_to_wait" )
        value1.text=inValue

    newpath = "TestCases\\"
    tree = ET.ElementTree(root)



    tree.write(newpath +"test_"+str(nbTest) + ".xml")
    easygui.msgbox("your file has been created successfully!", title="information")


    return TestCasesTree(request)

# ******************edit test
def editTestCase(request):
    logger.info("information")
    global FileName1
    global prdt
    global objectName
    OldStepId = request.POST.get("OldstepId", None)
    Oldpurpose=request.POST.get("Oldpurpose", None)
    OldExp = request.POST.get("OldExp", None)




    if request.method == "POST" and request.is_ajax():
        FileName1 = request.POST['id']
        logger.info(FileName1)
        # status = display(FileName1)
        status = ''

        path =  FileName1
        tree = ET.parse(path)
        root=tree.getroot()

        identifiant=root.get('id')
        descr=root.get('description')
        print descr
        prdt=root.get('product')
        logger.info(prdt)



        dataLinkName=root.find("data_link").get('name')
        function =root.find('function').text





        if function=="ActionRequest":

            paramAsXml=root.find('paramAsXml')
            for elt in paramAsXml.iter('ActionRequest'):
                for actionElt in elt.findall('purpose'):
                    purpose=actionElt.text
                    print purpose
                for o in elt.findall('object'):
                    for object in o.findall('objectName'):
                         objectName=object.text
                    for meth in o.findall('methodID'):
                        methodId=meth.text
                for ch in elt.findall('checks'):
                    for ch1 in ch.findall('checks1'):
                        typeCh=ch1.get('type')
                        checkRes=ch1.text
            result = root.find('result')
            for res in result.findall('ok'):
                ok=res.get('ret')
            for resn in result.findall('default'):
                default = resn.get('ret')
            return HttpResponse(simplejson.dumps(
                {'stat': status, 'identifiant': identifiant, 'dataLinkName': dataLinkName, 'function': function,
                 'purpose': purpose, 'objectName': objectName, 'methodId': methodId, 'typeCh': typeCh,
                 'checkRes': checkRes, 'ok': ok, 'default': default,'descr':descr,'prdt':prdt}), content_type='application/json')
        elif function=="WriteRequest":
            paramAsXml = root.find('paramAsXml')
            for elt in paramAsXml.iter('WriteRequest'):
                for actionElt in elt.findall('purpose'):
                    purpose = actionElt.text
                for o in elt.findall('object'):
                    for object in o.findall('objectName'):
                        objectName = object.text
                    for att in o.findall('AttributID'):
                        attributId=att.text
                for ch in elt.findall('checks'):
                    for ch1 in ch.findall('checks1'):
                        typeCh=ch1.get('type')
                        checkRes=ch1.text
                for val in elt.findall('values'):
                    for v in val.findall('value1'):

                        for typeVal in v:
                            typeval=typeVal.tag


                        for valName in v.findall(typeval):
                            valN=valName.get('name')
                            valV=valName.get('value')
            result = root.find('result')
            for res in result.findall('ok'):
                ok = res.get('ret')
            for resn in result.findall('default'):
                default = resn.get('ret')

            return HttpResponse(simplejson.dumps(
                {'stat': status, 'identifiant': identifiant, 'dataLinkName': dataLinkName, 'function': function,
                 'purpose': purpose, 'objectName': objectName,'attributId':attributId,'typeCh':typeCh,'checkRes':checkRes,
                 'descr':descr,'typeval':typeval,'valN':valN,'valV':valV,'ok':ok,'default':default,'prdt':prdt}), content_type='application/json')
        elif function=="ReadRequest":
            paramAsXml = root.find('paramAsXml')
            for elt in paramAsXml.iter('ReadRequest'):
                for actionElt in elt.findall('purpose'):
                    purpose = actionElt.text
                for o in elt.findall('object'):
                    for object in o.findall('objectName'):
                        objectName = object.text
                    for att in o.findall('AttributID'):
                        attributId = att.text
                for ch in elt.findall('checks'):
                    for ch1 in ch.findall('checks1'):
                        typeCh = ch1.get('type')
                        for typeVal in ch1:
                            typeval=typeVal.tag
                            print typeval
                        for valName in ch1.findall(typeval):
                            valN=valName.get('name')
                            valV=valName.get('value')
            result = root.find('result')
            for res in result.findall('ok'):
                ok = res.get('ret')
            for resn in result.findall('default'):
                default = resn.get('ret')

            return HttpResponse(simplejson.dumps(
                {'stat': status, 'identifiant': identifiant, 'dataLinkName': dataLinkName, 'function': function,
                 'purpose': purpose, 'objectName': objectName, 'attributId': attributId, 'typeCh': typeCh,

                 'descr': descr, 'typeval': typeval, 'valN': valN, 'valV': valV, 'ok': ok, 'default': default,'prdt':prdt }),
                content_type='application/json')
        elif function=="TimeSleep":
            paramAsXml = root.find('paramAsXml')
            for elt in paramAsXml.iter('TimeSleep'):
                for actionElt in elt.findall('purpose'):
                    purpose = actionElt.text
                for values in elt.findall('values'):
                    for value1 in values.findall('value1'):

                        valueT=value1.text
            result = root.find('result')
            for res in result.findall('ok'):
                ok = res.get('ret')
            for resn in result.findall('default'):
                default = resn.get('ret')
            return HttpResponse(simplejson.dumps(
                {'stat': status, 'identifiant': identifiant, 'dataLinkName': dataLinkName, 'function': function,
                 'purpose': purpose,'valueT':valueT, 'ok': ok, 'default': default, 'descr':descr,'prdt':prdt}),
                content_type='application/json')



    else:
        status = {'fileContent': 'Fail Loading Content'}
        return HttpResponse(status)
# ****************************************edit test
def editTest(request,template_name="listTestCases.html"):
    test=request.POST.get("test", None)

    action=request.POST.get("action", None)

    pathXml =str(test)
    OldStepId = request.POST.get("OldstepId", None)
    NewStepId=request.POST.get("stepId", None)

    print OldStepId,NewStepId

    Oldpurpose = request.POST.get("Oldpurpose", None)
    Newpurpose = request.POST.get("purpose", None)
    print Oldpurpose,Newpurpose


    OldExp = request.POST.get("OldExp", None)
    NewExp = request.POST.get("expected", None)



    print OldExp, NewExp

    Olddesc = request.POST.get("Olddesc", None)
    Newdesc = request.POST.get("desc", None)
    print Olddesc, Newdesc


    OldinValue=request.POST.get("OldinValue", None)
    NewinValue = request.POST.get("inValue", None)
    print OldinValue, NewinValue

    OldexValue=request.POST.get("OldexValue", None)
    NewexValue = request.POST.get("exValue", None)
    print NewexValue

    if (OldStepId != NewStepId) | (Oldpurpose != Newpurpose) | (OldExp != NewExp) | (Olddesc != Newdesc) | (
        OldinValue != NewinValue) |(OldexValue != NewexValue):
        for file in os.listdir("TestCases\\"):

            test1=pathXml.split("\\")
            if file == test1[2]:

                    os.chmod(pathXml, 0o777)
                    filePDt = open(pathXml, "r+")
                    tree = ET.parse(filePDt)
                    root = tree.getroot()
                    paramAsXml = root.find('paramAsXml')

                    root.set('description',Newdesc)
                    root.set('id', NewStepId)

                    for elt in paramAsXml.iter('ActionRequest'):
                        for actionElt in elt.findall('purpose'):
                            actionElt.text=Newpurpose
                        for ch in elt.findall('checks'):
                            for ch1 in ch.findall('checks1'):
                                ch1.text=NewExp
                    if action=="WriteRequest":
                        for elt in paramAsXml.iter('WriteRequest'):
                            for actionElt in elt.findall('purpose'):
                                actionElt.text = Newpurpose
                            for ch in elt.findall('checks'):
                                for ch1 in ch.findall('checks1'):
                                    ch1.text = NewExp

                            for val in elt.findall('values'):
                                for v in val.findall('value1'):

                                    for typeVal in v:
                                        typeval=typeVal.tag

                                    for valName in v.findall(typeval):

                                        valName.set('value',NewinValue)
                    elif action=="ReadRequest":
                        for elt in paramAsXml.iter('ReadRequest'):

                            for actionElt in elt.findall('purpose'):
                                actionElt.text = Newpurpose
                            for ch in elt.findall('checks'):

                                for ch1 in ch.findall('checks1'):
                                    for typeVal in ch1:
                                        typeval = typeVal.tag


                                    for valName in ch1.findall(typeval):

                                        valName.set('value',NewexValue)
                    elif action=="TimeSleep":
                        for elt in paramAsXml.iter('TimeSleep'):
                            for actionElt in elt.findall('purpose'):
                                actionElt.text = Newpurpose
                            for val in elt.findall('values'):
                                for v in val.findall('value1'):
                                    v.text=NewinValue

                    filePDt.close()
                    filePDt=open(pathXml,'w+')
                    filePDt.write(tostring(root))
                    filePDt.close()

    easygui.msgbox("Your TestCase FIle has been modified successfully!", title="information")
    return TestCasesTree(request)


def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
        #only for windows
    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

@csrf_protect
@login_required(login_url="login")
def dmtt(request, template_name="dmtt.html"):

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
    port = serial_ports()
    tree = listtreefunction(PRODUCTS)
    tree1['port'] = port
    tree1['tree'] = tree

    return render(request,template_name,{'tree1': tree1,}, )
def DMTTExecution(request, template_name="dmtt.html"):
    result = ''
    input = 'DMTT'
    if request.method == "POST" and request.is_ajax():
        port = request.POST['port']
        baud = request.POST['baud']
        ser = serial.Serial(port, baud, timeout=1)
        # open the serial port
        if ser.isOpen():
            result += ser.name + ' is open with baudrate ' + baud + ' ... \n'

        if input == 'exit':
            ser.close()
            exit()
        else:
            result += 'Message sent\t' + input.encode('ascii') + '\n'
            ser.write(input.encode('ascii') + '\r\n')
            out = ser.read()
            result += 'Receiving...' + out
    return  HttpResponse(result)

def productName(request):
    global association
    association = ''
    if request.method == "POST" and request.is_ajax():
        productName = request.POST['productName']
        pathAssociation = os.path.join(PRODUCTS, productName, 'product_config.xml')
        docAss = minidom.parse(pathAssociation)
        assocs = docAss.getElementsByTagName('clientAdress')
        for assocs1 in assocs:
            assoc = assocs1.getElementsByTagName('client')
            for assoc1 in assoc:
                sid = assoc1.getAttribute('adress')
                name = assoc1.getAttribute('associationName')
                association += "{}.{}".format(sid, name)+"\n"
            association = association
    return HttpResponse(association)
# *************************************tc firmware
nb=0
def Tc_Firmware(request,template_name="welcome.html"):
    # *******getting post values*****
    imageT=request.POST.get('imageT')
    global nb

    Upfile = request.FILES['Upfile']
    activeF=request.POST.get('activeF')
    version=request.POST.get('version')
    firmwareV=request.POST.get('firmwareV')
    crc=request.POST.get('crc')
    HEX=""
    chaine=""
    for c in crc:
        HEX = hex(ord(c))
        x=HEX.index('x')
        chaine+=HEX[x+1:len(HEX)]+';'





    # i = int(crc, 16)
    # i=str(crc).decode("hex")
    # print i



    # ********************************
    script = ET.Element("script")
    root = ET.SubElement(script,"Action", id="Step3.1_init_firmware_transfer")
    data = ET.SubElement(root, "data_link", name="DLMS_ANY1")
    function=ET.SubElement(root, "function")
    function.text = "InitFirmwareUpgrade"
    param=ET.SubElement(root, "ParamAsXml")
    InitFirmwareUpgrade = ET.SubElement(param, "InitFirmwareUpgrade")
    purpose = ET.SubElement(InitFirmwareUpgrade, "purpose")
    purpose.text="Initial APP firmware transferring"
    values=ET.SubElement(InitFirmwareUpgrade, "values")
    value1=ET.SubElement(values, "value1",description="obj_name")
    value1.text=imageT
    value2 = ET.SubElement(values, "value2", description="dest_dat")
    value2.text = str(Upfile)
    checks = ET.SubElement(InitFirmwareUpgrade, "checks")
    checks1 = ET.SubElement(checks, "checks1", type="execute_result")
    checks1.text = "True"
    result= ET.SubElement(root, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")
    # *****************************part 2
    root2 = ET.SubElement(script, "Action", id="Step3.2_check_image_transfer_status")
    data2 = ET.SubElement(root2, "data_link", name="DLMS_ANY1")
    function2 = ET.SubElement(root2, "function")
    function2.text = "ReadRequest"
    param2 = ET.SubElement(root2, "ParamAsXml")
    ReadRequest = ET.SubElement(param2, "ReadRequest")
    purpose = ET.SubElement(ReadRequest, "purpose")
    purpose.text = "Get status of image transfer"
    object = ET.SubElement(ReadRequest, "Object")
    objectN= ET.SubElement(object, "ObjectName")
    objectN.text=imageT
    attribute = ET.SubElement(object, "AttributeId")
    attribute.text = "6"
    chekcs2 = ET.SubElement(ReadRequest, "Checks")
    checks21=ET.SubElement(chekcs2, "Checks1",type="getting_result")
    enum=ET.SubElement(checks21, "enumerated",value="1")
    result = ET.SubElement(root2, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")

    # *************************************part3***************
    root3 = ET.SubElement(script, "Action", id="Step3.3_download_APP_firmware")
    data3 = ET.SubElement(root3, "data_link", name="DLMS_ANY1")
    function3 = ET.SubElement(root3, "function")
    function3.text = "FirmwareUpgrade"
    param3 = ET.SubElement(root3, "ParamAsXml")
    FirmwareUpgrade = ET.SubElement(param3, "FirmwareUpgrade")
    purpose = ET.SubElement(FirmwareUpgrade, "purpose")
    purpose.text = "Download APP firmware"
    values = ET.SubElement(FirmwareUpgrade, "values")
    value1=ET.SubElement(values, "value1",description="obj_name")
    value1.text=imageT
    value2 = ET.SubElement(values, "value2", description="dest_dat")
    value2.text = str(Upfile)
    value3 = ET.SubElement(values, "value3", description="pos_start")
    value3.text = "0"
    value4 = ET.SubElement(values, "value4", description="pos_end")
    value4.text = "0"
    chekcs3 = ET.SubElement(FirmwareUpgrade, "Checks")
    checck31 = ET.SubElement(chekcs3, "Checks1", type="execute_result")
    checck31.text="True"

    result = ET.SubElement(root3, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")

    # **************************************part4
    root4 = ET.SubElement(script, "Action", id="Step3.4_active_APP_firmware")
    data4 = ET.SubElement(root4, "data_link", name="DLMS_ANY1")
    function4 = ET.SubElement(root3, "function")
    function4.text = "FirmwareActive"
    param4 = ET.SubElement(root4, "ParamAsXml")
    FirmwareActive = ET.SubElement(param4, "FirmwareActive")
    purpose = ET.SubElement(FirmwareActive, "purpose")
    purpose.text = "Active the destination firmware version"
    values = ET.SubElement(FirmwareActive, "values")
    value1 = ET.SubElement(values, "value1", description="obj_name")
    value1.text = imageT

    chekcs3 = ET.SubElement(FirmwareActive, "Checks")
    checck31 = ET.SubElement(chekcs3, "Checks1", type="execute_result")
    checck31.text = "True"

    result = ET.SubElement(root4, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")

    # *************************************part 5
    root5 = ET.SubElement(script, "Action", id="Step3.5_get_current_APP_firmware")
    data5 = ET.SubElement(root5, "data_link", name="DLMS_ANY1")
    function2 = ET.SubElement(root5, "function")
    function2.text = "ReadRequest"
    param2 = ET.SubElement(root5, "ParamAsXml")
    ReadRequest = ET.SubElement(param2, "ReadRequest")
    purpose = ET.SubElement(ReadRequest, "purpose")
    purpose.text = "get current APP firmware version"
    object = ET.SubElement(ReadRequest, "Object")
    objectN = ET.SubElement(object, "ObjectName")
    objectN.text =unicode(activeF)
    attribute = ET.SubElement(object, "AttributeId")
    attribute.text = "2"
    chekcs2 = ET.SubElement(ReadRequest, "Checks")
    checks21 = ET.SubElement(chekcs2, "Checks1", type="getting_result",test_key_value="key_visiblestring")
    checks21.text=version

    result = ET.SubElement(root5, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")

    # ******************************************part6
    root6 = ET.SubElement(script, "Action", id="Step3.6_GetFirmwareVersionSignature1")
    data6 = ET.SubElement(root6, "data_link", name="DLMS_ANY1")
    function2 = ET.SubElement(root6, "function")
    function2.text = "ReadRequest"
    param2 = ET.SubElement(root6, "ParamAsXml")
    ReadRequest = ET.SubElement(param2, "ReadRequest")
    purpose = ET.SubElement(ReadRequest, "purpose")
    purpose.text = "get Firmware Version Signature1"
    object = ET.SubElement(ReadRequest, "Object")
    objectN = ET.SubElement(object, "ObjectName")
    objectN.text = unicode(firmwareV)
    attribute = ET.SubElement(object, "AttributeId")
    attribute.text = "2"
    chekcs2 = ET.SubElement(ReadRequest, "Checks")
    checks21 = ET.SubElement(chekcs2, "Checks1", type="getting_result")
    octetS=ET.SubElement(checks21, "octetstring", name="value",size="8",value=unicode(chaine))

    result = ET.SubElement(root6, "result")
    ok = ET.SubElement(result, "ok", ret="ok")
    default = ET.SubElement(result, "default", ret="nok")
    # **********************************************

    newpath = "TestCases\\"
    tree = ET.ElementTree(script)
    nb +=1

    tree.write(newpath + "TC_Firmware"+str(nb)+".xml")
    easygui.msgbox("Your TC_FirmwareFile has been created successfully!", title="information")



    return render  (request,template_name)



