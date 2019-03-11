#!usr/bin/python
# -*- coding: UTF-8 -*-

import interface.pull_pb2 as pull

class Login(object):
    '''
    login data convert
    '''
    
    def login_phone(self, phone_num, phone_id):
        lo = pull.LoginParam()
        lo.account = phone_num
        lo.login_type = pull.LoginParam.PHONE

        #SerializeToString
        lo_data = lo.SerializeToString()
        
        po = pull.PullServiceRequest()
        po.app_id = phone_id
        po.action_type = pull.PullServiceRequest.LOGIN
        po.param = lo_data
        
        po_data = po.SerializeToString()
        
        
        
        return po_data
    
    
    def login_phone_analyse(self, response):
        
        result = pull.PullServiceResponse()
        result.ParseFromString(response.content)
    
        login_res = pull.LoginResult()
        login_res.ParseFromString(result.result)
        
        return login_res.login_status