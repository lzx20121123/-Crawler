

class global_var(object):
    ID = '0'
    request_name='1'
    url = '2'
    run = '3'
    request_way = '4'
    header = '5'
    case_depend = '6'
    data_depend ='7'
    field_depend = '8'
    mysql='9'
    data = '10'
    expect = '11'
    result = '12'
    def get_id(self):
        return global_var.ID
        
    def get_requses_name(self):
        return global_var.request_name

    def get_url(self):
        return global_var.url

    def get_run(self):
        return global_var.run
    
    def get_requses_way(self):
        return global_var.request_way

    def get_header(self):
        return global_var.header

    def get_case_depend(self): 
        return global_var.case_depend

    def get_data_depend(self):
        return global_var.data_depend

    def get_field_depend(self):
        return global_var.field_depend

    def get_mysql(self):
        return global_var.mysql
    
    def get_data(self):
        return global_var.data

    def get_expect(self):
        return global_var.expect

    def get_result(self):
        return global_var.result
    


if __name__=='__main__':
    a = global_var()
    print (a.get_case_depend())