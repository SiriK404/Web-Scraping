
import json
import xlsxwriter
import requests

#First fetch the business directory according to category id
url= 'https://www.jewelxy.com/skirmish/fe_api/business/api_business_directory_filter_with_token' #url to fetch list of businesses according to the category
url1='https://www.jewelxy.com//skirmish/fe_api_v2/business/api_view_profile_by_biz_unique_id_login'#url to fetch details of business according to the 'bd_uniqur_url' parameter'

headers={ 'User-Agent': 'okhttp/3.12.0',
         'Mobile': 'Android, App Version : 2.0.12, Android Os Version : 9, Menufacture : xiaomi Redmi Note 5 Pro'
        }


data = {"start_limit":0,                                    #data for url
        "category_id":'',
        "wut_token":'fLVRajaPxHNO9SxkJGDXlgwsVKqviB4xmZpxjzmQgaFq2cKLSnJeEgHz075iIaQ5afDtO0j5aYvcbfY4DHihXZRY6XhP78VinyLcy5hI4MUf2TkGACYyCQxJNOyVWudk2ZwB4Oj8AenD7IkIkigX9OGWDeSzI5UL4qm9eGhPUFt2nOKI71FgPldsz52ibW4gnqpC6Gs1mV3JJOrRP67Frk81qajB7nRvOh8VYAWkw03gOu7DBej2zr4ZBoBJLsf'
        }

data1= {"wut_token_ex":1,                                  #data for url1
        "bd_unique_url":'',
        "wut_token":'fLVRajaPxHNO9SxkJGDXlgwsVKqviB4xmZpxjzmQgaFq2cKLSnJeEgHz075iIaQ5afDtO0j5aYvcbfY4DHihXZRY6XhP78VinyLcy5hI4MUf2TkGACYyCQxJNOyVWudk2ZwB4Oj8AenD7IkIkigX9OGWDeSzI5UL4qm9eGhPUFt2nOKI71FgPldsz52ibW4gnqpC6Gs1mV3JJOrRP67Frk81qajB7nRvOh8VYAWkw03gOu7DBej2zr4ZBoBJLsf'
        }

#response1 = requests.post(url1, data=data1, headers=headers)
#d1= json.loads(response1.text)
#k1= d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['bd_business_name']
#print(k1)
#k2=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['name']
#print(k2)
#k3=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['surname']
#print(k3)
#k4=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['bd_mobile']
#print(k4)
#k5=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_website_url']
#print(k5)
#k6=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address'][0]['ba_city']
#print(k6)
#k7=d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address'][0]['email_details']
#print(k7)
row =0

col=0
workbook = xlsxwriter.Workbook('data1.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(row, col,'bd_unique_url')
col=1
worksheet.write(row,col,'bd_business_name')
col=2
worksheet.write(row,col,'name')
col=3
worksheet.write(row,col,'surname')
col=4
worksheet.write(row,col,'bd_mobile')
col=5
worksheet.write(row,col,'biz_website_url')
col=6
worksheet.write(row,col,'ba_city')
col=7
worksheet.write(row,col,'email_details')
col=8
worksheet.write(row,col,'plan')
i=500
while i < 600:
        data['category_id']=i
        response = requests.post(url,data=data,headers=headers)
        d = json.loads(response.text)
        #print(d)
        k=d['DATA']
        #print(k)
        index=0
        no_of_elements=len(k)




        while index < no_of_elements:
                row+=1
                col=0
                worksheet.write(row,col,k[index]['bd_unique_url'])
                k8 = k[index]['bd_pm_title']
                col=8
                worksheet.write(row, col, k8)
                data1['bd_unique_url']=k[index]['bd_unique_url']
                response1 = requests.post(url1, data=data1, headers=headers)
                d1= json.loads(response1.text)
                k1 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['bd_business_name']
                col=1
                worksheet.write(row, col, k1)
                k2 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['name']
                col = 2
                worksheet.write(row, col, k2)
                k3 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['surname']
                col = 3
                worksheet.write(row, col, k3)
                k4 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['bd_mobile']
                if len(k4)!=0:
                        col = 4
                        worksheet.write(row, col, k4)
                else:
                        d2= d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address'][0]['mobile_details']
                        if len(d2)!= 0 :
                                k4a=d2[0]['bap_country_code'] + d2[0]['bap_phone_code'] + d2[0]['bap_phone']
                                col=4
                                worksheet.write(row, col,k4a)
                        else :
                                d3 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address'][0]['phone_details']
                                if len(d3)!=0 :
                                        k4b = d3[0]['bap_country_code'] + d3[0]['bap_phone_code'] + d3[0]['bap_phone']
                                        col=4
                                        worksheet.write(row,col,k4b)
                                else:

                                        col = 4
                                        worksheet.write(row, col, 'phone number does not exist')

                k5 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_website_url']
                col = 5
                worksheet.write(row, col, k5)
                k6 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address']
                if len(k6)==0:
                        col = 6
                        worksheet.write(row, col,'address not present')
                else:
                        col = 6
                        worksheet.write(row, col,k6[0]['ba_city'])

                k7 = d1['DATA'][0]['business'][0]['DATA'][0]['business_details'][0]['DATA'][0]['biz_address']
                if len(k7)!=0:
                        d4=k7[0]['email_details']
                        if len(d4)== 0 :
                                col = 7

                                worksheet.write(row, col,'email not present')
                        else :
                                col = 7

                                worksheet.write(row, col,d4[0]['bae_email'])


                else:

                        col = 7

                        worksheet.write(row, col,'email not present')




                #print (k1)
                index += 1
        i +=1

workbook.close()
