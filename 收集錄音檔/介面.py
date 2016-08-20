from django.shortcuts import render, redirect
from 收集錄音檔.models import 語料表
from 收集錄音檔.models import 語料表格


def 全部語料(request):
    return render(request, '全部.html', {
        '語料': 語料表.objects.all(),
    })


def 加語料(request, pk=None):
    if pk is not None:
        物件 = 語料表.objects.get(pk=pk)
    else:
        物件 = None
    if request.method == 'POST':
        print(request.FILES)
        表格 = 語料表格(request.POST, request.FILES, instance=物件)
        if 表格.is_valid():
            語料 = 表格.save()
            return redirect('看',語料.id)
    else:
        表格 = 語料表格(instance=物件)
    return render(request, '加.html', {
        '表格': 表格,
    })


def 看語料(request, pk):
    表格=語料表格(instance=語料表.objects.get(pk=pk))
    表格.fields['漢字'].disabled=True
    表格.fields['臺羅'].disabled=True
    表格.fields['音檔'].disabled=True
    表格.fields['備註'].disabled=True
    return render(request, '看.html', {
        '表格': 表格,
    })
