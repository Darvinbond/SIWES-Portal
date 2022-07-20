from django.shortcuts import render, redirect
from api.models import *
# from api.views import *
from api.serializers import *
from datetime import datetime

serializer_class = StudentSerializers
serializer_class_adm = SupSerializers
serializer_class_repo = ReportSerializers
serializer_class_work = OrganizationSerializers
serializer_class_mssg = MessageSerializers


def Admin_home(request):
    if 'a_data' in request.session:
        return render(request, "siwes_portal/a_info.html")
    else:
        return redirect(Admin_404)


def Student_change(request):
    if 'o_data' and 's_data' in request.session:
        request.session['repo'] = "nope"
        std = student.objects.filter(
            matric=request.session['s_data']['matric'])
        if std.exists():
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
                request.session['s_data']['mssg'] = std_serializer.data
                sup_serializer = serializer_class_adm(supervisor.objects.filter(
                    sup_id=std_serializer.data[0].get("sup_id")), many=True)

                request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                    "last_name") + " "+sup_serializer.data[0].get(
                    "first_name")
                req1 = message.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                count = req1.count()
                req2 = message_count.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                if req2.exists():
                    mm = message_count.objects.get(
                        sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                    request.session['s_data']['mssg_no'] = mm.count
                    mm.save()

            return render(request, "siwes_portal/s_change.html")
    else:
        return redirect(Student_404)


def Admin_change(request):
    if 'a_data' in request.session:
        return render(request, "siwes_portal/a_change.html")
    else:
        return redirect(Admin_404)


def Student_report(request):
    if 'o_data' and 's_data' in request.session:
        request.session['todays_date'] = datetime.today().strftime('%Y-%m-%d')
        std = student.objects.filter(
            matric=request.session['s_data']['matric'])
        if std.exists():
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
                request.session['s_data']['mssg'] = std_serializer.data
                sup_serializer = serializer_class_adm(supervisor.objects.filter(
                    sup_id=std_serializer.data[0].get("sup_id")), many=True)

                request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                    "last_name") + " "+sup_serializer.data[0].get(
                    "first_name")
                req1 = message.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                count = req1.count()
                req2 = message_count.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                if req2.exists():
                    mm = message_count.objects.get(
                        sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                    request.session['s_data']['mssg_no'] = mm.count
                    mm.save()

            return render(request, "siwes_portal/s_report.html")
    else:
        return redirect(Student_404)


def Student_work(request):
    if 'o_data' and 's_data' in request.session:
        request.session['repo'] = "nope"
        std = student.objects.filter(
            matric=request.session['s_data']['matric'])
        if std.exists():
            std_serializer = serializer_class(std, many=True)
            _id = std_serializer.data[0]['student_id']
            org = organization.objects.filter(student_id=_id)

            std1 = serializer_class_work(org, many=True)

            if org.exists():
                request.session['o_data'] = std1.data[0]
            else:
                request.session['o_data'] = ""

            request.session['s_data'] = std_serializer.data[0]
            # rqy_repo = report.objects.filter(
            #     student_id=request.session['s_data']['student_id'], date_signed=datetime.today().strftime('%Y-%m-%d'))
            # if rqy_repo.exists():
            #     request.session['s_data']['sent_repo'] = False
            # else:
            #     request.session['s_data']['sent_repo'] = True

            sd = message.objects.filter(
                sup_id=std_serializer.data[0].get("sup_id")).order_by('-id')
            if sd.exists():
                std_serializer = serializer_class_mssg(sd, many=True)
                request.session['s_data']['mssg'] = std_serializer.data
                sup_serializer = serializer_class_adm(supervisor.objects.filter(
                    sup_id=std_serializer.data[0].get("sup_id")), many=True)

                request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                    "last_name") + " "+sup_serializer.data[0].get(
                    "first_name")
                req1 = message.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                count = req1.count()
                req2 = message_count.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                if req2.exists():
                    mm = message_count.objects.get(
                        sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                    request.session['s_data']['mssg_no'] = mm.count
                    mm.save()

            return render(request, "siwes_portal/st_w_details.html")
    else:
        return redirect(Student_404)


def Student_404(request):
    return render(request, "siwes_portal/a_404.html")


def Admin_404(request):
    return render(request, "siwes_portal/404.html")


def Admin_404(request):
    return render(request, "siwes_portal/a_404.html")


def Admin_msg(request):
    return render(request, "siwes_portal/a_message.html")


def Student_msg(request):
    std = student.objects.filter(
        matric=request.session['s_data']['matric'])
    if std.exists():
        request.session['repo'] = "nope"
        std_serializer = serializer_class(std, many=True)
        _id = std_serializer.data[0]['student_id']
        org = organization.objects.filter(student_id=_id)

        std1 = serializer_class_work(org, many=True)

        if org.exists():
            request.session['o_data'] = std1.data[0]
        else:
            request.session['o_data'] = ""

        request.session['s_data'] = std_serializer.data[0]
        # rqy_repo = report.objects.filter(
        #     student_id=request.session['s_data']['student_id'], date_signed=datetime.today().strftime('%Y-%m-%d'))
        # if rqy_repo.exists():
        #     request.session['s_data']['sent_repo'] = True
        # else:
        #     request.session['s_data']['sent_repo'] = False

        sd = message.objects.filter(
            sup_id=std_serializer.data[0].get("sup_id")).order_by('-id')
        if sd.exists():
            std_serializer = serializer_class_mssg(sd, many=True)
            request.session['s_data']['mssg'] = std_serializer.data
            sup_serializer = serializer_class_adm(supervisor.objects.filter(
                sup_id=std_serializer.data[0].get("sup_id")), many=True)

            request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                "last_name") + " "+sup_serializer.data[0].get(
                "first_name")
            req2 = message_count.objects.filter(
                sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
            if req2.exists():
                mm = message_count.objects.get(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                mm.count = 0
                request.session['s_data']['mssg_no'] = mm.count
                mm.save()

        return render(request, "siwes_portal/s_message.html")


def Admin_register_student(request):
    if 'a_data' in request.session:
        return render(request, "siwes_portal/a_report.html")
    else:
        return redirect(Admin_404)


def Admin_student(request):
    if 'a_data' in request.session:
        return render(request, "siwes_portal/a_w_details.html")
    else:
        return redirect(Admin_404)


def Student_Signup(request):
    return render(request, "siwes_portal/signup.html")


def Admin_Signup(request):
    return render(request, "siwes_portal/a_signup.html")


def Student_Signin(request):
    return render(request, "siwes_portal/signin.html")

def Main(request):
    return render(request, "siwes_portal/main.html")

def Admin_Signin(request):
    return render(request, "siwes_portal/a_signin.html")


def Student_home(request):
    if 'o_data' and 's_data' in request.session:
        std = student.objects.filter(
            matric=request.session['s_data']['matric'])
        if std.exists():
            request.session['repo'] = "nope"
            std_serializer = serializer_class(std, many=True)
            _id = std_serializer.data[0]['student_id']
            org = organization.objects.filter(student_id=_id)

            std1 = serializer_class_work(org, many=True)

            if org.exists():
                request.session['o_data'] = std1.data[0]
            else:
                request.session['o_data'] = ""

            request.session['s_data'] = std_serializer.data[0]
            # rqy_repo = report.objects.filter(
            #     student_id=request.session['s_data']['student_id'], date_signed=datetime.today().strftime('%Y-%m-%d'))
            # if rqy_repo.exists():
            #     request.session['s_data']['sent_repo'] = True
            # else:
            #     request.session['s_data']['sent_repo'] = False

            sd = message.objects.filter(
                sup_id=std_serializer.data[0].get("sup_id")).order_by('-id')
            if sd.exists():
                std_serializer = serializer_class_mssg(sd, many=True)
                request.session['s_data']['mssg'] = std_serializer.data
                sup_serializer = serializer_class_adm(supervisor.objects.filter(
                    sup_id=std_serializer.data[0].get("sup_id")), many=True)

                request.session['s_data']['mssg_sup'] = sup_serializer.data[0].get(
                    "last_name") + " "+sup_serializer.data[0].get(
                    "first_name")
                req1 = message.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                count = req1.count()
                req2 = message_count.objects.filter(
                    sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                print(request.session['s_data']['mssg'][0].get('sup_id'))
                if req2.exists():
                    mm = message_count.objects.get(
                        sup_id=request.session['s_data']['mssg'][0].get('sup_id'))
                    request.session['s_data']['mssg_no'] = mm.count
                    mm.save()
                else:
                    pass
            else:
                pass

            return render(request, "siwes_portal/s_info.html")
    else:
        return redirect(Student_404)
