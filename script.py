#def deployApplications():
#    names = ['one_app_test', 'two_app_test', 'three_app_test']
#    for name in names:
#        AdminApp.install('/home/phillip/Downloads/mmistia-fogi-das-integration-ear-1.0.3.ear','[-node phillip-Latitude-7400Node03 -cell phillip-Latitude-7400Node03Cell -server server1 -appname' + name + ']')
import os
import sys
import time


try:
        application_name = []
        try:
            application_name = os.listdir(sys.argv[1])
            applications_size = len(application_name)
            app_passed_from_command_line = str(sys.argv[2])
            ear_location = '/home/phillip/Downloads/' + str(sys.argv[2])
            app_installed = 'this application did not install'
            print('LOG: are we here? ' + str(application_name) + ' : ' + str(applications_size))
            if applications_size > 0:
                print('LOG: ' + str(application_name))
                print('=================================================================================================')
                print AdminApp.list()
                print('=================================================================================================')

                for app in application_name:
                    print('LOG: installing this application: ' + app)
                    try:
                        #DeploymentStatus =  AdminApp.getDeployStatus(app)
                        if app_installed in str(DeploymentStatus):
                            print('this app is not installed')
                        else:
                            print('this app is installed ')
                            print AdminApp.uninstall(app)
                        #print(DeploymentStatus)
                        print('localtion of the ear file: ' + ear_location)
                        if app_passed_from_command_line == app:
                            print AdminApp.install(ear_location,'[-node phillip-Latitude-7400Node03 -cell phillip-Latitude-7400Node03Cell -server server1 -appname ' + str(app) +'was9' + ']')
                        else:
                            print('app will be skipped: ' + app)
                        #we need you to start
                    except:
                        print('this application did not install: ' + app)
                for app in application_name:
                    print('Log: removing application: ' + str(application))
                    try:
                        print AdminApp.uninstall(app)
                    except:
                        print('could not remove application: ' + str(app))
            else:
             print('we need application names phillip')
        except:
            print('this application did not install: ' + app)
except:
    print("An exception occurred trying to install application")
finally:
    AdminConfig.save()

def _removeApplications(applicationArray):
    for application in applicationArray:
        try:
            print('Log: removing application: ' + str(application))
            print AdminApp.uninstall(application)
        except:
            print('Log: could not uninstall application: ' + str(application))
