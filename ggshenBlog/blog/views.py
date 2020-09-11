# encoding:utf-8
import glob
import os, django, re, json
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPersonalBlog.settings')
django.setup()
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from blog.models import Article, MiniRecord, Photo, Video
import datetime, platform


# Windows, linux路径分开处理
if 'Windows' in platform.platform():
    # 获取照片数量
    path_photo_number = glob.glob(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), r'static\images\photo\*.jpg'))
    # 获取视频数量
    path_video_number = glob.glob(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), r'static\video\*.mp4'))
else:
    # 获取照片数量
    path_photo_number = glob.glob(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), r'static/images/photo/*.jpg'))
    # 获取视频数量
    path_video_number = glob.glob(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), r'static/video/*.mp4'))

def auth_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("/index/")
    else:
        return HttpResponse("用户名或密码错误")


def logout_view(request):
    logout(request)
    return HttpResponse("You're logged out.")


def user_login(request):
    return render(request, 'login.html')


# Create your views here.
@login_required
def index(request):

    dict_content = {}
    article_info = []
    article = Article.objects.all()
    # 上次更新时间赋初值
    last_date = datetime.date(1990, 1, 1)
    # 阅读量赋初值
    last_read = 0
    for art in article:
        article_info.append((art.title, art.title_zh, art.body, art.path, art.updateTime, art.category, art.like, art.read, art.author))
        # 对于名称为'个人博客，记录我及我爱之人的生活点滴！'的博客单独处理
        if art.title == 'MyPersonalBlog':
            dict_content['title003'] = art.title
            dict_content['title_zh003'] = art.title_zh
            dict_content['body003'] = art.body
            dict_content['path'] = art.path
            dict_content['updateTime003'] = art.updateTime
            dict_content['category003'] = art.category
            dict_content['like003'] = art.like
            dict_content['read003'] = art.read
        # 获取最新更新文章标题和html路径
        if art.updateTime > last_date:
            dict_content['newest_article_title_zh'] = art.title_zh
            dict_content['newest_article_path'] = art.path
        last_date = art.updateTime

        # 获取点击量最高的文章标题的html路径
        if art.read > last_read:
            dict_content['top_article_title_zh'] = art.title_zh
            dict_content['top_article_path'] = art.path
        last_read = art.read

    dict_content['article_info'] = article_info

    dict_content['count_article'] = Article.objects.count()
    dict_content['count_photo'] = len(path_photo_number)
    dict_content['count_video'] = len(path_video_number)
    dict_content['count_mini_record'] = MiniRecord.objects.count()

    return render(request, 'index.html', dict_content)


@login_required
def list(request):

    # 上次更新时间赋初值
    last_date = datetime.date(1990, 1, 1)
    # 阅读量赋初值
    last_read = 0

    dict_content = {}
    article_info = []
    article = Article.objects.all()
    for art in article:
        article_info.append((art.title, art.title_zh, art.body, art.path, art.updateTime, art.category, art.like, art.read, art.author))
        # 获取最新更新文章标题和html路径
        if art.updateTime > last_date:
            dict_content['newest_article_title_zh'] = art.title_zh
            dict_content['newest_article_path'] = art.path
        last_date = art.updateTime

        # 获取点击量最高的文章标题的html路径
        if art.read > last_read:
            dict_content['top_article_title_zh'] = art.title_zh
            dict_content['top_article_path'] = art.path
        last_read = art.read

    dict_content['article_info'] = article_info
    # dict_content['article_js'] = json.dumps(article_info[0])

    dict_content['count_article'] = Article.objects.count()
    dict_content['count_photo'] = len(path_photo_number)
    dict_content['count_video'] = len(path_video_number)
    dict_content['count_mini_record'] = MiniRecord.objects.count()

    return render(request, 'list.html', dict_content)


@login_required
def about(request):

    dict_about={}

    # 上次更新时间赋初值
    last_date = datetime.date(1990, 1, 1)
    # 阅读量赋初值
    last_read = 0

    article = Article.objects.all()
    for art in article:
        if art.updateTime > last_date:
            dict_about['newest_article_title_zh'] = art.title_zh
            dict_about['newest_article_path'] = art.path
        last_date = art.updateTime

        # 获取点击量最高的文章标题的html路径
        if art.read > last_read:
            dict_about['top_article_title_zh'] = art.title_zh
            dict_about['top_article_path'] = art.path
        last_read = art.read

    dict_about['count_article'] = Article.objects.count()
    dict_about['count_photo'] = len(path_photo_number)
    dict_about['count_video'] = len(path_video_number)
    dict_about['count_mini_record'] = MiniRecord.objects.count()

    return render(request, 'about.html', dict_about)


@login_required
def share(request):
    count_photo_db = Photo.objects.count()
    count_photo_folder = len(path_photo_number)
    if 'Windows' in platform.platform():
        lst_photo_title_folder = re.findall('\\\\\\\\\d+_(\w+_\d+).jpg', str(path_photo_number))
        lst_photo_name_folder = re.findall('\\\\\\\\(\w+_\d+.jpg)', str(path_photo_number))
        lst_photo_path = re.findall('\\\\\\\\(images\\\\\\\\photo\\\\.*?_\d+.jpg)', str(path_photo_number))
    else:
        lst_photo_title_folder = re.findall('images/photo/\d+_(.*?).jpg', str(path_photo_number))
        lst_photo_name_folder = re.findall('images/photo/(.*?.jpg)', str(path_photo_number))
        lst_photo_path = re.findall('(images/photo/.*?.jpg)', str(path_photo_number))
    # 每次刷新页面都重新从文件夹中更新文件到数据，再重数据库读取文件信息
    Photo.objects.all().delete()
    serial_num = 1
    for title, name, path in zip(lst_photo_title_folder, lst_photo_name_folder, lst_photo_path):
        Photo.objects.create(id=serial_num, name=name, title=title, path=path)
        serial_num += 1

    title_path = []
    dict_photo = {}
    this_photo = Photo.objects.all()
    for r in this_photo:
        title_path.append((r.title, r.path))
    dict_photo['title_path'] = title_path
    dict_photo['count_article'] = Article.objects.count()
    dict_photo['count_photo'] = len(path_photo_number)
    dict_photo['count_video'] = len(path_video_number)
    dict_photo['count_mini_record'] = MiniRecord.objects.count()

    return render(request, 'share.html', dict_photo)


@login_required
def infopic(request):
    count_video_db = Video.objects.count()
    count_video_folder = len(path_video_number)
    if 'Windows' in platform.platform():
        lst_video_title_folder = re.findall('\\\\\\\\(\w+).mp4', str(path_video_number))
        lst_video_name_folder = re.findall('\\\\\\\\(\w+.mp4)', str(path_video_number))
        lst_video_path = re.findall('\\\\\\\\(video\\\\\\\\.*?.mp4)', str(path_video_number))
    else:
        lst_video_title_folder = re.findall('video/(.*?).mp4', str(path_video_number))
        lst_video_name_folder = re.findall('video/(.*?.mp4)', str(path_video_number))
        lst_video_path = re.findall('(video/.*?.mp4)', str(path_video_number))
    print(lst_video_name_folder)
    print(lst_video_path)
    print(lst_video_title_folder)
    print(count_video_folder, count_video_db)
    # 每次刷新页面都重新从文件夹中更新文件到数据，再重数据库读取文件信息
    Video.objects.all().delete()
    serial_num = 1
    for title, name, path in zip(lst_video_title_folder, lst_video_name_folder, lst_video_path):
        Video.objects.create(id=serial_num, name=name, title=title, path=path)
        serial_num += 1

    name_title_path = []
    dict_video = {}
    this_video = Video.objects.all()
    for r in this_video:
        name_title_path.append((r.name, r.title, r.path))
    dict_video['name_title_path'] = name_title_path

    return render(request, 'infopic.html', dict_video)


@login_required
def time(request):
    time_body = []
    dict_record = {}
    this_record = MiniRecord.objects.all()
    for r in this_record:
        time_body.append((r.recordTime, r.body))
    dict_record['time_body'] = time_body
    dict_record['count_article'] = Article.objects.count()
    dict_record['count_photo'] = len(path_photo_number)
    dict_record['count_video'] = len(path_video_number)
    dict_record['count_mini_record'] = MiniRecord.objects.count()

    # 上次更新时间赋初值
    last_date = datetime.date(1990, 1, 1)
    # 阅读量赋初值
    last_read = 0

    article = Article.objects.all()
    for art in article:
        if art.updateTime > last_date:
            dict_record['newest_article_title_zh'] = art.title_zh
            dict_record['newest_article_path'] = art.path
        last_date = art.updateTime

        # 获取点击量最高的文章标题的html路径
        if art.read > last_read:
            dict_record['top_article_title_zh'] = art.title_zh
            dict_record['top_article_path'] = art.path
        last_read = art.read

    return render(request, 'time.html', dict_record)


@login_required
def search(request):
    q = request.GET.get('search')
    print("要搜索的内容为:%s"%q)
    error_msg = ''

    if not q:
        error_msg = '请输入关键词'
        return render(request, 'results.html', {'error_msg': error_msg})

    match_article = []
    article_list = Article.objects.filter(title__icontains=q)
    if article_list:
        for art in article_list:
            match_article.append((art.title, art.title_zh, art.body, art.path, art.updateTime, art.category, art.like, art.read, art.author))

    return render(request, 'results.html', {'error_msg': error_msg,
                                               'match_article': match_article})
