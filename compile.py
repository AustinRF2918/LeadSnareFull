import os

compilePath = 'GlobalStylesheet/sass/app.scss'
filePaths = ['LeadSnareLogin/css/app.css', 'LeadSnareSignUp/css/app.css', 'LeadSnareDashboardPeople/css/app.css', 'LeadSnareLandingPage/css/app.css']

x = input('Enter script or all');

if (x == 'all'):
    for file in filePaths:
        os.system("sass " + compilePath + " " + file)
else:
    os.system("sass " + compilePath + " " + filePaths[int(x)])
