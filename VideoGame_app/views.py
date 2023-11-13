from django.contrib import messages
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from VideoGame_app.models import Game, User


def HomePage(request):
    return render(request, 'HomePage.html')


def showGame(request):
    showall = Game.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'showGame.html', context)


def sortGame(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = Game.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'sortGame.html', context)
    else:
        return render(request, 'sortGame.html')


def insertGame(request):
    if request.method == "POST":
        if request.POST.get('game_id') and request.POST.get('game_name') and request.POST.get(
                'age_restriction') and request.POST.get('banned_regions') and request.POST.get(
            'genre') and request.POST.get('price') and request.POST.get('system_requirements') and request.POST.get(
            'game_ratings'):
            saverecord = Game()
            saverecord.game_id = request.POST.get('game_id')
            saverecord.game_name = request.POST.get('game_name')
            saverecord.age_restriction = request.POST.get('age_restriction')
            saverecord.banned_regions = request.POST.get('banned_regions')
            saverecord.genre = request.POST.get('genre')
            saverecord.price = request.POST.get('price')
            saverecord.system_requirements = request.POST.get('system_requirements')
            saverecord.game_ratings = request.POST.get('game_ratings')

            allval = Game.objects.all()

            for i in allval:
                if int(i.game_id) == int(request.POST.get('game_id')):
                    messages.warning(request, 'Game already exists....!');
                    return render(request, 'insertGame.html')

            saverecord.save()
            messages.success(request, 'Game ' + saverecord.game_name + ' is saved succesfully!!')
            return render(request, 'insertGame.html')
    else:
        return render(request, 'insertGame.html')


def editGame(request, id):
    editGameObj = Game.objects.get(game_id=id)

    context = {
        "game": editGameObj
    }
    return render(request, 'editGame.html', context)


def updateGame(request, id):
    originalGame = Game.objects.get(game_id=id)
    Gname = request.POST.get("game_name")
    Gage = request.POST.get("age_restriction")
    Gban = request.POST.get("banned_regions")
    Ggenre = request.POST.get("genre")
    Gprice = request.POST.get("price")
    Gsysre = request.POST.get("system_requirements")
    Gratings = request.POST.get("game_ratings")

    originalGame.game_name = Gname
    originalGame.age_restriction = Gage
    originalGame.banned_regions = Gban
    originalGame.genre = Ggenre
    originalGame.price = Gprice
    originalGame.system_requirements = Gsysre
    originalGame.game_ratings = Gratings
    originalGame.save()
    messages.success(request, 'Record updates succesfully!!')
    return render(request, 'editGame.html', {"Game": updateGame})


def delGame(request, id):
    delGameObj = Game.objects.get(game_id=id)
    context = {
        "Game": delGameObj
    }
    return render(request, 'delGame.html', context)


def deletedGame(request, id):
    delGameObj = Game.objects.get(game_id=id)
    delGameObj.delete()
    showall = Game.objects.all()
    messages.success(request, 'Record deleted succesfully!!')
    return render(request, 'delGame.html', {"Game": delGameObj})


def showUser(request):
    showall = User.objects.all()
    context = {
        'data': showall
    }
    return render(request, 'showUser.html', context)


def insertUser(request):
    if request.method == "POST":
        if request.POST.get('user_id') and request.POST.get('user_name') and request.POST.get(
                'age') and request.POST.get('user_location') and request.POST.get('game_id'):
            saverecord = User()
            saverecord.user_id = request.POST.get('user_id')
            saverecord.user_name = request.POST.get('user_name')
            saverecord.age = request.POST.get('age')
            saverecord.user_location = request.POST.get('user_location')
            saverecord.game_id = request.POST.get('game_id')

            allval = User.objects.all()

            for i in allval:
                if int(i.user_id) == int(request.POST.get('user_id')):
                    messages.warning(request, 'User already exists....!');
                    return render(request, 'insertUser.html')

            saverecord.save()
            messages.success(request, 'user ' + saverecord.user_name + ' is saved succesfully!!')
            return render(request, 'insertUser.html')
    else:
        return render(request, 'insertUser.html')


def sortUser(request):
    if request.method == "POST":
        if request.POST.get('Sort'):
            type = request.POST.get('Sort')
            sorted = User.objects.all().order_by(type)
            context = {
                'data': sorted
            }
            return render(request, 'sortUser.html', context)
    else:
        return render(request, 'sortUser.html')


def editUser(request, id):
    editUserObj = User.objects.get(user_id=id)
    context = {
        "User": editUserObj
    }
    return render(request, 'editUser.html', context)


def updateUser(request, id):
    originalUser = User.objects.get(user_id=id)
    Uname = request.POST.get("user_name")
    Uage = request.POST.get("age")
    Ulocat = request.POST.get("user_location")
    Ugid = request.POST.get("game_id")

    originalUser.user_name = Uname
    originalUser.age = Uage
    originalUser.user_location = Ulocat
    originalUser.game_id = Ugid
    originalUser.save()
    messages.success(request, 'Record updates succesfully!!')
    return render(request, 'editUser.html', {"User": originalUser})


def delUser(request, id):
    delUserObj = User.objects.get(user_id=id)
    context = {
        "User": delUserObj
    }
    return render(request, 'delUser.html', context)


def deletedUser(request, id):
    delUserObj = User.objects.get(user_id=id)
    delUserObj.delete()
    showall = User.objects.all()
    messages.success(request, 'Record deleted succesfully!!')
    return render(request, 'delUser.html', {"User": delUserObj})

def InputCustomQuery(request):
    return render(request, 'Query.html', {})

def runQueryGame(request):
    raw_query = "select \"game\".\"game_id\",\"game\".\"game_name\" from \"game\" "

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'Query.html', {'data': alldata})



def ProcessCustomQuery(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'runQueryGame.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

def runQueryUser(request):
    raw_query = "select \"user\".\"user_id\",\"user\".\"user_name\" from \"user\" "

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()

    return render(request, 'QueryUser.html', {'data': alldata})

def ProcessCustomQueryforuser(request):
    raw_query = request.POST.get('query')

    cursor = connection.cursor()
    cursor.execute(raw_query)
    alldata = cursor.fetchall()
    colnames = [desc[0] for desc in cursor.description]
    print(colnames)
    print(alldata)

    return render(request, 'runQueryUser.html', {'data':alldata,'colnames':colnames, 'lencol':range(len(colnames))})

def InputCustomQueryUser(request):
    return render(request, 'QueryUser.html', {})