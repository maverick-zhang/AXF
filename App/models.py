from django.db import models


class Main(models.Model):

    img = models.CharField(max_length=255)
    name = models.CharField(max_length=64)
    trackid = models.IntegerField(default=1)

    class Meta:
        abstract = True


class MainWheel(Main):

    """
    insert into axf_wheel(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031716035274.jpg@90Q.jpg",
    "酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/2017031710450787.jpg@90Q.jpg","优选圣女果","21869"),
    ("http://img01.bqstatic.com//upload/activity/2017030714522982.jpg@90Q.jpg","伊利酸奶大放价","21862"),
    ("http://img01.bqstatic.com//upload/activity/2017032116081698.jpg@90Q.jpg","鲜货直供－窝夫小子","21770"),
    ("http://img01.bqstatic.com//upload/activity/2017032117283348.jpg@90Q.jpg","鲜货直供－狼博森食品","21874");
    """
    class Meta:
        db_table = 'axf_wheel'


class MainNav(Main):
    """
    insert into axf_nav(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017032016495169.png",
    "每日必抢","21851"),("http://img01.bqstatic.com//upload/activity/2016121920130294.png","每日签到","21753"),
    ("http://img01.bqstatic.com//upload/activity/2017010517013925.png","鲜货直供","21749"),
    ("http://img01.bqstatic.com//upload/activity/2017031518404137.png","鲜蜂力荐","21854");

    """
    class Meta:
        db_table = "axf_nav"


class MustBuy(Main):

    """
    insert into axf_mustbuy(img,name,trackid) values("http://img01.bqstatic.com//upload/activity/2017031715194326.
    jpg@90Q.jpg","酸奶女王","21870"),("http://img01.bqstatic.com//upload/activity/cms_118826_1489742316.jpg@90Q",
    "鲜果女王","21861"),("http://img01.bqstatic.com//upload/activity/2017031011044918.jpg@90Q.jpg","麻辣女王","21866"),
    ("http://img01.bqstatic.com//upload/activity/2017022318314545.jpg@90Q.jpg","鲜货直供－果析","21858");

    """

    class Meta:
        db_table = "axf_mustbuy"

