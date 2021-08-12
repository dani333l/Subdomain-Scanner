# importing library
import requests
  
# função para verificação de subdomínios
def domain_scanner(domain_name,sub_domnames):
    print('-----------Scanner Iniciado-----------')
    print('----URL após a verificação de subdomínios----')
      
    # loop para obter URL's
    for subdomain in sub_domnames:
        
        # criando url colocando o subdomínio um por um
        url = f"https://{subdomain}.{domain_name}"
          
        # usando o bloco try catch para evitar a queda de
        # o programa
        try:
            
            # enviando solicitação get para o url
            requests.get(url)
              
            # se depois de colocar o subdomínio um por um url
            # is valid then printing the url
            print(f'[+] {url}')
              
        # if url is invalid then pass it
        except requests.ConnectionError:
            pass
    print('\n')
    print('----Scanner Finalizado----')
    print('-----Scanner Pausado-----')
  
# main function
if __name__ == '__main__':
    
    # inserir o nome de domínio
    dom_name = input("Bote o dominio aqui:")
    print('\n')
  
    # abrindo o arquivo de texto do subdomínio
    with open('subdomain_names1.txt','r') as file:
        
        # lendo o arquivo
        name = file.read()
          
        # usando a função spilitlines () armazenando o
        # lista de strings divididas
        sub_dom = name.splitlines()
          
    # chamando a função para verificar os subdomínios
    # e obtendo o url
    domain_scanner(dom_name,sub_dom)
