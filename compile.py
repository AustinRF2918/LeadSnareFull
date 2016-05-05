import os

compilePath = 'GlobalStylesheet/sass/app.scss'
filePaths = ['LeadSnareLogin/css/app.css', 'LeadSnareSignUp/css/app.css', 'LeadSnareDashboardPeople/css/app.css']

for file in filePaths:
    os.system("sass " + compilePath + " " + file)
