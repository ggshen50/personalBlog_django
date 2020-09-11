# coding:utf-8

import webbrowser
import glob
import os, django, re
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyPersonalBlog.settings')
django.setup()
from blog.models import Article


def generate_html():
    article = Article.objects.all()
    for art in article:
        # 命名生成的html
        GEN_HTML = art.title + ".html"
        # 打开文件，准备写入
        f = open(os.path.join('../static/html/',GEN_HTML), 'w', encoding='utf-8')

        # 写入HTML界面中
        message = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <link rel="stylesheet" href="../css/my_style.css">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="../css/base.css" rel="stylesheet">
            <script src="../js/jquery.min.js" type="text/javascript"></script>
            <script type="text/javascript" src="../js/comm.js"></script>
            <title>%s</title>
        </head>
        <body>
            <div class="container">
                <div class="row">
                    <div class="panel panel-primary">
                        <div class="panel-heading">
                                <h1 style="text-align: center">%s</h1>
                        </div>
                        <div class="content">
                            <pre style="word-wrap: break-word; white-space: pre-wrap; white-space: -moz-pre-wrap">%s</pre>
                        </div>
                    </div>
                </div>
            </div>
        </body>
        </html>
        """ %(art.title_zh, art.title_zh, art.body)

        # 写入文件
        f.write(message)
        # 关闭文件
        f.close()

generate_html()