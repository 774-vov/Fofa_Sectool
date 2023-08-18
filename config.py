#输出文件的路径
output_folder = './result/'
#时段查询的循环上限,防止数量一直不够导致无限循环
loop_max = 1000
#你能免费看到的最大页数,一页20条
page_max = 1
#只需要你的token就能运行,也可自定义header
headers={
    'cookie':'fofa_token="eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6Mjk0NjMyLCJtaWQiOjEwMDE2Njc5NywidXNlcm5hbWUiOiI3NzQiLCJleHAiOjE2OTIzNzA3MTV9.HW-7XVfO8USPL27tbHfehLQQRRg6xB82OIgep4N7vWhB6rNJsmrEq8GidVcZ8klbdFTd9Q30AE-9v0jOPv36xw"'
}