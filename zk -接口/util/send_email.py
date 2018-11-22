import smtplib
from email.mime.text import MIMEText

#定义类自动发送测试结果邮件，收件人发件人写死的

class SendEmail(object):
     #邮件内容模板
    def send_main(self,pass_list,fail_list):
        pass_num = float(len(pass_list))    #成功数
        fail_num = float(len(fail_list))    #失败数
        count_num = pass_num+fail_num       #总数

        pass_result = "%.2f%%"%(pass_num/count_num*100)  #成功率
        fail_result= "%.2f%%"%(fail_num/count_num*100)  #失败率

        content = "此次一共运行接口个数为%s个，通过%s个，失败%s个，通过率为%s，失败率为%s"%(count_num,pass_num,fail_num,pass_result,fail_result)
        return content

    #发送邮件
    def send_Email(self,email_data):
         
        # 第三方 SMTP 服务
        mail_host="smtp.qq.com" #设置服务器"smtp.qq.com", 465
        mail_user="794140113"    #用户名
        mail_pass="qweqicybeeewmhkbeia886sa"          
        sender = '794140113@qq.com' #发件人
        receivers = '794140113@qq.com' # 接收邮件，可设置为你的QQ邮箱或者其他邮箱      
        message = MIMEText(email_data, 'plain', 'utf-8')
        message['From'] = sender
        message['To'] =  receivers        
        subject = '接口测试结果'
        message['Subject'] =  subject                                                      #Header(subject, 'utf-8')    
        try:
            smtpObj = smtplib.SMTP() 
            smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
            smtpObj.login(mail_user,mail_pass)  
            smtpObj.sendmail(sender, receivers, message.as_string())
            smtpObj.close()
            print ("邮件发送成功")
        except smtplib.SMTPException as e:           
            print (e)
            print ("Error: 无法发送邮件")


if __name__=='__main__':
    

    sd_email = SendEmail()
    cont = sd_email.send_main( [1,2,3],[7,5,3,2])
    sd_email.send_Email(cont)

