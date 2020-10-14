#def deployApplications():
#    names = ['one_app_test', 'two_app_test', 'three_app_test']
#    for name in names:
#        AdminApp.install('/home/phillip/Downloads/mmistia-fogi-das-integration-ear-1.0.3.ear','[-node phillip-Latitude-7400Node03 -cell phillip-Latitude-7400Node03Cell -server server1 -appname' + name + ']')
import os
import sys
import time


try:
            application_properties = []
            ear = '.ear'
            try:
                application_properties = sys.argv;
                print(application_properties)
                if len(application_properties) > 0  and (ear in application_properties[1]):
                    application_name = application_properties[0]
                    application_path = '/home/phillip/eclipse-workspace/' + application_name
                    print('PATH: ' + application_path)
                    try:
                        print AdminApp.uninstall(application_name)
                    except:
                        print('this app is not installed: ' + application_name)
                    try:
                        print AdminApp.install(application_path,'[-node phillip-Latitude-7400Node03 -cell phillip-Latitude-7400Node03Cell -server server1 -appname ' + str(application_name) + ' -defaultbinding.virtual.host default_host -usedefaultbindings]')
                    except java.lang.Exception as err:
                        print(err)
                else:
                    if (ear not in application_properties[0]):
                        print('please check the extension of the application, it should end with ".ear"')
                    else:
                        print('no arguments were passed through the console')
            except:
                print('something went wrong :(')
except:
    print("An exception occurred trying to install application")
finally:
    print('finally clause')
    AdminConfig.save()
