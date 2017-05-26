from django.shortcuts import render



def index(req):
    '''
    首页
    '''
    return render(req, "web/index.html", locals())


def apply(req):
    '''
    本研申请
    '''
    return render(req, "web/application.html", locals())


def information(req):
    '''
    资讯中心
    '''
    return render(req, "web/information.html", locals())


def information_detail(req):
    '''
    资讯详情
    '''
    return render(req, "web/information_detail.html", locals())


def guidance(req):
    '''
    学术辅导
    '''
    return render(req, "web/guidance.html", locals())


def tour(req):
    '''
    游学之旅
    '''
    return render(req, "web/tour.html", locals())


def certification(req):
    '''
    学历学位认证
    '''
    return render(req, "web/certification.html", locals())


def live(req):
    '''
    生活辅助
    '''
    return render(req, "web/live.html", locals())
