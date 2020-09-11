import MyPersonalBlog.urls
from blog.models import Article, MiniRecord, Photo, Video

# 添加结果_01
# Article.objects.create(id='002',title='我的征程',author='ggshen', read=3, like=1, category='diary', updateTime='2020-2-20')
# Article.objects.create(id='003',title='个人博客，记录我及我爱之人的生活点滴！',body='第一个个人博客，希望通过这种方式，使自己更加能够珍惜现在拥有的，珍惜身边的人。不叹人世沧桑，但求知心共度！', author='ggshen', read=8, like=5, category='漫生活', updateTime='2020-2-13')
# MiniRecord.objects.create(id='001', body='开始博客的探索之路', recordTime='2020-02-11')
# MiniRecord.objects.create(id='002', body='录入第一篇思念博文-一路走好!', recordTime='2020-02-11')
# MiniRecord.objects.create(id='003', body='开始创建自己的博客', recordTime='2020-02-11')
# MiniRecord.objects.create(id='004', body='梳理并更新相册，录入59张家庭照片', recordTime='2020-02-12')
# MiniRecord.objects.create(id='005', body='开始将博客适配Django框架', recordTime='2020-02-19')
# MiniRecord.objects.create(id='006', body='Django Sqlite3数据读写成功，并将数据展示到页面上', recordTime='2020-02-20')
MiniRecord.objects.create(id='008', body='static文件夹中照片、视频更新到数据库，再展示到页面成功', recordTime='2020-02-23')

# 添加结果_02
# b1 = Article(id='001',title='一路走好',author='ggshen', read=5, like=3, category='diary', updateTime='2020-2-20')
# b1.save()

# 删除结果
# Article.objects.filter(name__contains="我的征程").delete()

# 更新结果_01
# Article.objects.filter(title__contains="我的征程").update(author='ShenJunyan', read=8, like=2)
# MiniRecord.objects.filter(id='007').update(recordTime='2020-02-21')
# import glob, re
# path_photo_number = glob.glob('../static/images/photo/*.jpg')
# print(path_photo_number)
# print(re.findall('\\\\\\\\(.*?)_\d+.jpg', str(path_photo_number)))

# 更新结果02
# art = Article.objects.get(title="一路走好")
# # art.title = "Django基础教程"
# art.updateTime = "2013-03-16"
# print(art.updateTime)
# art.save()
