import pandas as pd

def desafio1():
    #lendo o arquivo "DadosEmpresa.csv"
    file=pd.read_csv("DadosEmpresa.csv")

    #print das colunas desse arquivo
    print("\nAs colunas desse arquivo:\n",file.columns)

    #print das 5 primeiras linhas desse arquivo
    print("\n5 primeiras linhas desse arquivo:\n",file.head(5))

    #Print no terminal o total de empresas nesse arquivo que tem a coluna "opcao_pelo_simples" com o valor "SIM"
    file_opcao_pelo_simples_SIM=file.loc[file["opcao_pelo_simples"]== "SIM"]
    print("\nO total de empresas nesse arquivo que tem a coluna "+ "opcao_pelo_simples "+ "com o valor "+ "SIM "+"é de:\n",file_opcao_pelo_simples_SIM.shape[0])
    print("\nAs empresas são:\n", file_opcao_pelo_simples_SIM)

    #Print no terminal a soma do "capital_social" de todas as empresas
    print("\nA soma do capital social de toda a empresa é de ", file["capital_social"].sum())

    #Print de todas as empresas que tem "capital_social" maior que 10.000 e menor que 20.000;
    print("\nTemos as seguintes empresas com capital socila maior que 10K e menor que 20K:\n", file.loc[(file["capital_social"]>10000) & (file["capital_social"]<20000)])

    ######## EXTRA ##########

    # Lendo o arquivo "Leia o arquivo "DadosEndereco.csv".csv"

    file_DadosEndereco= pd.read_csv("DadosEndereco.csv")

    # Merge entre os dois arquivos pela coluna "cnpj"
    concat=pd.merge(file["cnpj"],file_DadosEndereco["cnpj"])
    print("\nO merge entre os dois arquivos pela coluna cnpj é: \n",concat)

    # Salvando um arquivo CSV com todas as empresas que são de "CURITIBA";
    new_concat=pd.merge(file,file_DadosEndereco)
    todas_empresas_de_Curitiba=new_concat.loc[new_concat["municipio"]=="CURITIBA"]
    todas_empresas_de_Curitiba.to_csv("todas_empresas_de_Curitiba.csv")

if __name__ == '__main__':
    desafio1()
