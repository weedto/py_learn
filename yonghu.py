# name = input('请输入用户名：')

# if 'A' <= name[0] <= 'Z':
#     count_num = 0
#     for x in name[1:]:
#         if '0' <= x <= '9':
#             count_num += 1
#         elif 'a' <= x <= 'z' or 'A' <= x <= 'Z':
#             pass
#         else:
#             print('不合法')
#             break
#     if count_num:
#         print('合法')
#     else:
#         print('不合法')

# else:
#     print('不合法')


# if(65 <= data.charCodeAt(i)&&data.charCodeAt(i) <= 90) { var flag = true;
#         for (var i = 0; i < data.length; i++) {
#             if (!((48 <= data.charCodeAt(i) && data.charCodeAt(i) <= 57) || (97 <= data.charCodeAt(i) && data.charCodeAt(i) <= 122))){
#                     console.log('不合法');
#                     flag = false;
#                     break;
#             }
# }
# if(flag){
#         console.log('合法');
#         }            
#     else{
#             console.log('不合法');
#         }


username = input('请输入用户名：')
if 'A' <= username[0] <= 'Z':
     count = 0     # 数字个数计数
     for x in username[1:]:
         if not('0' <= x <= '9' or 'a' <= x <= 'z' or 'A' <= x <= 'Z'):
             print('不合法')
             break
         else:
             if '0' <= x <= '9':
                 count += 1
     else:
         if count:
             print('登录成功！')
         else:
             print('用户名不合法！')
else:
     print('不合法')
