from django.http.request import HttpHeaders
from django.http.response import HttpResponse, HttpResponseNotAllowed, JsonResponse
from rest_framework.parsers import JSONParser
from .serializers import *
from django.shortcuts import redirect, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status
from siwes_portal.views import *
from datetime import datetime
# Create your views here.
from.models import *

serializer_class = StudentSerializers
serializer_class_adm = SupSerializers
serializer_class_repo = ReportSerializers
serializer_class_work = OrganizationSerializers
serializer_class_mssg = MessageSerializers
serializer_class_mssg_count = MessageCountSerializers


def s_signin(request):
    # print(request.method)
    # print(request.GET.get('password'))
    std = student.objects.filter(matric=request.GET.get(
        'matric'), password=request.GET.get('password'))
    if std.exists():
        request.session['todays_date'] = datetime.today().strftime('%Y-%m-%d')
        std_serializer = serializer_class(std, many=True)
        _id = std_serializer.data[0]['student_id']
        org = organization.objects.filter(student_id=_id)

        std1 = serializer_class_work(org, many=True)

        if org.exists():
            request.session['o_data'] = std1.data[0]
        else:
            request.session['o_data'] = ""

        request.session['s_data'] = std_serializer.data[0]

        sd = message.objects.filter(
            sup_id=std_serializer.data[0].get("sup_id")).order_by('-id')
        if sd.exists():
            std_serializer = serializer_class_mssg(sd, many=True)
            # print(len(std_serializer.data))
            request.session['s_data']['mssg'] = std_serializer.data
            sup_serializer = serializer_class_adm(supervisor.objects.filter(
                sup_id=std_serializer.data[0].get("sup_id")), many=True)

            request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                "last_name") + " "+sup_serializer.data[0].get(
                "first_name")
            request.session['s_data']['mssg_no'] = len(std_serializer.data)
            request.session['repo'] = "nope"
            print(request.session)
        # return Response({'Message': ''}, status=status.HTTP_200_OK)
        return redirect(Student_home)
        # return render(request, "siwes_portal/s_info.html")
    return render(request, "siwes_portal/signin.html", {"message": "No Such Student Found. Please, Try Again!"})
    # return JsonResponse("No such Student", safe=False)


def s_signup(request):
    # print(request.method)
    # print(request.data)
    serializer = serializer_class(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        # return JsonResponse("Succesfully Added", safe=False)
        return redirect(Student_Signin)
        # return Response({'Message': ''}, status=status.HTTP_200_OK)
    # print(serializer.errors)
    return render(request, "siwes_portal/signup.html", {"message": "Wrong Input Somewhere. Please, Try Again!"})
    # return JsonResponse("Failed", safe=False)


def s_update(request):
    if 'o_data' and 's_data' in request.session:
        # print(request.method)
        std = student.objects.filter(
            matric=request.session['s_data']['matric'], password=request.session['s_data']['password'])
        if std.exists():
            std = student.objects.get(
                matric=request.session['s_data']['matric'], password=request.session['s_data']['password'])
            std.first_name = request.POST.get('first_name')
            std.last_name = request.POST.get('last_name')
            std.department = request.POST.get('department')
            std.password = request.POST.get('password')
            pwd = std.password
            std.save()
            std = student.objects.filter(
                matric=request.session['s_data']['matric'], password=pwd)
            if std.exists():
                std_serializer = serializer_class(std, many=True)
                _id = std_serializer.data[0]['student_id']
                org = organization.objects.filter(student_id=_id)

                std1 = serializer_class_work(org, many=True)
                request.session['s_data'] = std_serializer.data[0]
                # print(org)
                if org.exists():
                    print(std1.data)
                    request.session['o_data'] = std1.data[0]
                else:
                    request.session['o_data'] = ""

                request.session.modified = True
                request.session['s_data']['first_name'] = request.POST.get(
                    'first_name')
                request.session['s_data']['last_name'] = request.POST.get(
                    'last_name')
                request.session['s_data']['phone'] = request.POST.get('phone')
                request.session['s_data']['password'] = request.POST.get(
                    'password')
                request.session.modified = True
                return render(request, "siwes_portal/s_change.html", {"message": "Updated Successfully", "err": "No"})
            else:
                return render(request, "siwes_portal/s_change.html", {"message": "Something wrong, Try again!", "err": "Yes"})
        else:
            return render(request, "siwes_portal/s_change.html", {"message": "No such Student", "err": "Yes"})
    else:
        return redirect(Student_404)


def a_update(request):
    if 'a_data' in request.session:
        # print(request.method)
        std = supervisor.objects.filter(
            email=request.session['a_data']['email'], password=request.session['a_data']['password'])
        if std.exists():
            std = supervisor.objects.get(
                email=request.session['a_data']['email'], password=request.session['a_data']['password'])
            std.first_name = request.POST.get('first_name')
            std.last_name = request.POST.get('last_name')
            std.phone = request.POST.get('phone')
            std.password = request.POST.get('password')
            pwd = std.password
            std.save()
            std = supervisor.objects.filter(
                email=request.session['a_data']['email'], password=pwd)
            print(std.exists())
            if std.exists():
                request.session['a_data']['first_name'] = request.POST.get(
                    'first_name')
                request.session['a_data']['last_name'] = request.POST.get(
                    'last_name')
                request.session['a_data']['phone'] = request.POST.get('phone')
                request.session['a_data']['password'] = request.POST.get(
                    'password')
                request.session.modified = True
                return render(request, "siwes_portal/a_change.html", {"message": "Updated Successfully", "err": "No"})
            else:
                return render(request, "siwes_portal/a_change.html", {"message": "Something wrong, Try again!", "err": "Yes"})
        return render(request, "siwes_portal/a_change.html", {"message": "Can't find student", "err": "Yes"})
        # return JsonResponse("No such Student", safe=False)
    else:
        return redirect(Admin_404)


def s_report(request):
    if 'o_data' and 's_data' in request.session:
        # print
        serializer = serializer_class_repo(data=request.POST)
        # print(serializers)
        if serializer.is_valid():
            # return JsonResponse("Report Sent", safe=False)
            rqy_repo = report.objects.filter(
                student_id=request.session['s_data']['student_id'], date_signed=datetime.today().strftime('%Y-%m-%d'))
            print(datetime.today().strftime('%Y-%m-%d'))
            if rqy_repo.exists():
                request.session['repo'] = False
                request.session.modified = True
            else:
                serializer.save()
                request.session['repo'] = True
                request.session.modified = True
        else:
            request.session['repo'] = "gffjjh"
            request.session.modified = True

        # print(request.session['repo'])
        return redirect(Student_report)
        # return Response({'Message': ''}, status=status.HTTP_200_OK)
        # print(serializer.errors)
    else:
        return redirect(Student_404)


def delete_m(request):
    if 'a_data' in request.session:
        req1 = message.objects.filter(id=request.POST.get('id'))
        if req1.exists():
            req1 = message.objects.get(id=request.POST.get('id'))
            sd = message.objects.filter(
                sup_id=request.session['s_data']["sup_id"]).order_by('-id')
            if sd.exists():
                std_serializer = serializer_class_mssg(sd, many=True)
                req1.delete()
                request.session['s_data']['mssg'] = std_serializer.data
                request.session.modified = True
                return render(request, "siwes_portal/s_message.html", {"message": "Deleted Successfully", "err": "No"})
            else:
                return render(request, "siwes_portal/s_message.html", {"message": "Already Deleted", "err": "Yes"})
        else:
            return render(request, "siwes_portal/s_message.html", {"message": "Message Never Existed", "err": "Yes"})


def s_work(request):
    if 'o_data' and 's_data' in request.session:
        # print(request.method)
        # print(request.data)
        _id = request.session['s_data']['student_id']
        org = organization.objects.filter(student_id=_id)

        std1 = serializer_class_work(org, many=True)
        # print(org)
        if org.exists():
            org = organization.objects.get(
                student_id=request.session['s_data']['student_id'])
            org.org_name = request.POST.get('org_name')
            org.address = request.POST.get('address')
            org.email = request.POST.get('email')
            org.phone = request.POST.get('phone')
            org.department = request.POST.get('department')
            org.job_desc = request.POST.get('job_desc')
            org.date_start = request.POST.get('date_start')
            org.date_end = request.POST.get('date_end')
            org.lga = request.POST.get('lga')
            org.save()

            org = organization.objects.filter(student_id=_id)
            std1 = serializer_class_work(org, many=True)
            request.session['o_data'] = std1.data[0]
            return redirect(Student_work)
        else:
            # request.session['o_data'] = ""
            serializer = serializer_class_work(data=request.POST)
            # print(serializers)
            if serializer.is_valid():
                serializer.save()
                # return JsonResponse("Succesfully Added", safe=False)
                request.session['o_data'] = std1.data[0]
                return redirect(Student_work)
                # return Response({'Message': ''}, status=status.HTTP_200_OK)
            # print(serializer.errors)
            return JsonResponse("Failed", safe=False)
    else:
        return redirect(Student_404)


def s_logout(request):
    if 'o_data' and 's_data' in request.session:
        del request.session["o_data"]
        del request.session["s_data"]
        del request.session['repo']
        del request.session['todays_date']
        return redirect(Student_Signin)
    return redirect(Student_404)


def a_signin(request):
    # print(request.method)
    # print(request.GET.get('password'))
    adm = supervisor.objects.filter(email=request.GET.get(
        'email'), password=request.GET.get('password'))
    if adm.exists():
        adm_serializer = serializer_class_adm(adm, many=True)
        # _id = adm_serializer.data[0]['student_id']\
        supervisor_id = adm_serializer.data[0].get("sup_id")
        request.session["found"] = ""
        st1 = student.objects.filter(
            sup_id=supervisor_id)
        if st1.exists():
            stdnt = serializer_class(st1, many=True)
            # print(stdnt.data)
            request.session['a_std'] = stdnt.data
        else:
            request.session['a_std'] = ""
        request.session['a_data'] = adm_serializer.data[0]
        # return Response({'Message': ''}, status=status.HTTP_200_OK)
        return redirect(Admin_home)
        # return render(request, "siwes_portal/s_info.html")
    return render(request, "siwes_portal/a_signin.html", {"message": "Supervisor Dose't Exit. Please, Try Again!"})
    # return JsonResponse("No such Student", safe=False)


def a_signup(request):
    # print(request.method)
    # print(request.data)
    serializer = serializer_class_adm(data=request.POST)
    if serializer.is_valid():
        serializer.save()
        # return JsonResponse("Succesfully Added", safe=False)
        return redirect(Admin_Signin)
        # return Response({'Message': ''}, status=status.HTTP_200_OK)
    # print(serializer.errors)
    return render(request, "siwes_portal/a_signin.html", {"message": "Invalid Input Somewhere. Please, Try Again!"})
    # return JsonResponse("Failed", safe=False)


def find_st(request):
    req = student.objects.filter(matric=request.POST.get("matric"))
    if req.exists():
        st1 = serializer_class(req, many=True)
        request.session['found'] = st1.data[0]
        return redirect(Admin_register_student)
    else:
        request.session["found"] = ""
        request.session.modified = True

        return render(request, "siwes_portal/a_report.html", {"message": "Can't find Student with such matric number!", "err": "Yes"})


def register_st(request):
    req = student.objects.filter(matric=request.POST.get("matric"))
    if req.exists():
        std = student.objects.get(matric=request.POST.get("matric"))
        std.sup_id = request.session['a_data']['sup_id']
        std.save()
        # print(request.session['a_data']['sup_id'])
        st1 = student.objects.filter(
            sup_id=request.session['a_data']['sup_id'])
        if st1.exists():
            stdnt = serializer_class(st1, many=True)
            # print(stdnt.data)
            request.session['a_std'] = stdnt.data
            return render(request, "siwes_portal/a_report.html", {"message": "Registered Successfully", "err": "No"})
        else:
            request.session["found"] = ""
            request.session.modified = True
            return render(request, "siwes_portal/a_report.html", {"message": "Something Wrong, Try again!", "err": "Yes"})
        # return redirect(Admin_register_student)
    # return redirect(Admin_register_student)
    return render(request, "siwes_portal/a_report.html", {"message": "Student Not Found!", "err": "Yes"})


def a_logout(request):
    if 'a_data' in request.session:
        del request.session["a_data"]
        del request.session["found"]
        del request.session["a_std"]
        return redirect(Admin_Signin)
    return redirect(Admin_404)


def message_st(request):
    if 'a_data' in request.session:
        serializer = serializer_class_mssg(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            # request.session['s_data']['mssg_no']
            # ser = serializer_class(student.objects.filter(
            #     matric=request.session['s_data']['matric']), many=True)
            # print(ser.data[0].get('sup_id'))
            req = message_count.objects.filter(
                sup_id=request.session['a_data']['sup_id'])
            if req.exists():
                print("hh1")
                req = message_count.objects.get(
                    sup_id=request.session['a_data']['sup_id'])
                req.sup_id = request.session['a_data']['sup_id']
                req.count = int(req.count) + 1
                req.save()
                return render(request, "siwes_portal/a_message.html", {"message": "Sent Successfully", "err": "No"})
            else:
                data = {
                    'sup_id': request.session['a_data']['sup_id'],
                    'count': 1
                }
                serializer = serializer_class_mssg_count(data=data)
                if serializer.is_valid():
                    serializer.save()
                return render(request, "siwes_portal/a_message.html", {"message": "Sent Successfully", "err": "No"})
            # return redirect(Admin_msg)
        return render(request, "siwes_portal/a_message.html", {"message": "Something wrong Somewhere. Please, Try Again!", "err": "Yes"})
        # return JsonResponse("Failed", safe=False)
    return redirect(Admin_404)
