from django.db import models
from django.forms.models import ModelForm


class 語料表(models.Model):
    收錄時間 = models.DateField(auto_now_add=True)
    上尾修改時間 = models.DateField(auto_now=True)

    漢字 = models.TextField(blank=True)
    臺羅 = models.TextField(blank=True)
    音檔 = models.FileField(blank=True)

    備註 = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return '{} {}'.format(''.join(self.漢字.split()[:1]), self.備註)


class 語料表格(ModelForm):

    class Meta:
        model = 語料表
        fields = '__all__'
