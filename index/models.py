from DjangoUeditor.models import UEditorField
from django.db import models

class Article(models.Model):
    title = models.CharField(u'博客标题', max_length=100)
    category = models.CharField(u'博客标签', max_length=100, blank=True)
    pub_date = models.DateTimeField(u'发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now_add=True, null=True)
    # content = models.TextField(blank=True, null=True)
    content = UEditorField(u"文章正文", height=300, width=1000, default=u'', blank=True, imagePath="uploads/index/images/",
                           toolbars='besttome', filePath='uploads/index/files/')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = '文章'
        verbose_name_plural = verbose_name



