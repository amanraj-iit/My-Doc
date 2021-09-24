from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from joblib import dump, load

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score

def Check(request):
    #cont = {'a' : 'Submit not pressed'}
    return render(request, 'check.html')


def predictHeart(request):
    context = {'a' : 'Submit pressed'}
    #print(request)

    if(request.method == 'POST'):
        tmp = {}
        tmp['age'] = request.POST.get('age')
        tmp['sex'] = request.POST.get('sex')
        tmp['cp'] = request.POST.get('cp')
        tmp['trestbps'] = request.POST.get('trestbps')
        tmp['chol'] = request.POST.get('chol')
        tmp['fbs'] = request.POST.get('fbs')
        tmp['restecg'] = request.POST.get('restecg')
        tmp['thalach'] = request.POST.get('thalach')
        tmp['exang'] = request.POST.get('exang')
        tmp['oldPeak'] = request.POST.get('oldPeak')
        tmp['slope'] = request.POST.get('slope')
        tmp['ca'] = request.POST.get('ca')
        tmp['thal'] = request.POST.get('thal')

    testData = pd.DataFrame({'x':tmp}).transpose()
    filename = "./models/heart.csv"
    data = pd.read_csv(filename)
    data = pd.read_csv(filename)

    data.dropna()
    y = data['target']
    x = data.drop(['target'], axis = 1)

    x_normal = (x - x.mean())/(x.max() - x.min())
    x_train, x_test, y_train, y_test = train_test_split(x_normal, y, train_size = 0.7, test_size = 0.3, random_state = 42)

    model2 = RandomForestClassifier(n_estimators = 200, max_depth = 15, random_state = 0)
    model2.fit(x_train, y_train)
    y_pred2 = model2.predict(x_test)
    prediction = model2.predict(testData)[0]
    context = {'prediction' : prediction}
    return render(request, 'check.html', context)