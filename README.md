# valor-one-fundos

Endpoints para o backend de Fundos do Valor Econômico.


## Banco
O banco foi dividido em basicamente algumas bases de dados para armazenar as informações dos fundos: 

Fund (Fundos)<br>
DailyReports (Informações Diárias)<br>
Guia (dados baixados da Money Star<br>
Document (Documentos publicados pelos fundos - Fato Relevante etc)<br>
Score (salvar o histórido de pontuação dos fundos)<br>
Star (histórico de estrelas dos fundos avaliados)<br>
Metric (as métricas dos fundos - no caso, sharpe e retorno)<br>

## Organização

As categorias da CVM em IDs, assim a consulta é muito rápida para o usuário final em um eventual front. 

### IDs Classe Anbima
"Renda Fixa Duração Livre Grau de Invest." = 1<br>
"Renda Fixa Duração Livre Crédito Livre" = 2<br>
"Ações Invest. no Exterior" = 3<br>
"Fechados de Ações" = 4<br>
"Ações Livre" = 5<br>
"Renda Fixa Duração Baixa Crédito Livre" = 6<br>
"Renda Fixa Duração Média Grau de Invest." = 7<br>
"Renda Fixa Duração Baixa Grau de Invest." = 8<br>
"Multimercados Livre" = 9<br>
"Renda Fixa Dívida Externa" = 10<br>
"Multimercados Macro" = 11<br>
"Ações Índice Ativo" = 12<br>
"Cambial" = 13<br>
"Ações Valor/Crescimento" = 14<br>
"Renda Fixa Duração Livre Soberano" = 15<br>
"Renda Fixa Duração Baixa Soberano" = 16<br>
"Renda Fixa Duração Alta Grau de Invest." = 17<br>
"Multimercados Invest. no Exterior" = 18<br>
"Multimercados Juros e Moedas" = 19<br>
"Multimercados Balanceados" = 20<br>
"Ações Small Caps" = 21<br>
"Previdência RF Duração Livre Grau de Inv" = 22<br>
"Ações Indexados" = 23<br>
"Renda Fixa Duração Média Crédito Livre" = 24<br>
"Previdência Balanceados de 30-49" = 25<br>
"Previdência RF Duração Média Grau de Inv" = 26<br>
"Ações Setoriais" = 27<br>
"Fundos de Participações" = 28<br>
"Ações Dividendos" = 29<br>
"Multimercados Estrat. Específica" = 30<br>
"Previdência RF Duração Livre Crédito Liv" = 31<br>
"Renda Fixa Indexados" = 32<br>
"Previdência Balanceados de 15-30" = 33<br>
"Previdência RF Duração Baixa Grau de Inv" = 34<br>
"Previdência Balanceados até 15" = 35<br>
"Ações FMP - FGTS" = 36<br>
"Previdência Multimercado Livre" = 37<br>
"Previdência RF Duração Alta Grau de Inv." = 38<br>
"Previdência RF Duração Livre Soberano" = 39<br>
"Multimercados Dinâmico" = 40<br>
"Previdência Ações Indexados" = 41<br>
"Multimercados L/S - Direcional" = 42<br>
"Fundos de Mono Ação" = 43<br>
"Previdência RF Indexados" = 44<br>
"Ações Sustentabilidade/Governança" = 45<br>
"FII Hibrido Gestão Ativa" = 46<br>
"Multimercados Trading" = 47<br>
"Renda Fixa Duração Média Soberano" = 48<br>
"Previdência Multimercados Juros e Moedas" = 49<br>
"Previdência Balanceados Data Alvo" = 50<br>
"Previdência Ações Ativo" = 51<br>
"Multimercados L/S - Neutro" = 52<br>
"Previdência RF Duração Baixa Soberano" = 53<br>
"Multimercados Capital Protegido" = 54<br>
"Renda Fixa Duração Alta Soberano" = 55<br>
"Renda Fixa Duração Alta Crédito Livre" = 56<br>
"Previdência RF Duração Alta Soberano" = 57<br>
"FIDC Outros" = 58<br>
"FIDC Fomento Mercantil" = 59<br>
"Previdência RF Duração Baixa Crédito Liv" = 60<br>
"FII Renda Gestão Ativa" = 61<br>
"Previdência RF Data Alvo" = 62<br>
"Previdência RF Duração Média Soberano" = 63<br>
"Renda Fixa Invest. no Exterior" = 64<br>
"Previdência RF Duração Média Crédito Liv" = 65<br>
"Previdência Balanceados acima de 49" = 66<br>
"Previdência RF Duração Alta Crédito Livr" = 67<br>

### IDs Classe CVM

"Fundo Multimercado" = 1<br>
"Fundo de Ações" = 2<br>
"Fundo de Renda Fixa" = 3<br>
"Fundo Cambial" = 4<br>
"FIDC" = 5<br>
"FIDC-NP" = 6<br>
"FIC FIDC" = 7<br>
"FICFIDC-NP" = 8<br>
"FMP-FGTS" = 9<br>
"FIDCFIAGRO" = 10<br>
"FIP Multi" = 11<br>
"FIP" = 12<br>
"FIP CS" = 13<br>
"FIC FIP" = 14<br>
"FIP EE" = 15<br>
"FIP IE" = 16<br>
"FII" = 17<br>
"FII-FIAGRO" = 18<br>
"FIP-FIAGRO" = 19<br>
"FUNCINE" = 20<br>
"FIDC-PIPS" = 21<br>
"FMIEE" = 22<br>
"Fundo Referenciado" = 23<br>
"Fundo de Curto Prazo" = 24<br>
"Fundo da Dívida Externa" = 25<br>
"FIP PD&I" = 26<br>

### IDs Classe Valor:
Aqui temos a identificação dos fundos feita pelo Valor Data.

"Crédito Privado Até 15 Dias" = 1<br>
"Alocação Ações" = 2<br>
"Ações no Exterior" = 3<br>
"Prefixado Renda Fixa Ativo" = 4<br>
"Juro Real" = 5<br>
"Renda Fixa DI" = 6<br>
"Debênture Incentivada" = 7<br>
"Ações" = 8<br>
"Crédito Privado Acima de 16 Dias" = 9<br>
"Crédito Privado até 15 Dias" = 10<br>
"Ações Índice" = 11<br>
"Long & Short" = 12<br>
"Investimento no Exterior" = 13<br>
"Multimercado Baixa Volatilidade" = 14<br>
"Long Biased" = 15<br>
"Multimercado" = 16<br>
"Alocação Multimercado" = 17<br>