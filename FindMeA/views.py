import re
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth import models
from django.urls import reverse
from django.contrib.auth import authenticate, login
from FindMeA.models import Interest, UserProfile, Mentor, Notification
from django.contrib.auth import get_user_model

def homepage(request):
    
    userlogged = request.user
    user_name = userlogged
    uid = User.objects.get(username=user_name).id
    userobjects=UserProfile.objects.get(user=uid)
    allobjects = UserProfile.objects.all()
    user_interests = userobjects.user_interests.all()
    mentoring = userobjects.mentoring
    mentoring = mentoring.lower()
    recusers = []
    # all_users = get_user_model().objects.all()
    # all_users.delete("diya")
    # all_users.delete(user_name)
    # for i in all_users:
    #     for interest in i.user_interests:
    #         for user_int in user_interests:
    #             if interest == user_int:
    #                 recusers.append(i.username)
    #                 #all_users.delete(i.username)

    for interest in user_interests:
        sub_id = Interest.objects.get(interest_text=interest)
        pusers = UserProfile.objects.filter(user_interests=sub_id).exclude(user=request.user)
        for p in pusers:
            recusers.append(p)
    print(recusers)
    recusers = list(dict.fromkeys(recusers))
    print(recusers)
    try:
        user1 = recusers[0]
        u1interests = user1.user_interests.all()
        print(u1interests)
    except:
        user1 = "We are currently looking for more users for you"
        u1interests = "..."
    try: 
        user2 = recusers[1]
        u2interests = user2.user_interests.all()
    except:
        user2 = "We are currently looking for more users for you"
        u2interests = "..."
    try:
        user3 = recusers[3]
        u3interests = user3.user_interests.all()
        
    except:
        user3 = "We are currently looking for more users for you"
        u3interests = "..."

    notifications = Notification.objects.filter(recipient=userlogged)
    print(notifications)
    send = request.GET.get("send", '')

    print(send)
    if not request.user.is_authenticated:
        return load_login_page(request)
    return render(request, 'FindMeA/homepage.html', {"send":send, "notifications":notifications, "mentoring":mentoring, "u2interests":u2interests, "u3interests":u3interests, "username":user_name, "recusers":recusers, "user1":user1, "user2":user2, "user3":user3, "user_interests":user_interests, "u1interests":u1interests})
    
def browseusers(request):
    all_users = get_user_model().objects.all()
    # all_users.delete(all_users[0])
    print(all_users)
    userlogged = request.user
    userobjects = UserProfile.objects.all()
    
    # uid = User.objects.get(username=user).id
    # userobjects=UserProfile.objects.get(user=uid)
    notifications = Notification.objects.filter(recipient=userlogged)
    print(notifications)
    if not request.user.is_authenticated:
        return load_login_page(request)
    return render(request, 'FindMeA/browseusers.html', {"notifications":notifications, "userlogged":userlogged, "all_users":userobjects, "username":userlogged})
    

def signup(request):

    username = request.POST['username']
    password = request.POST['password']
    # email = request.POST['email']
    user = User.objects.create_user(username=username, password=password)
    if user is not None:
        login(request, user)
        return createyourprofile(request)
    

def load_login_page(request):
    print('In load_login_page')
    
    return render(request, 'FindMeA/login.html', {})

def verify_and_login(request):
    print("in login...")
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username= username, password= password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('FindMeA:homepage'))
    else:
        return HttpResponseRedirect(reverse('FindMeA:homepage'))

def createyourprofile(request):
    username = request.user
    mentorsubjects = Mentor.objects.all()
    interests = Interest.objects.all()
    yeargroups = ["Year 7", "Year 8", "Year 9", "Year 10", "Year 11", "Year 12", "Year 13"]
    if not request.user.is_authenticated:
        return load_login_page(request)
    return render(request, 'FindMeA/createyourprofile.html', {"yeargroups":yeargroups, "username":username, "interests":interests, "mentorsubjects":mentorsubjects})

def makeprofile(request):
    userlogged = request.user
    email_address = request.POST['Communicate']
    description = request.POST['Description']
    first_name = request.POST['Name']
    second_name = request.POST['Surname']
    mentoring = request.POST.get('mentoring')

    

    mentor_subjects = request.POST.getlist('mentors')
    print(mentor_subjects)
    # #if mentoring == "Yes":
    # #    for subject in mentorsubjects:
    # #        mentor_value = request.POST.get(subject.mentor_text)
    # #        if mentor_value:
    # #            print(mentor_value, end=', ')
    # #        if mentor_value != None:
    #             user_mentor_subjects.append(mentor_value)
    
    user_interests = request.POST.getlist('interests')
    print(user_interests)
    
    # for interest in interests:
    #     value = request.POST.get(interest.interest_text)
    #     if value:
    #         print(value, end=', ')
    #     if value != None:
    #         user_interests.append(value)
    useryear = request.POST['year']
    print(email_address)
    print(userlogged)
    new_user = userlogged.userprofile_set.create(year_group=useryear, mentoring = mentoring, email_address=email_address, description=description, first_name=first_name, second_name=second_name)
    # new_user = UserProfile(year_group = useryear, mentor_subjects = user_mentor_subjects, mentoring = mentoring, user_interests = user_interests, user=userlogged, email_address = email_address, description = description, first_name=first_name, second_name=second_name)
    # new_user.save()

    for i in user_interests:
        i_id = Interest.objects.get(interest_text=i).id
        new_user.user_interests.add(i_id)

    for ms in mentor_subjects:
        ms_id = Interest.objects.get(interest_text=ms).id
        new_user.mentor_subjects.add(ms_id)
    
    if not userlogged.is_authenticated:
        return load_login_page(request)
    else:
        return HttpResponseRedirect(reverse('FindMeA:homepage'))

def userprofile(request):
    user_name = request.GET['user']
    uid = User.objects.get(username=user_name).id
    userobjects=UserProfile.objects.get(user=uid)
    email = userobjects.email_address
    userlogged = request.user
    mentoring = userobjects.mentoring
    mentor_subjects = userobjects.mentor_subjects.all()
    #mentor_subjects = mentor_subjects.split("',")
    description = userobjects.description

    first_name = userobjects.first_name
    second_name = userobjects.second_name
    year_group = userobjects.year_group
    user_interests = userobjects.user_interests.all()
    print(user_interests)
    #user_interests = user_interests.split("',")
    #user_interests = user_interests.split("'")
    notifications = Notification.objects.filter(recipient=userlogged)
    print(notifications)

    if not request.user.is_authenticated:
        return load_login_page(request)
    return render(request, 'FindMeA/userprofile.html', {"notifications":notifications, "userlogged":userlogged, "year_group":year_group, "mentor_subjects":mentor_subjects, "user_name":user_name, "email":email, "description":description, "mentoring":mentoring, "first_name":first_name, "second_name":second_name, "user_interests":user_interests})
 
 
def findsomeone(request):
    username = request.user
    if not request.user.is_authenticated:
        return load_login_page(request)
    
    subjects = Interest.objects.all()
    print(subjects)
    notifications = Notification.objects.filter(recipient=username)
    print(notifications)

    return render(request, 'FindMeA/findsomeone.html', {"notifications":notifications, "username":username, "subjects":subjects})

def possiblementors(request):
    username = request.user
    if not request.user.is_authenticated:
        return load_login_page(request)
    msubjects = Interest.objects.all()

    all_users= get_user_model().objects.all()
    print(all_users)
    wantsubject = request.POST.get('subjects')
    print(f'wantsubject: {wantsubject}')
    listpossmentors = []
    sub_id = Interest.objects.get(interest_text=wantsubject)
    possmentors = UserProfile.objects.filter(mentor_subjects=sub_id, mentoring='yes').exclude(user=request.user)
    print(possmentors)

    for mentor in possmentors:
        if mentor.user != username:
            listpossmentors.append(mentor.user)
    print(listpossmentors)

    notifications = Notification.objects.filter(recipient=username)
    print(notifications)

    return render(request, 'FindMeA/possiblementors.html', {"notificiations":notifications, "username":username, "subjects":msubjects, "possmentors":possmentors, "wantsubject": wantsubject, })

def findfriend(request):
    userlogged = request.user
    if not userlogged.is_authenticated:
        return load_login_page(request)
    notifications = Notification.objects.filter(recipient=userlogged)
    print(notifications)
    return render(request, "FindMeA/findfriend.html", {"notifications":notifications, "userlogged":userlogged})

def mentorme(request):
    userlogged = request.user
    if not userlogged.is_authenticated:
        return load_login_page(request)
    userrec = request.GET['user']
    print(userrec)
    rec = User.objects.get(username=userrec)
    new_notification = Notification(sender=userlogged, recipient=rec, message = "Can you mentor me?")
    new_notification.save()
    # success = "yes"

    #return HttpResponseRedirect(reverse('FindMeA:homepage'))
    return redirect("/FindMeA/homepage?send=success")

def splashpage(request):
    
    # return HttpResponseRedirect(reverse('FindMeA:splashpage'))
    return render(request, "FindMeA/splashpage.html", {})