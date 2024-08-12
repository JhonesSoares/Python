estados_brasil = """UF [-],Código [-],Gentílico [-],Governador [2019],Capital [2010],Área Territorial - km² [2019],População estimada - pessoas [2020],Densidade demográfica - hab/km² [2010],Matrículas no ensino fundamental - matrículas [2018],IDH <span>Índice de desenvolvimento humano</span> [2010],Receitas realizadas - R$ (×1000) [2017],Despesas empenhadas - R$ (×1000) [2017],Rendimento mensal domiciliar per capita - R$ [2019],Total de veículos - veículos [2018],
Acre,12,acriano,GLADSON DE LIMA CAMELI,Rio Branco,164123.964,894470,4.47,157646,0.663,6632883.10836,6084416.8063,890,277831,
Alagoas,27,alagoano,JOSE RENAN VASCONCELOS CALHEIROS FILHO,Maceió,27843.295,3351543,112.33,490587,0.631,11950438.46015,10460634.91711,731,834827,
Amapá,16,amapaense,ANTONIO WALDEZ GÓES DA SILVA,Macapá,142470.762,861773,4.69,136185,0.708,5396417.14471,4224464.08829,880,195039,
Amazonas,13,amazonense,WILSON MIRANDA LIMA,Manaus,1559167.889,4207714,2.23,705007,0.674,17328459.43402,15324896.55705,842,883083,
Bahia,29,baiano,RUI COSTA DOS SANTOS,Salvador,564760.427,14930634,24.82,2034711,0.660,50191003.24052,45570160.0038,913,4139107,
Ceará,23,cearense,CAMILO SOBREIRA DE SANTANA,Fortaleza,148894.441,9187103,56.76,1198116,0.682,28420222.47191,24608352.18276,942,3148369,
Distrito Federal,53,brasiliense,IBANEIS ROCHA BARROS JUNIOR,Brasília,5760.783,3055149,444.66,377622,0.824,23812211.27074,21990464.6849,2686,1812473,
Espírito Santo,32,capixaba ou espírito-santense,JOSE RENATO CASAGRANDE,Vitória,46074.447,4064052,76.25,502059,0.740,19685616.74376,14392338.00188,1477,1936862,
Goiás,52,goiano,RONALDO RAMOS CAIADO,Goiânia,340203.329,7113540,17.65,877593,0.735,37885335.16848,24248380.34233,1306,3909429,
Maranhão,21,maranhense,FLÁVIO DINO DE CASTRO E COSTA,São Luís,329642.182,7114598,19.81,1178949,0.639,18503261.35491,17627170.75574,636,1696683,
Mato Grosso,51,mato-grossense,MAURO MENDES FERREIRA,Cuiabá,903207.019,3526220,3.36,471613,0.725,23958528.83588,18187363.27009,1403,2080848,
Mato Grosso do Sul,50,sul-mato-grossense ou mato-grossense-do-sul,REINALDO AZAMBUJA SILVA,Campo Grande,357145.534,2809394,6.86,404114,0.729,16396655.77012,14506915.37404,1514,1583142,
Minas Gerais,31,mineiro,ROMEU ZEMA NETO,Belo Horizonte,586521.123,21292666,33.41,2511483,0.731,97199823.15616,98391669.16323,1358,11191341,
Pará,15,paraense,HELDER ZAHLUTH BARBALHO,Belém,1245870.798,8690745,6.07,1439788,0.646,25849446.10454,22533470.04547,807,2013952,
Paraíba,25,paraibano,JOÃO AZEVEDO LINS FILHO,João Pessoa,56467.242,4039277,66.70,556248,0.658,13097005.31928,10074700.04266,929,1293668,
Paraná,41,paranaense,CARLOS ROBERTO MASSA JUNIOR,Curitiba,199298.979,11516840,52.40,1427218,0.749,60163576.12246,55534402.97483,1621,7571122,
Pernambuco,26,pernambucano,PAULO HENRIQUE SARAIVA CÂMARA,Recife,98067.881,9616621,89.62,1301930,0.673,35746028.97102,33320486.44445,970,3010638,
Piauí,22,piauiense,JOSÉ WELLINGTON BARROSO DE ARAÚJO DIAS,Teresina,251756.515,3281480,12.40,480126,0.646,12124215.61511,9676736.31835,827,1196192,
Rio de Janeiro,33,fluminense,WILSON JOSÉ WITZEL,Rio de Janeiro,43750.427,17366189,365.23,2003315,0.761,78488140.78862,67965548.69757,1882,6725822,
Rio Grande do Norte,24,potiguar ou  norte-rio-grandense ou  rio-grandense-do-norte,MARIA DE FATIMA BEZERRA,Natal,52809.602,3534165,59.99,467629,0.684,13527552.73159,11330957.55333,1057,1290903,
Rio Grande do Sul,43,gaúcho ou sul-rio-grandense,EDUARDO FIGUEIREDO CAVALHEIRO LEITE,Porto Alegre,281707.156,11422973,37.96,1298736,0.746,66397468.17915,62476279.34364,1843,7077972,
Rondônia,11,rondoniense ou rondoniano,MARCOS JOSE ROCHA DOS SANTOS,Porto Velho,237765.240,1796460,6.58,269626,0.690,9122310.72305,7085530.0168,1136,985047,
Roraima,14,roraimense,ANTONIO OLIVERIO GARCIA DE ALMEIDA,Boa Vista,223644.527,631181,2.01,96582,0.707,4419450.41557,3384683.73914,1044,219290,
Santa Catarina,42,catarinense ou barriga-verde,CARLOS MOISÉS DA SILVA,Florianópolis,95730.684,7252502,65.27,851993,0.774,34696772.82078,25595103.37918,1769,5152615,
São Paulo,35,paulista,JOÃO AGRIPINO DA COSTA DORIA JUNIOR,São Paulo,248219.481,46289333,166.23,5367614,0.783,232822496.56706,231982243.69176,1946,29057749,
Sergipe,28,sergipano ou sergipense,BELIVALDO CHAGAS SILVA,Aracaju,21925.424,2318822,94.36,331297,0.665,10145046.95355,8494927.19996,980,772380,
Tocantins,17,tocantinense,MAURO CARLESSE,Palmas,277466.763,1590248,4.98,246183,0.699,10305099.01288,8929456.43836,1056,690169,"""

# 1. Usando o conteúdo da variável acima, cria uma rotina para transformar seu conteúdo em um dicionário de dados aninhando, lista com um dicionário para cada estado. Use os nomes das colunas para o nome das chaves dos dicionários e valores das colunas para o valor de cada chave.
estados_dict = {}

for linha in estados_brasil.splitlines()[1:]:
    cabecalho = estados_brasil.splitlines()[0].split(',')
    linha_lista = linha.split(',')
    uf = linha_lista[0]
    #print(uf)
    estados_dict[uf] = {cabecalho[x]: linha_lista[x] for x in range(len(cabecalho))}

    

#print(estados_dict)  


# PARA PEGAR AS CHAVES ---> .keys()

# 2. Usando o dicionário criado na questão anterior ou a variável inicial imprima qual o nome do governador de Roraima.
print(estados_dict['Roraima']['Governador [2019]'])

# 3. Usando o dicionário criado na questão anterior ou a variável inicial imprima qual o gentílico de quem nas no Rio Grande do Norte.
print(estados_dict['Rio Grande do Norte']['Gentílico [-]'])

# 4. Usando o dicionário criado na questão anterior ou a variável inicial imprima qual o capital do estado do Amapá.
print(estados_dict['Amapá']['Capital [2010]'])

# 5. Usando o dicionário criado na questão anterior ou a variável inicial imprima o total da área territorial do Brasil.

area_totalbrasil = 0
for dados in estados_dict.values():
    area_totalbrasil += float(dados['Área Territorial - km² [2019]'])    
print(area_totalbrasil)

# 6. Usando o dicionário criado na questão anterior ou a variável inicial imprima o total da população estimada do Brasil.
populacao_brasil = 0
for estados, populacao_estados in estados_dict.items():
    populacao_brasil += float(populacao_estados['População estimada - pessoas [2020]'])
print(populacao_brasil)

# 8. Usando o dicionário criado na questão anterior ou a variável inicial imprima o total de veículos do Brasil.


# 9. Imprima o nome do estado de maior densidade demográfica
maiordensidade = 0
estadomaior = ''
for estado, dados in estados_dict.items():
    densidadeatual = float(dados['Densidade demográfica - hab/km² [2010]'])
    if maiordensidade < densidadeatual:
        maiordensidade = densidadeatual
        estadomaior = estado
print(estadomaior, maiordensidade)