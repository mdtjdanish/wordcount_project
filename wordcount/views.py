from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def count(request):
    fulltext = request.GET['fulltext']
    words = fulltext.split()
    word_dic = {}
    for word in words:
        # checking
        if word in word_dic:
            word_dic[word] += 1
            # increase
        else:
            word_dic[word] = 1
    sortedwords = sorted(
        word_dic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': fulltext, 'count': len(words), 'sortedwords': sortedwords})
