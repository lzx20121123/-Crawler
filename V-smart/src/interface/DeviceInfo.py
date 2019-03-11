#!usr/bin/python
# -*- coding: UTF-8 -*-

import interface.pull_pb2 as pull

class DeviceInfo(object):
    '''
    get the devices's info
    '''


    def getInfo(self, offset, count, gw_guid, app_id):
        lo = pull.PagingParam()
        lo.offset = int(offset)
        lo.count = int(count)
        
        do = pull.DeviceOverviewParam()
        do.gw_guid = gw_guid
        do.page_param.offset = lo.offset
        do.page_param.count= lo.offset
        do_data = do.SerializeToString()
        
        po = pull.PullServiceRequest()
        po.app_id = app_id
        po.action_type = pull.PullServiceRequest.DEVICE_OVERVIEW
        po.param = do_data
        
        po_data = po.SerializeToString()
        
        return po_data
        
    def getinfo_analyse(self, response):
        
        result = pull.PullServiceResponse()
        result.ParseFromString(response.content)
        
        return result