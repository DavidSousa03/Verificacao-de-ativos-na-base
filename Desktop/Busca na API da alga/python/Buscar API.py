import csv
import requests

# Função para fazer a chamada à API com o endpoint específico
def get_api_data(msisdn):
    api_url = f"/api/v1/exemplo"
    response = requests.get(api_url)

    # Verifique se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        return response.json()
    else:
        return None  # Ou qualquer valor que você deseje usar para indicar uma falha na chamada à API

# Leitura do arquivo CSV de entrada e criação de um novo arquivo CSV para saída
with open('csv/msisdn_algar.csv', 'r') as input_file, open('Base_2024.csv', 'w', newline='') as output_file:
    csv_reader = csv.reader(input_file)
    csv_writer = csv.writer(output_file)

    # Escreva o cabeçalho no arquivo de saída, substituindo 'Endpoint' por 'msisdn'
    csv_writer.writerow(['msisdn', 'imsi', 'tipoConta', 'tipoPlano', 'tecnologia', 'prepaid'])

    # Iteração sobre as linhas do arquivo de entrada
    for row in csv_reader:
        if len(row) > 0:  # Check if the row is not empty
            msisdn = row[0]  # Agora, assumindo que o MSISDN está na primeira coluna do CSV
            api_data = get_api_data(msisdn)

            if api_data is not None:
                # Ajuste esta parte conforme a estrutura real da resposta da sua API
                imsi = api_data.get('imsi', 'N/A')
                tipo_conta = api_data.get('tipoConta', 'N/A')
                tipo_plano = api_data.get('tipoPlano', 'N/A')
                tecnologia = api_data.get('tecnologia', 'N/A')
                prepaid = api_data.get('prepaid', 'N/A')

                # Escreva os dados no arquivo de saída
                csv_writer.writerow([msisdn, imsi, tipo_conta, tipo_plano, tecnologia, prepaid])
            else:
                # Se a chamada à API falhar, escreva um valor padrão ou trate conforme necessário
                csv_writer.writerow([msisdn, ', , , , nao encontrado' ])
        else:
            print("Empty row found")  # Tratar conforme necessário, como pular ou logar

print("Concluido. Os dados foram salvos em 'Base_2024.csv'.")
