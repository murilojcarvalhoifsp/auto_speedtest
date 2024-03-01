import csv
import time
from datetime import datetime
from subprocess import run, PIPE

class Speed:
    def __init__(self):
        self.timestamp = ''
        self.latency = 0
        self.download_Bps = 0
        self.upload_Bps = 0
        self.download_Mbps = 0
        self.upload_Mbps = 0
        self.isp = ''
        self.server_id = ''
        self.server_host = ''
        self.server_name = ''
        self.server_location = ''

    def speed_test(self):
        print('Testando a velocidade ...')
        comando = ["speedtest", "--format", "json"]
        execucao = run(comando, stdout=PIPE, stderr=PIPE)
        # print(execucao.stdout)
        if(execucao.returncode == 0):
            print('Teste de velocidade realizado com sucesso.')
            execucao_str = execucao.stdout.decode()
            # print(execucao_str)
            execucao_str = execucao_str.replace('null', 'None') #Modifica para datatype compatível com Python
            execucao_str = execucao_str.replace('false', 'False')   #Modifica para datatype compatível com Python
            execucao_str = execucao_str.replace('true', 'True') #Modifica para datatype compatível com Python
            execucao_dict = eval(execucao_str)
            # print(execucao_dict)
            self.timestamp = execucao_dict["timestamp"]
            self.latency = execucao_dict["ping"]["latency"]
            self.download_Bps = execucao_dict["download"]["bandwidth"]
            self.upload_Bps = execucao_dict["upload"]["bandwidth"]
            self.download_Mbps = self.download_Bps/125000
            self.upload_Mbps = self.upload_Bps/125000
            self.isp = execucao_dict["isp"]
            self.server_id = execucao_dict["server"]["id"]
            self.server_host = execucao_dict["server"]["host"]
            self.server_name = execucao_dict["server"]["name"]
            self.server_location = execucao_dict["server"]["location"]
        else:
            print('Falha de conexao.')
            self.timestamp = ''
            self.latency = 0
            self.download_Bps = 0
            self.upload_Bps = 0
            self.download_Mbps = 0
            self.upload_Mbps = 0
            self.isp = ''
            self.server_id = ''
            self.server_host = ''
            self.server_name = ''
            self.server_location = ''

    def get_timestamp(self):
        return self.timestamp
    
    def get_latency(self):
        return self.latency
    
    def get_download_Bps(self):
        return self.download_Bps
    
    def get_upload_Bps(self):
        return self.upload_Bps
    
    def get_download_Mbps(self):
        return self.download_Mbps
    
    def get_upload_Mbps(self):
        return self.upload_Mbps
    
    def get_isp(self):
        return self.isp
    
    def get_server_id(self):
        return self.server_id
    
    def get_server_host(self):
        return self.server_host
    
    def get_server_name(self):
        return self.server_name
    
    def get_server_location(self):
        return self.server_location


def versao_speedtest():
    versao = run(["speedtest", "--version"], stdout=PIPE, stderr=PIPE)
    print(versao.stdout.decode())
    print('---------------------------------------------------------------------------------')




versao_speedtest()

now = datetime.now()
now_txt = now.strftime('%Y%m%d_%H%M')
headers = ['#','timestamp', 'latency(ms)', 'download_Mbps', 'upload_Mbps', 'isp', 'server_id', 'server_host', 'server_name', 'server_location']
csvfile = open('./CSV/speedtest-'+now_txt+'.csv', 'w')
w = csv.writer(csvfile, delimiter=';')
w.writerow(headers)
csvfile.close()

contador_speedtest = 0
intervalo = 900

print(f'Intervalo entre testes: {intervalo} segundos')
time.sleep(3)

while(True):
    contador_speedtest = contador_speedtest + 1
    print('');
    print(f'Verificação #{contador_speedtest}')
    test1 = Speed()
    test1.speed_test()

    timestamp = test1.get_timestamp()
    print(f'timestamp: {timestamp}')
    latency = test1.get_latency()
    print(f'latencia: {latency} ms')
    download_Bps = test1.get_download_Bps()
    print(f'download: {download_Bps} bytes/s')
    upload_Bps = test1.get_upload_Bps()
    print(f'upload: {upload_Bps} bytes/s')
    download_Mbps = test1.get_download_Mbps()
    print(f'download: {download_Mbps} Mbps')
    upload_Mbps = test1.get_upload_Mbps()
    print(f'upload: {upload_Mbps} Mbps')
    isp = test1.get_isp()
    print(f'isp: {isp}')
    server_id = test1.get_server_id()
    print(f'server_id: {server_id}')
    server_host = test1.get_server_host()
    print(f'server_host: {server_host}')
    server_name = test1.get_server_name()
    print(f'server_name: {server_name}')
    server_location = test1.get_server_location()
    print(f'server_location: {server_location}')

    #gambiarra para substituir os '.' por ',' (formato de número pt-BR)
    latency = str(latency)
    latency = latency.replace('.',',')
    download_Mbps = str(download_Mbps)
    download_Mbps = download_Mbps.replace('.',',')
    upload_Mbps = str(upload_Mbps)
    upload_Mbps = upload_Mbps.replace('.',',')

    speedtest_list = [contador_speedtest, timestamp, latency, download_Mbps, upload_Mbps, isp, server_id, server_host, server_name, server_location]
    with open('./CSV/speedtest-'+now_txt+'.csv', 'a') as csvfile:
        a = csv.writer(csvfile, delimiter=';')
        a.writerow(speedtest_list)
        csvfile.close()

    #Aguarda próxima verificação
    print('');
    for i in range(intervalo):
        # print(f'Próxima verficação em {intervalo-i} segundos')
        print("\033[K", f'Próxima verficação em {intervalo-i} segundos', end="\r")
        time.sleep(1)
    print('')