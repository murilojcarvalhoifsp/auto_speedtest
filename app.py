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

    def test_speed(self):
        print('Testando a velocidade ...')
        comando = ["speedtest", "--format", "json"]
        execucao = run(comando, stdout=PIPE, stderr=PIPE)
        # print(execucao.stdout)
        if(execucao.returncode == 0):
            print('Teste de velocidade realizado com sucesso.')
            execucao_str = execucao.stdout.decode()
            try:
                execucao_str = execucao_str.replace('null', 'None')
                execucao_str = execucao_str.replace('false', 'False')
                execucao_str = execucao_str.replace('true', 'True')
            except:
                print('Não foram encontrados "null", "false", "true"')
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

test1 = Speed()
test1.test_speed();

timestamp = test1.get_timestamp()
print(f'timestamp: {timestamp} ms')
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