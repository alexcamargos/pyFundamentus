#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: html_collector.py
#  Version: 0.0.1
#
#  Summary: Python Fundamentus
#           Python Fundamentus is a Python API that allows you to quickly
#           access the main fundamental indicators of the main stocks
#           in the Brazilian market.
#
#  Author: Alexsander Lopes Camargos
#  Author-email: alcamargos@vivaldi.net
#
#  License: MIT
# ------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=trailing-whitespace
# pylint: disable=too-many-lines

__STATUS_CODE = 200

__FUNDAMENTUS_HTML = """

<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="iso-8859-1">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<meta property="og:title" content="Fundamentus" />
<meta property="og:url" content="http://www.fundamentus.com.br" />
<meta property="og:image" content="http://www.noema.com.br/-/fundamentus/m/assets/img/fundamentus-simbolo.png" />
<meta property="og:image:width" content="500" />
<meta property="og:image:height" content="500" />
<meta property="og:site_name" content="Fundamentus" />
<meta property="og:description" content="Invista consciente" />
<link rel="apple-touch-icon" sizes="180x180" href="assets/favicon/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon/favicon-16x16.png">
<link rel="manifest" href="assets/favicon/site.webmanifest">
<link rel="mask-icon" href="assets/favicon/safari-pinned-tab.svg" color="#0037c1">
<meta name="msapplication-TileColor" content="#ffffff">
<meta name="theme-color" content="#0037c1">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<link href="https://unpkg.com/aos@2.3.1/dist/aos.css" rel="stylesheet">
<link href="assets/css/fundamentus_v1.css" rel="stylesheet">
<link rel="preconnect" href="https://fonts.gstatic.com">
<link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&family=Oswald&family=Poppins:ital,wght@0,300;0,400;0,500;0,600;0,700;0,900;1,300;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">
<title>Fundamentus - Invista Consciente - Indicadores Financeiros e Fundamentalistas - MGLU3</title>
</head> <body class="acao">
<script type="text/javascript" src="assets/autocomplete/mootools.svn.js" language="JavaScript"></script>
<script type="text/javascript" src="assets/autocomplete/Observer.js" language="JavaScript"></script>
<script type="text/javascript" src="assets/autocomplete/Autocompleter.js"></script>
<script defer type="text/javascript" src="assets/autocomplete/cmplte.php" language="JavaScript"></script>
<div class="header">
<div class="container">
<div class="logo-container">
<a class="logo-ico" href=".">Fundamentus</a>
<a class="logo-fundamentus" href=".">Invista consciente</a>
<span class="header-acao-papel">MGLU3</span>
</div>
<div class="search">
<form class="search-form" method="get" action="detalhes.php">
<input name="papel" type="text" class="search-input" id="completar" autocomplete="off" spellcheck="false">
<input name="h" value="1" type="hidden">
</form>
<span class="search-close">fechar</span>
</div>
<div class="header-nav">
<ul class="menu menu_">
<li><a class="menu-item" href=".">Home</a></li>
<li><a class="menu-item" href="consciente.php">Investimento consciente</a></li>
<li class="has-submenu"><span class="menu-item">Ações</span>
<ul>
<li><a class="menu-item" href="fr.php">Fatos relevantes</a></li>
<li><a class="menu-item" href="ultimos-resultados.php">Últimos resultados</a></li>
<li><a class="menu-item" href="altas-baixas.php">Maiores Altas e Baixas</a></li>
</ul>
</li>
<li class="has-submenu"><span class="menu-item">FIIS</span>
<ul>
<li><a class="menu-item " href="fii_imoveis.php">Pesquisar Imóveis</a></li>
<li><a class="menu-item" href="fii_altas-baixas.php">Maiores Altas e Baixas</a></li>
</ul>
</li>
<li><a class="menu-item fundamentus-classico" href="?papel=MGLU3&interface=classic">Fundamentus Clássico</a></li>
</ul>
<div class="busca-avancada">
<span class="busca-avancada-label">Busca<br> avançada por</span>
<a href="buscaavancada.php">empresa</a>
<a href="fii_buscaavancada.php">fii</a>
</div>
</div>
</div>
<div class="ico-menu"><span></span></div>
<div class="fundamentus-bar"><span class="fb-azul"></span><span class="fb-verde"></span></div>
</div>
<div class="main">
<script src="https://cdn.jsdelivr.net/npm/apexcharts"></script>
<style>  
#chart {
  max-width: 760px;
  margin: 35px auto;
  opacity: 0.7;
}

.arrow_box {
  position: relative;
  background: #dfeaf0a3; 
  border: 1px solid #77b2d288;
  padding: 5px;
  border-radius: 7px;
  font-size: 14px;
}
.arrow_box:after, .arrow_box:before {
  right: 100%;
  top: 50%;
  border: solid transparent;
/*  content: " ";*/
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}
.apexcharts-tooltip.apexcharts-theme-light {
    border: 0px solid #e3e3e3;
    background: rgba(255, 255, 255, 0);
}

.arrow_box:after {
  border-color: rgba(85, 85, 85, 0);
  border-right-color: #555;
  border-width: 10px;
  margin-top: -10px;
}
.arrow_box:before {
  border-color: rgba(0, 0, 0, 0);
  border-right-color: #000000;
  border-width: 13px;
  margin-top: -13px;
}

#chart .apexcharts-tooltip {
  color: #fff;
  transform: translateX(10px) translateY(10px);
  overflow: visible !important;
  white-space: normal !important;
}

#chart .apexcharts-tooltip span {
  padding: 5px 10px;
  display: inline-block;
}
</style>
<div class="autocomplete" style="position: fixed; top:0;left:0;right:0;bottom:0; color:gray; z-index:30;">
</div>
<div class="header-acao-wrapper">
<div class="container">
<div class="header-acao">
<div class="header-acao-title">
<h1 class="acao-papel">MGLU3</h1>
<span class="acao-nome">MAGAZ LUIZA</span>
</div>
<div class="header-acao-nav">
<ul class="menu menu_">
<li><a class="menu-item active" href="detalhes.php?papel=MGLU3&h=1">Detalhes</a></li>
<li class="has-submenu"><span class="menu-item" onclick="">Gráficos</span>
<ul>
<li><a class="menu-item" href="graficos.php?papel=MGLU3&tipo=1">Balanço patrimonial</a></li>
<li><a class="menu-item" href="graficos.php?papel=MGLU3&tipo=2">Demonstrativos de resultados</a></li>
<li><a class="menu-item" href="graficos.php?papel=MGLU3&tipo=4">Fluxo de caixa</a></li>
<li><a class="menu-item" href="graficos.php?papel=MGLU3&tipo=3">Indicadores fundamentalistas</a></li>
</ul>
</li>
<li class="has-submenu"><span class="menu-item" onclick="">INFO<span class="rmacoes">RMAÇÕES</span></span>
<ul>
<li><a class="menu-item" href="acionistas.php?papel=MGLU3">Acionistas</a></li>
<li><a class="menu-item" href="principais_acionistas.php?papel=MGLU3">Principais Acionistas</a></li>
<li><a class="menu-item" href="administradores.php?papel=MGLU3">Administração</a></li>
<li><a class="menu-item" href="fatos_relevantes.php?papel=MGLU3">Fatos Relevantes</a></li>
<li><a class="menu-item" href="apresentacoes.php?papel=MGLU3">Apresentações</a></li>
<li><a class="menu-item" href="resultados_trimestrais.php?papel=MGLU3">Resultados Trim.</a></li>
<li><a class="menu-item" href="formularios_referencia.php?papel=MGLU3">Form. Referência</a></li>
<li><a class="menu-item" href="insiders.php?papel=MGLU3">Insiders</a></li>
<li><a class="menu-item" href="recompras.php?papel=MGLU3">Recompras</a></li>
<li><a class="menu-item" href="balancos.php?papel=MGLU3">Balanços em Excel</a></li>
<li><a class="menu-item" href="proventos.php?papel=MGLU3">Proventos</a></li>
</ul>
</li>
<li><a class="menu-item" href="cotacoes.php?papel=MGLU3">Cotações</a></li>
</ul>
</div>
</div>
</div>
</div> <div class="container">
<div class="frame">
<div class="row">
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Valor de mercado <span class="data-tooltip" data-toggle="tooltip" title="Valor de mercado da empresa, calculado multiplicando o preço da ação pelo número total de ações.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 30.775.100.000</span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Valor da firma <span class="data-tooltip" data-toggle="tooltip" title="Valor da firma (Enterprise Value) é calculado somando o valor de mercado da empresa a sua dívida líquida.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 35.699.700.000 </span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Nº de ações <span class="data-tooltip" data-toggle="tooltip" title="Número total de ações, somadas todas as espécies: ON, PN, etc.">?</span></span>
<span class="data-value">6.748.930.000</span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Último balanço <span class="data-tooltip" data-toggle="tooltip" title="Data do último balanço divulgado pela empresa que consta no nosso banco de dados. Todos os indicadores são calculados considerando os últimos 12 meses finalizados na data deste balanço.">?</span></span>
<span class="data-value">30/06/2022</span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Setor <span class="data-tooltip" data-toggle="tooltip" title="Classificação setorial.">?</span></span>
<span class="data-value"><a href="resultado.php?setor=7">Comércio</a></span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Subsetor <span class="data-tooltip" data-toggle="tooltip" title="Classificação por segmento de atuação.">?</span></span>
<span class="data-value"><a href="resultado.php?segmento=9">Eletrodomésticos</a></span>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-sm-auto">
<div class="frame-cotacao">
<div class="data">
<span class="data-title">Cotação <span class="data-tooltip" data-toggle="tooltip" title="Cotação de fechamento da ação no último pregão.">?</span></span>
<span class="data-value cotacao-preco"><span class="currency">R$</span>4,56</span>
</div>
<div class="data">
<span class="data-title">Última cotação <span class="data-tooltip" data-toggle="tooltip" title="Data do último pregão em  que o ativo foi negociado.">?</span></span>
<span class="data-value">
19/09/2022
</span>
</div>
</div>
</div>
<div class="col col-xl-auto">
<div class="frame">
<div class="row">
<div class="col col-xl-auto vpalpa2-estilo">
<div class="row" style="margin-bottom:14px">
<div class="col-auto">
<div class="data">
<span class="data-title">Tipo <span class="data-tooltip" data-toggle="tooltip" title="ON = Ordinária, PN = Preferencial, PNA = Pref. tipo A, etc.">?</span></span>
<span class="data-value">ON NM</span>
</div>
</div>
<div class="col-sm-auto">
<div class="data">
<span class="data-title">Volume negociado por dia <span class="data-tooltip" data-toggle="tooltip" title="Valor médio de negociação diária da ação, considerando os últimos 2 meses (R$).">?</span></span>
<span class="data-value"><span class="currency">R$</span> 691.968.000</span>
</div>
</div>
<style>
                    @media (min-width: 1200px) {
                      .vpalpa2-estilo {
                        border-right: 1px solid #e8e8e8;
                        padding-right: 0px;
                        margin-right: 9px;
                      }
                    }
                    .vpalpa {
                      display:none;
                    }
                    .vpalpa2 {
                      display:block;
                    }
                    @media (max-width: 1200px) {
                      .vpalpa {
                        display:block;
                      }
                      .vpalpa2 {
                        display:none;
                      }                    

                    }
                  </style>
<div class="col-md col-12 vpalpa">
<div class="row">
<div class="col-auto">
<div class="data">
<span class="data-title">VPA <span class="data-tooltip" data-toggle="tooltip" title="Valor Patrimonial por Ação: Valor do Patrimônio Líquido dividido pelo número total de ações.">?</span></span>
<span class="data-value">1,62</span>
</div>
</div>
<div class="col-auto">
<div class="data">
<span class="data-title">LPA <span class="data-tooltip" data-toggle="tooltip" title="Lucro por Ação.">?</span></span>
<span class="data-value">-0,01</span>
</div>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-sm-auto">
<div class="data variacao">
<span class="data-title">Variação 52 semanas</span>
<div class="data">
<span class="data-value"><span class="currency">R$</span> 2,13</span>
<span class="data-text">mínimo <span class="data-tooltip" data-toggle="tooltip" title="Menor cotação da ação nos últimos 12 meses.">?</span></span>
</div>
<div class="oscilacao-bar"></div>
<div class="data">
<span class="data-value"><span class="currency">R$</span> 16,39</span>
<span class="data-text">máximo <span class="data-tooltip" data-toggle="tooltip" title="Maior cotação da ação nos últimos 12 meses.">?</span></span>
</div>
</div>
</div>
</div>
</div>
<div class="col-auto vpalpa2">
<div class="row" style="margin-bottom:30px">
<div class="col">
<div class="data">
<span class="data-title">VPA <span class="data-tooltip" data-toggle="tooltip" title="Valor Patrimonial por Ação: Valor do Patrimônio Líquido dividido pelo número total de ações.">?</span></span>
<span class="data-value">1,62</span>
</div>
</div>
</div>
<div class="row">
<div class="col">
<div class="data">
<span class="data-title">LPA <span class="data-tooltip" data-toggle="tooltip" title="Lucro por Ação.">?</span></span>
<span class="data-value">-0,01</span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="col-xl col-lg-12">
<div class="frame">
<div class="oscilacoes">
<h3 class="data-title">Oscilações</h3>
<div class="row" style="margin-bottom:24px;">
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value">
<font color="#215be4">2,24 <span class="porcentagem">%</span></font></span>
<span class="data-text">dia</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">6,79 <span class="porcentagem">%</span></font></span>
<span class="data-text">mês</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">20,63 <span class="porcentagem">%</span></font></span>
<span class="data-text">30 dias</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#F75D59">-72,48 <span class="porcentagem">%</span></font></span>
<span class="data-text">12 meses</span>
</div>
</div>
</div>
<div class="row">
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#F75D59">-36,84 <span class="porcentagem">%</span></font></span>
<span class="data-text">2022</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#F75D59">-71,04 <span class="porcentagem">%</span></font></span>
<span class="data-text">2021</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">110,08 <span class="porcentagem">%</span></font></span>
<span class="data-text">2020</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">112,19 <span class="porcentagem">%</span></font></span>
<span class="data-text">2019</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">126,39 <span class="porcentagem">%</span></font></span>
<span class="data-text">2018</span>
</div>
</div>
<div class="col-sm-auto col-4">
<div class="data">
<span class="data-value"><font color="#215be4">536,59 <span class="porcentagem">%</span></font></span>
<span class="data-text">2017</span>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="row chart-historico-cotacoes">
<div class="col">
<div class="frame">
<div id="chartHistoricoCotacoes"></div>
</div>
</div>
</div>
<div class="row">
<div class="col">
<div class="frame">
<h2 class="session-title">Indicadores de valuation</h2>
<div class="row">
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">P/L <span class="data-tooltip" data-toggle="tooltip" title="Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes.">?</span></span>
<span class="data-value">-514,47</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">P/VP <span class="data-tooltip" data-toggle="tooltip" title="Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa.">?</span></span>
<span class="data-value">2,81</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
 <span class="data-title">P/EBIT <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Preço da ação dividido pelo EBIT por ação. EBIT é o Lucro antes dos Impostos e Despesas Financeiras. É uma boa aproximação do lucro operacional da empresa.">?</span></span>
<span class="data-value">109,57</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">PSR <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação.">?</span></span>
<span class="data-value">0,87</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Preço/Ativos <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Preço da ação dividido pelos Ativos totais por ação.">?</span></span>
<span class="data-value">0,89</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Preço/Ativ circ liq <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc).">?</span></span>
<span class="data-value">-8,80</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Dividend Yield <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos.">?</span></span>
<span class="data-value">0,0 <span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">EV/EBITDA <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Valor da Firma (Enterprise Value dividido pelo EBITDA.">?</span></span>
<span class="data-value">28,54</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">EV/EBIT <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Valor da Firma (Enterprise Value dividido pelo EBIT.">?</span></span>
<span class="data-value">127,11</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Preço/Capital de giro <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante.">?</span></span>
<span class="data-value">3,94</span>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col">
<div class="frame">
<h2 class="session-title">Indicadores de rentabilidade</h2>
<div class="row">
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">ROE <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido.">?</span></span>
<span class="data-value">-0,5<span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">ROIC <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicado.">?</span></span>
<span class="data-value">1,1 <span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">EBIT/Ativo <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="EBIT dividido por Ativos totais.">?</span></span>
<span class="data-value">0,8</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Crescimento receita <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Crescimento da Receita Líquida nos últimos 5 anos.">?</span></span>
<span class="data-value">30,0 <span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Giro ativos <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Receita Líquida dividido por Ativos Totais. Indica a eficiência com a qual a empresa usa seus ativos para gerar vendas.">?</span></span>
<span class="data-value">1,02 </span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Margem bruta <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Lucro Bruto dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o custo dos produtos/serviços vendidos.">?</span></span>
<span class="data-value">25,4 <span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Margem EBIT <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas.">?</span></span>
<span class="data-value">0,8 <span class="porcentagem">%</span></span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Margem líquida <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Lucro Líquido dividido pela Receita Líquida.">?</span></span>
<span class="data-value">-0,2 <span class="porcentagem">%</span></span>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col">
<div class="frame">
<h2 class="session-title">Indicadores de endividamento</h2>
<div class="row">
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Liquidez corrente <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo.">?</span></span>
<span class="data-value">1,64</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Dívida bruta/Patrim <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Dívida Bruta total (Dívida+Debêntures) dividido pelo Patrimônio Líquido.">?</span></span>
<span class="data-value">0,63</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Dívida líquida/Patrim <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo Patrimônio Líquido.">?</span></span>
<span class="data-value">0,45</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">Dívida líquida/EBITDA <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Dívida Bruta total (Dívida+Debêntures) menos caixa dividido pelo EBITDA.">?</span></span>
<span class="data-value">3,94</span>
</div>
</div>
<div class="col-6 col-sm-4 col-md-2">
<div class="data">
<span class="data-title">PL/Ativos <span class="data-tooltip" data-toggle="tooltip" title="" data-original-title="Patrimônio Líquido sobre Ativos">?</span></span>
<span class="data-value">0,32</span>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="row">
<div class="col-sm">
<div class="frame">
<h2 class="session-title">Balanço patrimonial</h2>
<div class="row">
<div class="col-sm">
<div class="data">
<span class="data-title">Ativo <span class="data-tooltip" data-toggle="tooltip" title="Todos os bens, direitos e valores a receber de uma entidade.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 34.501.000.000</span>
</div>
<div class="data">
<span class="data-title">Ativo circulante <span class="data-tooltip" data-toggle="tooltip" title="Bens ou direitos que podem ser convertido em dinheiro em curto prazo.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 20.065.600.000</span>
</div>
<div class="data">
<span class="data-title">Disponibilidades <span class="data-tooltip" data-toggle="tooltip" title="Contas que representam bens numerários (Dinheiro).">?</span></span>
<span class="data-value"><span class="currency">R$</span> 1.922.030.000</span>
</div>
</div>
<div class="col-sm">
<div class="data">
<span class="data-title">Dívida bruta <span class="data-tooltip" data-toggle="tooltip" title="Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 6.846.580.000</span>
</div>
<div class="data">
<span class="data-title">Dívida líquida <span class="data-tooltip" data-toggle="tooltip" title="Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 4.924.550.000</span>
</div>
<div class="data">
<span class="data-title">Patrimônio líquido <span class="data-tooltip" data-toggle="tooltip" title="O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas.">?</span></span>
<span class="data-value"><span class="currency">R$</span> 10.937.800.000</span>
</div>
</div>
</div>
</div> </div>
<div class="col-sm">
<div class="frame">
<h2 class="session-title">Demonstrativo de resultados</h2>
<div class="table-responsive">
<table class="table table-demonstrativo-resultados">
<thead>
<tr>
<th></th>
<th>Últimos 12 meses</th>
<th>Últimos 3 meses</th>
</tr>
</thead>
<tbody>
<tr>
<th><span class="dt-title">Receita líquida <span class="data-tooltip" data-boundary="window" data-toggle="tooltip" title="Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.">?</span></span></th>
<td><span class="dt-value"><span class="currency">R$</span> 35.336.600.000</span></td>
<td><span class="dt-value"><span class="currency">R$</span> 8.562.390.000</span></td>
</tr>
<tr>
<th><span class="dt-title">EBIT <span class="data-tooltip" data-boundary="window" data-toggle="tooltip" title="Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas">?</span></span></th>
<td><span class="dt-value"><span class="currency">R$</span> 280.867.000</span></td>
<td><span class="dt-value"><span class="currency">R$</span> 274.562.000</span></td>
</tr>
<tr>
<th><span class="dt-title">Lucro líquido <span class="data-tooltip" data-boundary="window" data-toggle="tooltip" title="O que sobra das vendas após a dedução de todas as despesas.">?</span></span></th>
<td><span class="dt-value"><span class="currency">R$</span> -59.819.000</span></td>
<td><span class="dt-value"><span class="currency">R$</span> -135.004.000</span></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
<script> 
  function formataDataDMY( data ) {
    dia  = data.getDate().toString().padStart(2, '0'),
    mes  = (data.getMonth()+1).toString().padStart(2, '0'), //+1 pois no getMonth Janeiro começa com zero.
    ano  = data.getFullYear();
    return dia+"/"+mes+"/"+ano;
  }
 
  var dataSerieCotacoes = [
     [  1537513200000 , 3.8293  ],
     [  1537772400000 , 3.7521  ],
     [  1537858800000 , 3.8068  ],
     [  1537945200000 , 3.7744  ],
     [  1538031600000 , 3.8342  ],
     [  1538118000000 , 3.7844  ],
     [  1538377200000 , 3.7893  ],
     [  1538463600000 , 4.0283  ],
     [  1538550000000 , 4.3043  ],
     [  1538636400000 , 4.3093  ],
     [  1538722800000 , 4.3866  ],
     [  1538982000000 , 4.5881  ],
     [  1539068400000 , 4.6403  ],
     [  1539154800000 , 4.4388  ],
     [  1539241200000 , 4.6552  ],
     [  1539586800000 , 4.6353  ],
     [  1539673200000 , 4.9190  ],
     [  1539759600000 , 4.9987  ],
     [  1539846000000 , 4.9713  ],
     [  1539932400000 , 5.2225  ],
     [  1540191600000 , 5.1628  ],
     [  1540278000000 , 5.2250  ],
     [  1540364400000 , 5.1927  ],
     [  1540450800000 , 5.1977  ],
     [  1540537200000 , 5.1553  ],
     [  1540796400000 , 5.1429  ],
     [  1540882800000 , 5.2300  ],
     [  1540969200000 , 5.2176  ],
     [  1541055600000 , 5.2524  ],
     [  1541397600000 , 5.3420  ],
     [  1541484000000 , 4.8966  ],
     [  1541570400000 , 4.6627  ],
     [  1541656800000 , 4.5583  ],
     [  1541743200000 , 4.5234  ],
     [  1542002400000 , 4.7448  ],
     [  1542088800000 , 4.7398  ],
     [  1542175200000 , 4.8046  ],
     [  1542348000000 , 4.8369  ],
     [  1542607200000 , 4.8244  ],
     [  1542780000000 , 4.7971  ],
     [  1542866400000 , 4.9439  ],
     [  1542952800000 , 5.0160  ],
     [  1543212000000 , 4.8866  ],
     [  1543298400000 , 5.2151  ],
     [  1543384800000 , 5.2549  ],
     [  1543471200000 , 5.2922  ],
     [  1543557600000 , 5.0882  ],
     [  1543816800000 , 5.0111  ],
     [  1543903200000 , 5.0932  ],
     [  1543989600000 , 5.0957  ],
     [  1544076000000 , 5.1082  ],
     [  1544162400000 , 5.0783  ],
     [  1544421600000 , 4.9613  ],
     [  1544508000000 , 5.0808  ],
     [  1544594400000 , 5.1927  ],
     [  1544680800000 , 5.1753  ],
     [  1544767200000 , 5.2724  ],
     [  1545026400000 , 5.2549  ],
     [  1545112800000 , 5.4340  ],
     [  1545199200000 , 5.4688  ],
     [  1545285600000 , 5.4963  ],
     [  1545372000000 , 5.6455  ],
     [  1545804000000 , 5.4588  ],
     [  1545890400000 , 5.3743  ],
     [  1545976800000 , 5.5933  ],
     [  1546408800000 , 5.7624  ],
     [  1546495200000 , 5.7003  ],
     [  1546581600000 , 5.5262  ],
     [  1546840800000 , 5.6133  ],
     [  1546927200000 , 5.5658  ],
     [  1547013600000 , 5.5485  ],
     [  1547100000000 , 5.6033  ],
     [  1547186400000 , 5.5013  ],
     [  1547445600000 , 5.5460  ],
     [  1547532000000 , 5.4813  ],
     [  1547618400000 , 5.4217  ],
     [  1547704800000 , 5.4042  ],
     [  1547791200000 , 5.3967  ],
     [  1548050400000 , 5.1753  ],
     [  1548136800000 , 5.0210  ],
     [  1548223200000 , 5.2549  ],
     [  1548309600000 , 5.1902  ],
     [  1548655200000 , 5.1877  ],
     [  1548741600000 , 5.5162  ],
     [  1548828000000 , 5.4563  ],
     [  1548914400000 , 5.5460  ],
     [  1549000800000 , 5.5385  ],
     [  1549260000000 , 5.4838  ],
     [  1549346400000 , 5.4365  ],
     [  1549432800000 , 5.2599  ],
     [  1549519200000 , 5.1678  ],
     [  1549605600000 , 5.2674  ],
     [  1549864800000 , 5.1230  ],
     [  1549951200000 , 5.1057  ],
     [  1550037600000 , 4.9987  ],
     [  1550124000000 , 5.2897  ],
     [  1550210400000 , 5.0808  ],
     [  1550473200000 , 5.2225  ],
     [  1550559600000 , 5.2574  ],
     [  1550646000000 , 5.0358  ],
     [  1550732400000 , 4.9912  ],
     [  1550818800000 , 5.5113  ],
     [  1551078000000 , 5.3793  ],
     [  1551164400000 , 5.5287  ],
     [  1551250800000 , 5.4514  ],
     [  1551337200000 , 5.3718  ],
     [  1551423600000 , 5.4266  ],
     [  1551855600000 , 5.3171  ],
     [  1551942000000 , 5.4863  ],
     [  1552028400000 , 5.6008  ],
     [  1552287600000 , 5.6555  ],
     [  1552374000000 , 5.5410  ],
     [  1552460400000 , 5.4913  ],
     [  1552546800000 , 5.4663  ],
     [  1552633200000 , 5.4888  ],
     [  1552892400000 , 5.5883  ],
     [  1552978800000 , 5.5983  ],
     [  1553065200000 , 5.6256  ],
     [  1553151600000 , 5.6455  ],
     [  1553238000000 , 5.3668  ],
     [  1553497200000 , 5.3619  ],
     [  1553583600000 , 5.4688  ],
     [  1553670000000 , 5.2051  ],
     [  1553756400000 , 5.2922  ],
     [  1553842800000 , 5.3544  ],
     [  1554102000000 , 5.3072  ],
     [  1554188400000 , 5.1478  ],
     [  1554274800000 , 5.2400  ],
     [  1554361200000 , 5.2375  ],
     [  1554447600000 , 5.2674  ],
     [  1554706800000 , 5.1678  ],
     [  1554793200000 , 5.1528  ],
     [  1554879600000 , 5.2275  ],
     [  1554966000000 , 5.1429  ],
     [  1555052400000 , 5.1082  ],
     [  1555311600000 , 5.0658  ],
     [  1555398000000 , 5.0533  ],
     [  1555484400000 , 4.9638  ],
     [  1555570800000 , 5.3047  ],
     [  1555916400000 , 5.1927  ],
     [  1556002800000 , 5.3121  ],
     [  1556089200000 , 5.3544  ],
     [  1556175600000 , 5.4340  ],
     [  1556262000000 , 5.5559  ],
     [  1556521200000 , 5.5435  ],
     [  1556607600000 , 5.9392  ],
     [  1556780400000 , 5.9218  ],
     [  1556866800000 , 6.0934  ],
     [  1557126000000 , 6.2178  ],
     [  1557212400000 , 5.9665  ],
     [  1557298800000 , 6.0088  ],
     [  1557385200000 , 5.7724  ],
     [  1557471600000 , 5.7898  ],
     [  1557730800000 , 5.5883  ],
     [  1557817200000 , 5.5335  ],
     [  1557903600000 , 5.3718  ],
     [  1557990000000 , 5.1877  ],
     [  1558076400000 , 5.2425  ],
     [  1558335600000 , 5.3718  ],
     [  1558422000000 , 5.5708  ],
     [  1558508400000 , 5.5958  ],
     [  1558594800000 , 5.6033  ],
     [  1558681200000 , 5.4913  ],
     [  1558940400000 , 5.5262  ],
     [  1559026800000 , 5.8694  ],
     [  1559113200000 , 5.8769  ],
     [  1559199600000 , 5.9888  ],
     [  1559286000000 , 6.0860  ],
     [  1559545200000 , 6.0461  ],
     [  1559631600000 , 6.0411  ],
     [  1559718000000 , 5.9367  ],
     [  1559804400000 , 5.8993  ],
     [  1559890800000 , 6.1630  ],
     [  1560150000000 , 6.2874  ],
     [  1560236400000 , 6.4343  ],
     [  1560322800000 , 6.3073  ],
     [  1560409200000 , 6.5089  ],
     [  1560495600000 , 6.5710  ],
     [  1560754800000 , 6.4443  ],
     [  1560841200000 , 6.4616  ],
     [  1560927600000 , 6.5214  ],
     [  1561100400000 , 6.6035  ],
     [  1561359600000 , 6.5214  ],
     [  1561446000000 , 6.4143  ],
     [  1561532400000 , 6.4740  ],
     [  1561618800000 , 6.4790  ],
     [  1561705200000 , 6.5562  ],
     [  1561964400000 , 6.5289  ],
     [  1562050800000 , 6.5985  ],
     [  1562137200000 , 6.8573  ],
     [  1562223600000 , 6.8647  ],
     [  1562310000000 , 7.0190  ],
     [  1562569200000 , 7.1234  ],
     [  1562742000000 , 7.2504  ],
     [  1562828400000 , 7.1658  ],
     [  1562914800000 , 7.2055  ],
     [  1563174000000 , 7.1608  ],
     [  1563260400000 , 7.2653  ],
     [  1563346800000 , 7.5888  ],
     [  1563433200000 , 7.6709  ],
     [  1563519600000 , 7.3923  ],
     [  1563778800000 , 7.6808  ],
     [  1563865200000 , 7.5141  ],
     [  1563951600000 , 7.6335  ],
     [  1564038000000 , 7.5913  ],
     [  1564124400000 , 7.8250  ],
     [  1564383600000 , 8.1934  ],
     [  1564470000000 , 8.2158  ],
     [  1564556400000 , 8.1909  ],
     [  1564642800000 , 8.5840  ],
     [  1564729200000 , 8.8054  ],
     [  1564988400000 , 8.5690  ],
     [  1565074800000 , 9.0915  ],
     [  1565161200000 , 9.0195  ],
     [  1565247600000 , 9.2260  ],
     [  1565334000000 , 9.3851  ],
     [  1565593200000 , 9.0468  ],
     [  1565679600000 , 9.4026  ],
     [  1565766000000 , 9.1787  ],
     [  1565852400000 , 9.0195  ],
     [  1565938800000 , 9.3305  ],
     [  1566198000000 , 9.3976  ],
     [  1566284400000 , 9.0742  ],
     [  1566370800000 , 9.0767  ],
     [  1566457200000 , 8.5516  ],
     [  1566543600000 , 8.3899  ],
     [  1566802800000 , 8.3725  ],
     [  1566889200000 , 8.4970  ],
     [  1566975600000 , 8.6710  ],
     [  1567062000000 , 9.2557  ],
     [  1567148400000 , 9.0145  ],
     [  1567407600000 , 9.0940  ],
     [  1567494000000 , 8.9125  ],
     [  1567580400000 , 9.2409  ],
     [  1567666800000 , 9.1164  ],
     [  1567753200000 , 8.9424  ],
     [  1568012400000 , 8.4945  ],
     [  1568098800000 , 8.0740  ],
     [  1568185200000 , 8.5940  ],
     [  1568271600000 , 8.6934  ],
     [  1568358000000 , 8.4695  ],
     [  1568617200000 , 8.6612  ],
     [  1568703600000 , 8.6562  ],
     [  1568790000000 , 8.7084  ],
     [  1568876400000 , 8.8950  ],
     [  1568962800000 , 9.0817  ],
     [  1569222000000 , 8.9399  ],
     [  1569308400000 , 9.1339  ],
     [  1569394800000 , 9.1214  ],
     [  1569481200000 , 9.0842  ],
     [  1569567600000 , 9.1414  ],
     [  1569826800000 , 9.2011  ],
     [  1569913200000 , 9.3030  ],
     [  1569999600000 , 9.0667  ],
     [  1570086000000 , 9.2657  ],
     [  1570172400000 , 9.6340  ],
     [  1570431600000 , 9.5394  ],
     [  1570518000000 , 9.4549  ],
     [  1570604400000 , 9.8654  ],
     [  1570690800000 , 9.6887  ],
     [  1570777200000 , 10.0769  ],
     [  1571036400000 , 10.4925  ],
     [  1571122800000 , 10.4003  ],
     [  1571209200000 , 10.6391  ],
     [  1571295600000 , 10.7412  ],
     [  1571382000000 , 10.6989  ],
     [  1571641200000 , 10.7237  ],
     [  1571727600000 , 10.8781  ],
     [  1571814000000 , 10.8208  ],
     [  1571900400000 , 10.7612  ],
     [  1571986800000 , 10.4501  ],
     [  1572246000000 , 10.6168  ],
     [  1572332400000 , 10.2386  ],
     [  1572418800000 , 10.9526  ],
     [  1572505200000 , 11.1069  ],
     [  1572591600000 , 11.7414  ],
     [  1572850800000 , 11.1892  ],
     [  1572937200000 , 10.9576  ],
     [  1573023600000 , 11.2463  ],
     [  1573110000000 , 10.9976  ],
     [  1573196400000 , 10.9005  ],
     [  1573455600000 , 11.2015  ],
     [  1573542000000 , 10.7984  ],
     [  1573628400000 , 10.5745  ],
     [  1573714800000 , 11.0100  ],
     [  1574060400000 , 11.1916  ],
     [  1574146800000 , 11.0771  ],
     [  1574319600000 , 11.1966  ],
     [  1574406000000 , 11.3185  ],
     [  1574665200000 , 11.0224  ],
     [  1574751600000 , 10.7088  ],
     [  1574838000000 , 11.3458  ],
     [  1574924400000 , 11.3458  ],
     [  1575010800000 , 11.2039  ],
     [  1575270000000 , 11.1767  ],
     [  1575356400000 , 11.0945  ],
     [  1575442800000 , 10.9651  ],
     [  1575529200000 , 11.1692  ],
     [  1575615600000 , 11.2961  ],
     [  1575874800000 , 11.4081  ],
     [  1575961200000 , 11.5947  ],
     [  1576047600000 , 11.8385  ],
     [  1576134000000 , 11.9007  ],
     [  1576220400000 , 12.2091  ],
     [  1576479600000 , 12.2664  ],
     [  1576566000000 , 11.9131  ],
     [  1576652400000 , 12.0748  ],
     [  1576738800000 , 12.0972  ],
     [  1576825200000 , 12.0897  ],
     [  1577084400000 , 12.1271  ],
     [  1577343600000 , 12.2141  ],
     [  1577430000000 , 12.1246  ],
     [  1577689200000 , 11.8683  ],
     [  1577948400000 , 12.2813  ],
     [  1578034800000 , 12.1718  ],
     [  1578294000000 , 12.1818  ],
     [  1578380400000 , 12.1470  ],
     [  1578466800000 , 12.5204  ],
     [  1578553200000 , 12.9660  ],
     [  1578639600000 , 12.8962  ],
     [  1578898800000 , 13.5012  ],
     [  1578985200000 , 13.4440  ],
     [  1579071600000 , 13.3593  ],
     [  1579158000000 , 13.3096  ],
     [  1579244400000 , 13.5311  ],
     [  1579503600000 , 13.9418  ],
     [  1579590000000 , 13.9195  ],
     [  1579676400000 , 13.8647  ],
     [  1579762800000 , 14.0864  ],
     [  1579849200000 , 13.9793  ],
     [  1580108400000 , 13.3942  ],
     [  1580194800000 , 14.1883  ],
     [  1580281200000 , 14.2631  ],
     [  1580367600000 , 14.0664  ],
     [  1580454000000 , 13.8921  ],
     [  1580713200000 , 14.0739  ],
     [  1580799600000 , 14.3551  ],
     [  1580886000000 , 14.2656  ],
     [  1580972400000 , 13.8996  ],
     [  1581058800000 , 13.5012  ],
     [  1581318000000 , 13.0406  ],
     [  1581404400000 , 13.5112  ],
     [  1581490800000 , 13.9270  ],
     [  1581577200000 , 14.2033  ],
     [  1581663600000 , 14.0239  ],
     [  1581922800000 , 14.6514  ],
     [  1582009200000 , 14.4946  ],
     [  1582095600000 , 14.4051  ],
     [  1582182000000 , 14.0764  ],
     [  1582268400000 , 14.0539  ],
     [  1582700400000 , 13.1652  ],
     [  1582786800000 , 12.5104  ],
     [  1582873200000 , 12.5776  ],
     [  1583132400000 , 13.0830  ],
     [  1583218800000 , 13.1577  ],
     [  1583305200000 , 13.0581  ],
     [  1583391600000 , 11.8980  ],
     [  1583478000000 , 11.2855  ],
     [  1583737200000 , 10.0482  ],
     [  1583823600000 , 11.6987  ],
     [  1583910000000 , 10.7253  ],
     [  1583996400000 , 8.4647  ],
     [  1584082800000 , 10.4564  ],
     [  1584342000000 , 8.4822  ],
     [  1584428400000 , 8.8556  ],
     [  1584514800000 , 7.1727  ],
     [  1584601200000 , 7.6058  ],
     [  1584687600000 , 7.6307  ],
     [  1584946800000 , 7.5212  ],
     [  1585033200000 , 9.1319  ],
     [  1585119600000 , 9.9585  ],
     [  1585206000000 , 10.2373  ],
     [  1585292400000 , 9.7095  ],
     [  1585551600000 , 10.3569  ],
     [  1585638000000 , 9.7070  ],
     [  1585724400000 , 9.3312  ],
     [  1585810800000 , 8.9354  ],
     [  1585897200000 , 8.8481  ],
     [  1586156400000 , 9.5105  ],
     [  1586242800000 , 9.9808  ],
     [  1586329200000 , 10.4464  ],
     [  1586415600000 , 10.3692  ],
     [  1586761200000 , 10.4341  ],
     [  1586847600000 , 10.6805  ],
     [  1586934000000 , 10.9170  ],
     [  1587020400000 , 11.3452  ],
     [  1587106800000 , 11.1013  ],
     [  1587366000000 , 12.0696  ],
     [  1587538800000 , 12.5851  ],
     [  1587625200000 , 12.3162  ],
     [  1587711600000 , 11.7958  ],
     [  1587970800000 , 12.3237  ],
     [  1588057200000 , 12.8962  ],
     [  1588143600000 , 12.6026  ],
     [  1588230000000 , 12.3734  ],
     [  1588575600000 , 12.8066  ],
     [  1588662000000 , 12.4979  ],
     [  1588748400000 , 13.7303  ],
     [  1588834800000 , 14.1386  ],
     [  1588921200000 , 13.8274  ],
     [  1589180400000 , 13.6806  ],
     [  1589266800000 , 13.6431  ],
     [  1589353200000 , 13.7178  ],
     [  1589439600000 , 13.8174  ],
     [  1589526000000 , 13.7253  ],
     [  1589785200000 , 13.8796  ],
     [  1589871600000 , 14.5842  ],
     [  1589958000000 , 14.1660  ],
     [  1590044400000 , 14.5121  ],
     [  1590130800000 , 14.3526  ],
     [  1590390000000 , 15.0373  ],
     [  1590476400000 , 16.0531  ],
     [  1590562800000 , 16.7701  ],
     [  1590649200000 , 16.2449  ],
     [  1590735600000 , 16.0207  ],
     [  1590994800000 , 15.8589  ],
     [  1591081200000 , 15.3859  ],
     [  1591167600000 , 15.5303  ],
     [  1591254000000 , 15.0597  ],
     [  1591340400000 , 14.8008  ],
     [  1591599600000 , 15.5303  ],
     [  1591686000000 , 15.5303  ],
     [  1591772400000 , 16.0830  ],
     [  1591945200000 , 15.9212  ],
     [  1592204400000 , 16.3942  ],
     [  1592290800000 , 16.4314  ],
     [  1592377200000 , 16.7278  ],
     [  1592463600000 , 17.3527  ],
     [  1592550000000 , 17.7759  ],
     [  1592809200000 , 17.6515  ],
     [  1592895600000 , 17.4897  ],
     [  1592982000000 , 17.3776  ],
     [  1593068400000 , 17.3502  ],
     [  1593154800000 , 17.2655  ],
     [  1593414000000 , 17.5294  ],
     [  1593500400000 , 17.8381  ],
     [  1593586800000 , 18.0000  ],
     [  1593673200000 , 17.4522  ],
     [  1593759600000 , 17.9254  ],
     [  1594018800000 , 17.9229  ],
     [  1594105200000 , 18.6024  ],
     [  1594191600000 , 19.0953  ],
     [  1594278000000 , 19.7676  ],
     [  1594364400000 , 19.9618  ],
     [  1594623600000 , 20.0415  ],
     [  1594710000000 , 20.0415  ],
     [  1594796400000 , 20.2905  ],
     [  1594882800000 , 19.9618  ],
     [  1594969200000 , 20.4150  ],
     [  1595228400000 , 21.6598  ],
     [  1595314800000 , 20.9876  ],
     [  1595401200000 , 21.0747  ],
     [  1595487600000 , 20.0165  ],
     [  1595574000000 , 19.8349  ],
     [  1595833200000 , 19.7553  ],
     [  1595919600000 , 20.0165  ],
     [  1596006000000 , 19.9693  ],
     [  1596092400000 , 20.7361  ],
     [  1596178800000 , 20.1181  ],
     [  1596438000000 , 20.5818  ],
     [  1596524400000 , 20.5643  ],
     [  1596610800000 , 20.6889  ],
     [  1596697200000 , 21.4144  ],
     [  1596783600000 , 21.3495  ],
     [  1597042800000 , 20.4223  ],
     [  1597129200000 , 20.1880  ],
     [  1597215600000 , 19.9561  ],
     [  1597302000000 , 20.0534  ],
     [  1597388400000 , 20.3799  ],
     [  1597647600000 , 20.3525  ],
     [  1597734000000 , 22.3092  ],
     [  1597820400000 , 22.3590  ],
     [  1597906800000 , 21.7732  ],
     [  1597993200000 , 21.7732  ],
     [  1598252400000 , 21.7060  ],
     [  1598338800000 , 21.9353  ],
     [  1598425200000 , 22.4713  ],
     [  1598511600000 , 22.9273  ],
     [  1598598000000 , 23.5755  ],
     [  1598857200000 , 23.2365  ],
     [  1598943600000 , 23.7623  ],
     [  1599030000000 , 23.3089  ],
     [  1599116400000 , 22.0599  ],
     [  1599202800000 , 22.1272  ],
     [  1599548400000 , 21.8581  ],
     [  1599634800000 , 22.7330  ],
     [  1599721200000 , 21.9976  ],
     [  1599807600000 , 21.8282  ],
     [  1600066800000 , 22.5085  ],
     [  1600153200000 , 22.3291  ],
     [  1600239600000 , 22.2269  ],
     [  1600326000000 , 21.7110  ],
     [  1600412400000 , 21.7260  ],
     [  1600671600000 , 22.1097  ],
     [  1600758000000 , 22.3067  ],
     [  1600844400000 , 21.5565  ],
     [  1600930800000 , 22.2593  ],
     [  1601017200000 , 22.5909  ],
     [  1601276400000 , 21.8032  ],
     [  1601362800000 , 21.8057  ],
     [  1601449200000 , 22.2344  ],
     [  1601535600000 , 22.9074  ],
     [  1601622000000 , 21.9478  ],
     [  1601881200000 , 22.4688  ],
     [  1601967600000 , 22.2593  ],
     [  1602054000000 , 22.1697  ],
     [  1602140400000 , 22.9000  ],
     [  1602226800000 , 24.4653  ],
     [  1602572400000 , 25.9235  ],
     [  1602658800000 , 25.5165  ],
     [  1602745200000 , 25.4367  ],
     [  1602831600000 , 25.7259  ],
     [  1603090800000 , 25.6162  ],
     [  1603177200000 , 25.9653  ],
     [  1603263600000 , 26.1447  ],
     [  1603350000000 , 26.0250  ],
     [  1603436400000 , 25.8456  ],
     [  1603695600000 , 25.3969  ],
     [  1603782000000 , 25.3770  ],
     [  1603868400000 , 24.5593  ],
     [  1603954800000 , 25.2872  ],
     [  1604041200000 , 24.5593  ],
     [  1604386800000 , 24.9182  ],
     [  1604473200000 , 26.1148  ],
     [  1604559600000 , 27.3712  ],
     [  1604646000000 , 27.2515  ],
     [  1604905200000 , 26.3741  ],
     [  1604991600000 , 25.1477  ],
     [  1605078000000 , 25.5065  ],
     [  1605164400000 , 25.4069  ],
     [  1605250800000 , 25.0279  ],
     [  1605510000000 , 24.7786  ],
     [  1605596400000 , 24.6591  ],
     [  1605682800000 , 24.4695  ],
     [  1605769200000 , 24.5693  ],
     [  1605855600000 , 24.1306  ],
     [  1606114800000 , 23.3527  ],
     [  1606201200000 , 23.6319  ],
     [  1606287600000 , 23.9311  ],
     [  1606374000000 , 24.1803  ],
     [  1606460400000 , 24.1206  ],
     [  1606719600000 , 23.3130  ],
     [  1606806000000 , 22.8143  ],
     [  1606892400000 , 22.9839  ],
     [  1606978800000 , 23.2331  ],
     [  1607065200000 , 23.5921  ],
     [  1607324400000 , 23.7317  ],
     [  1607410800000 , 24.8783  ],
     [  1607497200000 , 23.9112  ],
     [  1607583600000 , 23.3328  ],
     [  1607670000000 , 22.9239  ],
     [  1607929200000 , 23.9810  ],
     [  1608015600000 , 24.5394  ],
     [  1608102000000 , 24.8883  ],
     [  1608188400000 , 24.4695  ],
     [  1608274800000 , 24.4496  ],
     [  1608534000000 , 24.9582  ],
     [  1608620400000 , 25.1179  ],
     [  1608706800000 , 24.9282  ],
     [  1609138800000 , 25.2077  ],
     [  1609225200000 , 25.2377  ],
     [  1609311600000 , 24.9323  ],
     [  1609743600000 , 25.1821  ],
     [  1609830000000 , 24.7424  ],
     [  1609916400000 , 23.4234  ],
     [  1610002800000 , 23.1436  ],
     [  1610089200000 , 23.8231  ],
     [  1610348400000 , 23.4733  ],
     [  1610434800000 , 24.1828  ],
     [  1610521200000 , 24.0030  ],
     [  1610607600000 , 23.7132  ],
     [  1610694000000 , 23.9430  ],
     [  1610953200000 , 24.4327  ],
     [  1611039600000 , 24.0629  ],
     [  1611126000000 , 25.4020  ],
     [  1611212400000 , 25.4719  ],
     [  1611298800000 , 25.9716  ],
     [  1611644400000 , 25.7317  ],
     [  1611730800000 , 25.7717  ],
     [  1611817200000 , 26.1714  ],
     [  1611903600000 , 25.2521  ],
     [  1612162800000 , 24.9123  ],
     [  1612249200000 , 25.2821  ],
     [  1612335600000 , 25.6318  ],
     [  1612422000000 , 25.2920  ],
     [  1612508400000 , 25.8317  ],
     [  1612767600000 , 26.1414  ],
     [  1612854000000 , 26.2214  ],
     [  1612940400000 , 25.2821  ],
     [  1613026800000 , 25.6318  ],
     [  1613113200000 , 25.8916  ],
     [  1613545200000 , 25.4819  ],
     [  1613631600000 , 25.0222  ],
     [  1613718000000 , 24.9223  ],
     [  1613977200000 , 24.2328  ],
     [  1614063600000 , 24.8424  ],
     [  1614150000000 , 24.6225  ],
     [  1614236400000 , 24.0429  ],
     [  1614322800000 , 24.1628  ],
     [  1614582000000 , 24.5326  ],
     [  1614668400000 , 24.2528  ],
     [  1614754800000 , 25.1022  ],
     [  1614841200000 , 25.4220  ],
     [  1614927600000 , 25.1122  ],
     [  1615186800000 , 23.0836  ],
     [  1615273200000 , 23.3734  ],
     [  1615359600000 , 24.8823  ],
     [  1615446000000 , 24.7824  ],
     [  1615532400000 , 24.5526  ],
     [  1615791600000 , 23.7032  ],
     [  1615878000000 , 24.1329  ],
     [  1615964400000 , 23.9230  ],
     [  1616050800000 , 22.2642  ],
     [  1616137200000 , 22.2742  ],
     [  1616396400000 , 21.8945  ],
     [  1616482800000 , 21.4947  ],
     [  1616569200000 , 20.3556  ],
     [  1616655600000 , 20.2856  ],
     [  1616742000000 , 19.9658  ],
     [  1617001200000 , 19.6361  ],
     [  1617087600000 , 20.0458  ],
     [  1617174000000 , 20.2256  ],
     [  1617260400000 , 20.4255  ],
     [  1617606000000 , 20.4055  ],
     [  1617692400000 , 20.5854  ],
     [  1617778800000 , 20.1657  ],
     [  1617865200000 , 21.8345  ],
     [  1617951600000 , 21.6546  ],
     [  1618210800000 , 21.6346  ],
     [  1618297200000 , 22.1843  ],
     [  1618383600000 , 22.1043  ],
     [  1618470000000 , 22.1843  ],
     [  1618556400000 , 21.9045  ],
     [  1618815600000 , 21.6346  ],
     [  1618902000000 , 21.5847  ],
     [  1619074800000 , 21.1350  ],
     [  1619161200000 , 21.7146  ],
     [  1619420400000 , 21.6946  ],
     [  1619506800000 , 20.9351  ],
     [  1619593200000 , 20.6354  ],
     [  1619679600000 , 20.2456  ],
     [  1619766000000 , 20.0158  ],
     [  1620025200000 , 20.1657  ],
     [  1620111600000 , 19.7360  ],
     [  1620198000000 , 19.8859  ],
     [  1620284400000 , 19.4462  ],
     [  1620370800000 , 19.8759  ],
     [  1620630000000 , 19.1864  ],
     [  1620716400000 , 19.3063  ],
     [  1620802800000 , 18.5768  ],
     [  1620889200000 , 19.1164  ],
     [  1620975600000 , 19.1364  ],
     [  1621234800000 , 18.8466  ],
     [  1621321200000 , 18.9565  ],
     [  1621407600000 , 18.6667  ],
     [  1621494000000 , 18.7267  ],
     [  1621580400000 , 18.5169  ],
     [  1621839600000 , 19.9858  ],
     [  1621926000000 , 20.0058  ],
     [  1622012400000 , 19.6560  ],
     [  1622098800000 , 19.5761  ],
     [  1622185200000 , 20.2356  ],
     [  1622444400000 , 20.1457  ],
     [  1622530800000 , 20.3356  ],
     [  1622617200000 , 20.4855  ],
     [  1622790000000 , 20.8352  ],
     [  1623049200000 , 20.7852  ],
     [  1623135600000 , 21.0351  ],
     [  1623222000000 , 20.2556  ],
     [  1623308400000 , 20.2656  ],
     [  1623394800000 , 20.3655  ],
     [  1623654000000 , 20.5754  ],
     [  1623740400000 , 20.8752  ],
     [  1623826800000 , 20.2956  ],
     [  1623913200000 , 21.2949  ],
     [  1623999600000 , 21.0551  ],
     [  1624258800000 , 21.2549  ],
     [  1624345200000 , 20.9551  ],
     [  1624431600000 , 20.5654  ],
     [  1624518000000 , 21.6346  ],
     [  1624604400000 , 21.3748  ],
     [  1624863600000 , 21.5147  ],
     [  1624950000000 , 21.6546  ],
     [  1625036400000 , 21.1350  ],
     [  1625122800000 , 20.6753  ],
     [  1625209200000 , 21.6247  ],
     [  1625468400000 , 21.3648  ],
     [  1625554800000 , 21.0700  ],
     [  1625641200000 , 22.0100  ],
     [  1625727600000 , 21.9200  ],
     [  1626073200000 , 22.1000  ],
     [  1626159600000 , 22.4900  ],
     [  1626246000000 , 22.9300  ],
     [  1626332400000 , 23.7200  ],
     [  1626418800000 , 23.9000  ],
     [  1626678000000 , 23.1200  ],
     [  1626764400000 , 23.3700  ],
     [  1626850800000 , 23.3600  ],
     [  1626937200000 , 23.2500  ],
     [  1627023600000 , 22.6000  ],
     [  1627282800000 , 22.0400  ],
     [  1627369200000 , 21.4500  ],
     [  1627455600000 , 21.5300  ],
     [  1627542000000 , 21.7200  ],
     [  1627628400000 , 20.6000  ],
     [  1627887600000 , 20.6300  ],
     [  1627974000000 , 20.4300  ],
     [  1628060400000 , 19.9600  ],
     [  1628146800000 , 20.4600  ],
     [  1628233200000 , 20.6800  ],
     [  1628492400000 , 20.4900  ],
     [  1628578800000 , 20.4000  ],
     [  1628665200000 , 20.9100  ],
     [  1628751600000 , 20.9700  ],
     [  1628838000000 , 20.2700  ],
     [  1629097200000 , 19.4200  ],
     [  1629183600000 , 19.3100  ],
     [  1629270000000 , 18.8400  ],
     [  1629356400000 , 18.9500  ],
     [  1629442800000 , 18.8600  ],
     [  1629702000000 , 18.1300  ],
     [  1629788400000 , 19.2400  ],
     [  1629874800000 , 19.5500  ],
     [  1629961200000 , 18.8000  ],
     [  1630047600000 , 19.0300  ],
     [  1630306800000 , 18.8800  ],
     [  1630393200000 , 18.2400  ],
     [  1630479600000 , 18.6800  ],
     [  1630566000000 , 18.0100  ],
     [  1630652400000 , 18.9000  ],
     [  1630911600000 , 19.4800  ],
     [  1631084400000 , 18.7900  ],
     [  1631170800000 , 18.8500  ],
     [  1631257200000 , 17.1800  ],
     [  1631516400000 , 17.4400  ],
     [  1631602800000 , 17.0300  ],
     [  1631689200000 , 16.6200  ],
     [  1631775600000 , 16.3700  ],
     [  1631862000000 , 16.5700  ],
     [  1632121200000 , 16.0500  ],
     [  1632207600000 , 16.3900  ],
     [  1632294000000 , 16.3400  ],
     [  1632380400000 , 15.8700  ],
     [  1632466800000 , 15.6300  ],
     [  1632726000000 , 15.0100  ],
     [  1632812400000 , 14.1800  ],
     [  1632898800000 , 13.9400  ],
     [  1632985200000 , 14.3400  ],
     [  1633071600000 , 14.5500  ],
     [  1633330800000 , 13.7100  ],
     [  1633417200000 , 13.6800  ],
     [  1633503600000 , 14.4600  ],
     [  1633590000000 , 14.0300  ],
     [  1633676400000 , 14.9700  ],
     [  1633935600000 , 14.3800  ],
     [  1634108400000 , 14.5000  ],
     [  1634194800000 , 14.1700  ],
     [  1634281200000 , 14.5600  ],
     [  1634540400000 , 14.2800  ],
     [  1634626800000 , 13.7300  ],
     [  1634713200000 , 13.2500  ],
     [  1634799600000 , 12.4100  ],
     [  1634886000000 , 12.4200  ],
     [  1635145200000 , 12.3400  ],
     [  1635231600000 , 11.9800  ],
     [  1635318000000 , 11.6000  ],
     [  1635404400000 , 11.1500  ],
     [  1635490800000 , 10.8100  ],
     [  1635750000000 , 11.3000  ],
     [  1635922800000 , 11.5500  ],
     [  1636009200000 , 11.0800  ],
     [  1636095600000 , 12.4400  ],
     [  1636354800000 , 11.9300  ],
     [  1636441200000 , 13.1300  ],
     [  1636527600000 , 13.0200  ],
     [  1636614000000 , 13.6500  ],
     [  1636700400000 , 11.1500  ],
     [  1637046000000 , 9.7400  ],
     [  1637132400000 , 9.2700  ],
     [  1637218800000 , 8.9900  ],
     [  1637305200000 , 9.2700  ],
     [  1637564400000 , 8.8400  ],
     [  1637650800000 , 8.6000  ],
     [  1637737200000 , 8.8200  ],
     [  1637823600000 , 8.7000  ],
     [  1637910000000 , 8.0600  ],
     [  1638169200000 , 8.0400  ],
     [  1638255600000 , 7.8000  ],
     [  1638342000000 , 6.8800  ],
     [  1638428400000 , 6.7600  ],
     [  1638514800000 , 7.0500  ],
     [  1638774000000 , 7.3000  ],
     [  1638860400000 , 7.6200  ],
     [  1638946800000 , 6.8100  ],
     [  1639033200000 , 6.2800  ],
     [  1639119600000 , 6.3700  ],
     [  1639378800000 , 6.0500  ],
     [  1639465200000 , 5.7400  ],
     [  1639551600000 , 6.1700  ],
     [  1639638000000 , 6.4000  ],
     [  1639724400000 , 6.6600  ],
     [  1639983600000 , 6.3300  ],
     [  1640070000000 , 6.4200  ],
     [  1640156400000 , 6.1600  ],
     [  1640242800000 , 6.2000  ],
     [  1640588400000 , 6.7800  ],
     [  1640674800000 , 6.8300  ],
     [  1640761200000 , 6.7600  ],
     [  1640847600000 , 7.2200  ],
     [  1641193200000 , 6.7200  ],
     [  1641279600000 , 6.6100  ],
     [  1641366000000 , 6.4200  ],
     [  1641452400000 , 6.2500  ],
     [  1641538800000 , 6.2200  ],
     [  1641798000000 , 5.7400  ],
     [  1641884400000 , 5.8700  ],
     [  1641970800000 , 6.3100  ],
     [  1642057200000 , 6.0900  ],
     [  1642143600000 , 6.3300  ],
     [  1642402800000 , 6.1200  ],
     [  1642489200000 , 5.8900  ],
     [  1642575600000 , 6.3100  ],
     [  1642662000000 , 6.6500  ],
     [  1642748400000 , 6.9000  ],
     [  1643007600000 , 6.3900  ],
     [  1643094000000 , 6.7200  ],
     [  1643180400000 , 6.7500  ],
     [  1643266800000 , 7.2200  ],
     [  1643353200000 , 6.7100  ],
     [  1643612400000 , 7.0000  ],
     [  1643698800000 , 7.0100  ],
     [  1643785200000 , 6.5100  ],
     [  1643871600000 , 6.5300  ],
     [  1643958000000 , 6.3300  ],
     [  1644217200000 , 6.3100  ],
     [  1644303600000 , 6.5400  ],
     [  1644390000000 , 6.6000  ],
     [  1644476400000 , 6.9400  ],
     [  1644562800000 , 6.3500  ],
     [  1644822000000 , 6.4800  ],
     [  1644908400000 , 6.8400  ],
     [  1644994800000 , 6.8200  ],
     [  1645081200000 , 6.6300  ],
     [  1645167600000 , 6.3600  ],
     [  1645426800000 , 6.0200  ],
     [  1645513200000 , 6.0700  ],
     [  1645599600000 , 5.9100  ],
     [  1645686000000 , 6.1200  ],
     [  1645772400000 , 6.0100  ],
     [  1646204400000 , 6.3100  ],
     [  1646290800000 , 6.3100  ],
     [  1646377200000 , 6.2900  ],
     [  1646636400000 , 5.8500  ],
     [  1646722800000 , 6.0500  ],
     [  1646809200000 , 6.2300  ],
     [  1646895600000 , 5.9600  ],
     [  1646982000000 , 5.6900  ],
     [  1647241200000 , 5.3300  ],
     [  1647327600000 , 4.8700  ],
     [  1647414000000 , 5.1300  ],
     [  1647500400000 , 5.5400  ],
     [  1647586800000 , 5.8200  ],
     [  1647846000000 , 5.7200  ],
     [  1647932400000 , 5.8100  ],
     [  1648018800000 , 6.0000  ],
     [  1648105200000 , 6.6000  ],
     [  1648191600000 , 6.5400  ],
     [  1648450800000 , 6.4700  ],
     [  1648537200000 , 7.0000  ],
     [  1648623600000 , 6.8700  ],
     [  1648710000000 , 6.8200  ],
     [  1648796400000 , 7.3500  ],
     [  1649055600000 , 7.1900  ],
     [  1649142000000 , 6.9100  ],
     [  1649228400000 , 6.6200  ],
     [  1649314800000 , 6.5600  ],
     [  1649401200000 , 6.1300  ],
     [  1649660400000 , 6.0800  ],
     [  1649746800000 , 5.9700  ],
     [  1649833200000 , 6.0300  ],
     [  1649919600000 , 6.0100  ],
     [  1650265200000 , 5.8900  ],
     [  1650351600000 , 5.9400  ],
     [  1650438000000 , 5.6100  ],
     [  1650610800000 , 5.5500  ],
     [  1650870000000 , 5.4400  ],
     [  1650956400000 , 5.1800  ],
     [  1651042800000 , 5.1000  ],
     [  1651129200000 , 5.1800  ],
     [  1651215600000 , 4.8800  ],
     [  1651474800000 , 4.8000  ],
     [  1651561200000 , 4.6000  ],
     [  1651647600000 , 4.9500  ],
     [  1651734000000 , 4.4200  ],
     [  1651820400000 , 4.3000  ],
     [  1652079600000 , 3.9100  ],
     [  1652166000000 , 3.9500  ],
     [  1652252400000 , 3.9300  ],
     [  1652338800000 , 4.1800  ],
     [  1652425200000 , 4.3800  ],
     [  1652684400000 , 4.4500  ],
     [  1652770800000 , 3.9400  ],
     [  1652857200000 , 3.7200  ],
     [  1652943600000 , 3.7300  ],
     [  1653030000000 , 3.6700  ],
     [  1653289200000 , 3.7000  ],
     [  1653375600000 , 3.7100  ],
     [  1653462000000 , 3.7100  ],
     [  1653548400000 , 4.0700  ],
     [  1653634800000 , 4.0000  ],
     [  1653894000000 , 3.8400  ],
     [  1653980400000 , 3.7200  ],
     [  1654066800000 , 3.7100  ],
     [  1654153200000 , 3.8000  ],
     [  1654239600000 , 3.5900  ],
     [  1654498800000 , 3.4000  ],
     [  1654585200000 , 3.2900  ],
     [  1654671600000 , 3.2200  ],
     [  1654758000000 , 3.0100  ],
     [  1654844400000 , 2.9000  ],
     [  1655103600000 , 2.6700  ],
     [  1655190000000 , 2.5400  ],
     [  1655276400000 , 2.5500  ],
     [  1655449200000 , 2.3800  ],
     [  1655708400000 , 2.5800  ],
     [  1655794800000 , 2.5100  ],
     [  1655881200000 , 2.4400  ],
     [  1655967600000 , 2.5500  ],
     [  1656054000000 , 2.4700  ],
     [  1656313200000 , 2.4300  ],
     [  1656399600000 , 2.3800  ],
     [  1656486000000 , 2.4100  ],
     [  1656572400000 , 2.3400  ],
     [  1656658800000 , 2.2000  ],
     [  1656918000000 , 2.1300  ],
     [  1657004400000 , 2.3800  ],
     [  1657090800000 , 2.5000  ],
     [  1657177200000 , 2.5600  ],
     [  1657263600000 , 2.6200  ],
     [  1657522800000 , 2.6300  ],
     [  1657609200000 , 2.9300  ],
     [  1657695600000 , 2.8300  ],
     [  1657782000000 , 2.9100  ],
     [  1657868400000 , 2.7800  ],
     [  1658127600000 , 2.7700  ],
     [  1658214000000 , 2.7900  ],
     [  1658300400000 , 3.0700  ],
     [  1658386800000 , 3.0100  ],
     [  1658473200000 , 2.8600  ],
     [  1658732400000 , 2.7900  ],
     [  1658818800000 , 2.6100  ],
     [  1658905200000 , 2.7000  ],
     [  1658991600000 , 2.7200  ],
     [  1659078000000 , 2.5800  ],
     [  1659337200000 , 2.7200  ],
     [  1659423600000 , 2.7100  ],
     [  1659510000000 , 2.9300  ],
     [  1659596400000 , 3.3400  ],
     [  1659682800000 , 3.1600  ],
     [  1659942000000 , 3.2700  ],
     [  1660028400000 , 3.0800  ],
     [  1660114800000 , 3.2900  ],
     [  1660201200000 , 3.0400  ],
     [  1660287600000 , 3.5800  ],
     [  1660546800000 , 4.0400  ],
     [  1660633200000 , 4.1500  ],
     [  1660719600000 , 4.0200  ],
     [  1660806000000 , 4.0300  ],
     [  1660892400000 , 3.7800  ],
     [  1661151600000 , 3.8200  ],
     [  1661238000000 , 4.1500  ],
     [  1661324400000 , 4.5000  ],
     [  1661410800000 , 4.6800  ],
     [  1661497200000 , 4.5800  ],
     [  1661756400000 , 4.5200  ],
     [  1661842800000 , 4.5100  ],
     [  1661929200000 , 4.2700  ],
     [  1662015600000 , 4.3700  ],
     [  1662102000000 , 4.2600  ],
     [  1662361200000 , 4.3200  ],
     [  1662447600000 , 4.0000  ],
     [  1662620400000 , 4.2900  ],
     [  1662706800000 , 4.3800  ],
     [  1662966000000 , 4.7800  ],
     [  1663052400000 , 4.7000  ],
     [  1663138800000 , 4.4700  ],
     [  1663225200000 , 4.3400  ],
     [  1663311600000 , 4.4600  ],
     [  1663570800000 , 4.5600  ],
      
  ];
  
  var maxXAxis = dataSerieCotacoes[dataSerieCotacoes.length-1][0] + 8*24*60*60*1000;
  var optionsHistCotacoes = {
    series: [
      { name: "Cotações", data: dataSerieCotacoes },
    ],
    colors: ['#77b2d2'], 
    chart: {
      type: 'line',
      height: 290,
      width: '95%',
      toolbar : {
        show: false,
      },
      sparkline: { enabled: false },
      zoom: { enabled: false }
    },
    stroke: {
      width: 2,
      colors: '#4093bf',
    },
    xaxis: {
      type: 'datetime',
      show: true,
      max : maxXAxis,
      range : 4.2*365*24*60*60*1000,
      labels :  {
        show : true,
      },
      tooltip: {
        enabled: false,
      },
      axisBorder: {
        show: true
      },
      axisTicks: {
        show: true
      },
      labels: {
        datetimeFormatter: {
          year: 'yyyy',
          month: 'MMM \'yy',
          day: 'dd MMM',
          hour: 'HH:mm'
        }
      },
    },
    yaxis: {
      min: 0,
      forceNiceScale: true,
      show: true,
      labels :  {
        show : true,
      },
      tickAmount: 8,
      axisBorder: {
        show: true
      },
      axisTicks: {
        show: true
      },
      labels : {
        formatter: function(val, index) {
          return (val).toFixed(2).replace('.',',');
        }
      }
    },
    fill: {
      /* opacity: 0.85,  */
      type: ['solid'],
    },
    grid: {
      padding: {
       top: 0,
       bottom: 0,
       left: 0,
       right: 0
      }
    },
    legend: {
      show: false,
      position: 'bottom',
      horizontalAlign: 'center',
      offsetX: 0,
      offsetY: 0,
      markers: {
        fillColors: ['#4093bf'],
      }
      
    },
    dataLabels: {
      enabled : false,
      formatter : function (val, opts) {
        return (val*100).toFixed(2).replace('.',',')+"%";
      }
    },
    tooltip: {
      enabled : true,
      followCursor : false,
      intersect : false,
      onDatasetHover: {
          highlightDataSeries: false,
      },
      custom: function({series, seriesIndex, dataPointIndex, w}) {
          return '<div class="arrow_box" style="font-size:11px"><div>'+formataDataDMY(new Date(w.globals.seriesX[0][dataPointIndex])) +'</div>'+
            '<div>' + (series[0][dataPointIndex]).toFixed(2).replace('.',',')+'</div>' +
            '</div>';
      },
    },
  };
  

  var chartHistCotacoes = new ApexCharts(document.querySelector("#chartHistoricoCotacoes"), optionsHistCotacoes);
  chartHistCotacoes.render();    
</script>
</div>
<div class="footer">
<div class="container">
<div class="fundamentus-simbolo">Fundamentus</div>
<ul class="menu-footer menu_">
<li><a href=".">Home</a></li>
<li><a href="termos-uso.php">Termos de uso</a></li>
<li><a href="politica-privacidade.php">Política de privacidade</a></li>
<li><a href="detalhes.php">Lista de Ativos</a></li>
<li><a href="contato.php">Fale conosco</a></li>
</ul>
<div class="footer-statement">
<p>Todas as informações disponibilizadas são obtidas a partir de fontes públicas, consideradas confiáveis e possuem caráter meramente informativo. Fundamentus não se responsabiliza por decisões tomadas a partir dessas informações.</p>
</div>
<p class="copyright">Copyright © 2021 Fundamentus. Todos os direitos reservados</p>
<a class="noema" href="https://www.noema.com.br" target="_blank" title="noema">noema</a>
</div>
<div class="fundamentus-bar"><span class="fb-azul"></span><span class="fb-verde"></span></div>
</div>
<a href="#" class="bt-scrolltop">topo</a>
<script type="text/javascript" src="script/pvt.php" language="JavaScript" async></script>
<script type="text/javascript">
    var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
    document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
    </script>
<script type="text/javascript">
    var pageTracker = _gat._getTracker("UA-3584125-1");
    pageTracker._initData();
    pageTracker._trackPageview();
  </script>
<script src="https://code.jquery.com/jquery-3.2.1.min.js" integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
<script src="assets/js/validate.js"></script>
<script src="https://unpkg.com/aos@2.3.1/dist/aos.js"></script>
<script src="assets/js/cycle2.js"></script>
<script src="assets/js/fundamentus_v1.js"></script><script>(function(){var js = "window['__CF$cv$params']={r:'74d9941d4c6ea5d7',m:'DXyaWEuiepYoPbkdyAVIp3xCjaPjM6SVHpJLQgdNSaY-1663666605-0-Acku2VxW/F6SyQgp756ax3Ed0m7SSKYFpG+qXM4td71WzF5BW+UNbzJFyOoVRRMyykessME1odt5gEhIrxjepp5e1QohUgPKlUtqVfxGqeQVLyQbYN932qbeHDq9w90C92x0KsGzPN2c8/YEwFCHbjs=',s:[0x08b76bbc13,0xb030c87631],u:'/cdn-cgi/challenge-platform/h/b'};var now=Date.now()/1000,offset=14400,ts=''+(Math.floor(now)-Math.floor(now%offset)),_cpo=document.createElement('script');_cpo.nonce='',_cpo.src='/cdn-cgi/challenge-platform/h/b/scripts/alpha/invisible.js?ts='+ts,document.getElementsByTagName('head')[0].appendChild(_cpo);";var _0xh = document.createElement('iframe');_0xh.height = 1;_0xh.width = 1;_0xh.style.position = 'absolute';_0xh.style.top = 0;_0xh.style.left = 0;_0xh.style.border = 'none';_0xh.style.visibility = 'hidden';document.body.appendChild(_0xh);function handler() {var _0xi = _0xh.contentDocument || _0xh.contentWindow.document;if (_0xi) {var _0xj = _0xi.createElement('script');_0xj.nonce = '';_0xj.innerHTML = js;_0xi.getElementsByTagName('head')[0].appendChild(_0xj);}}if (document.readyState !== 'loading') {handler();} else if (window.addEventListener) {document.addEventListener('DOMContentLoaded', handler);} else {var prev = document.onreadystatechange || function () {};document.onreadystatechange = function (e) {prev(e);if (document.readyState !== 'loading') {document.onreadystatechange = prev;handler();}};}})();</script></body>
</html>
"""

HTML_COLLECTOR_MOCK = {
    'status_code': __STATUS_CODE,
    'content': __FUNDAMENTUS_HTML
}
