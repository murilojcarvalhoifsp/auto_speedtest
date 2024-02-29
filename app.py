from subprocess import run, PIPE

def test_speed():
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
        timestamp = execucao_dict["timestamp"]
        latencia = execucao_dict["ping"]["latency"]
        download_Bps = execucao_dict["download"]["bandwidth"]
        upload_Bps = execucao_dict["upload"]["bandwidth"]
        download_Mbps = download_Bps/125000
        upload_Mbps = upload_Bps/125000
        isp = execucao_dict["isp"]
        server_id = execucao_dict["server"]["id"]
        server_host = execucao_dict["server"]["host"]
        server_name = execucao_dict["server"]["name"]
        server_location = execucao_dict["server"]["location"]
        print(f'Download: {download_Bps} bytes/s')
        print(f'upload: {upload_Bps} bytes/s')
        print(f'Download: {download_Mbps} Mbps')
        print(f'upload: {upload_Mbps} Mbps')
        print(f'isp: {isp}')
        print(f'server_id: {server_id}')
        print(f'server_host: {server_host}')
        print(f'server_name: {server_name}')
        print(f'server_location: {server_location}')
    else:
        print('Falha de conexao.')


versao_speedtest = run(["speedtest", "--version"], stdout=PIPE, stderr=PIPE)
print(versao_speedtest.stdout.decode())
print('---------------------------------------------------------------------------------')
test_speed();