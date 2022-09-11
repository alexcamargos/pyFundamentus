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

__FUNDAMENTUS_HTML = """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html lang="pt-br">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<title>FUNDAMENTUS - MGLU3 - Invista consciente - Indicadores Fundamentalistas</title>
</head>

<body class="detalhes">
<table class="w728">
<tr>
<td class="label w15"><span class="help tips" title="Código da ação">?</span><span class="txt">Papel</span></td>
<td class="data w35"><span class="txt">MGLU3</span></td>
<td class="label destaque w2"><span class="help tips" title="Cotação de fechamento da ação no último pregão">?</span><span class="txt">Cotação</span></td>
<td class="data destaque w3"><span class="txt">4,52</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="ON = Ordinária, PN = Preferencial, PNA = Pref. tipo A, etc">?</span><span class="txt">Tipo</span></td>
<td class="data"><span class="txt">ON NM</span></td>
<td class="label"><span class="help tips" title="Data do último pregão em  que o ativo foi negociado">?</span><span class="txt">Data últ cot</span></td>
<td class="data"><span class="txt">29/08/2022</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Nome comercial da empresa.">?</span><span class="txt">Empresa</span></td>
<td class="data"><span class="txt">MAGAZ LUIZA ON NM</span></td>
<td class="label"><span class="help tips" title="Menor cotação da ação nos últimos 12 meses.">?</span><span class="txt">Min 52 sem</span></td>
<td class="data"><span class="txt">2,13</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Classificação setorial">?</span><span class="txt">Setor</span></td>
<td class="data"><span class="txt"><a href="resultado.php?setor=7">Comércio</a></span></td>
<td class="label"><span class="help tips" title="Maior cotação da ação nos últimos 12 meses">?</span><span class="txt">Max 52 sem</span></td>
<td class="data"><span class="txt">19,48</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Classificação por segmento de atuação.">?</span><span class="txt">Subsetor</span></td>
<td class="data"><span class="txt"><a href="resultado.php?segmento=9">Eletrodomésticos</a></span></td>
<td class="label"><span class="help tips" title="Volume médio de negociação da ação nos últimos 2 meses (R$)">?</span><span class="txt">Vol $ méd (2m)</span></td>
<td class="data"><span class="txt">624.925.000</span></td>
</tr>
</table>
<table class="w728">
<tr>
<td class="label w2"><span class="help tips" title="Valor de mercado da empresa, calculado multiplicando o preço da ação pelo número total de ações.">?</span><span class="txt">Valor de mercado</span></td>
<td class="data w3"><span class="txt">30.505.200.000</span></td>
<td class="label w3"><span class="help tips" title="Data do último balanço divulgado pela empresa que consta no nosso banco de dados. Todos os indicadores são calculados considerando os últimos 12 meses finalizados na data deste balanço.">?</span><span class="txt">Últ balanço processado</span></td>
<td class="data w2"><span class="txt">30/06/2022</span></td>
</tr>
<tr>
<td class="label w2"><span class="help tips" title="Valor da firma (Enterprise Value) é calculado somando o valor de mercado da empresa a sua dívida líquida.">?</span><span class="txt">Valor da firma</span></td>
<td class="data w3"><span class="txt">35.429.700.000</span></td>
<td class="label"><span class="help tips" title="Número total de ações, somadas todas as espécies: ON, PN, etc">?</span><span class="txt">Nro. Ações</span></td>
<td class="data"><span class="txt">6.748.930.000</span></td>
</tr>
</table>
<table class="w728">
<tr>
<td class="nivel1" colspan="2"><span class="txt">Oscilações</span></td>
<td class="nivel1" colspan="4"><span class="txt">Indicadores fundamentalistas</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">Dia</span></td>
<td class="data w1"><span class="oscil">
<font color="#F75D59">-1,31%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelo lucro por ação. O P/L é o número de anos que se levaria para reaver o capital aplicado na compra de uma ação, através do recebimento do lucro gerado pela empresa, considerando que esses lucros permaneçam constantes.">?</span><span class="txt">P/L</span></td>
<td class="data w2"><span class="txt">-509,96</span></td>
<td class="label w2"><span class="help tips" title="Lucro por Ação">?</span><span class="txt">LPA</span></td>
<td class="data w2"><span class="txt">-0,01</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">Mês</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">75,19%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelo Valor Patrimonial por ação. Informa quanto o mercado está disposto a pagar sobre o Patrimônio Líquido da empresa">?</span><span class="txt">P/VP</span></td>
<td class="data w2"><span class="txt">2,79</span></td>
<td class="label w2"><span class="help tips" title="Valor Patrimonial por Ação: Valor do Patrimônio Líquido dividido pelo número total de ações.">?</span><span class="txt">VPA</span></td>
<td class="data w2"><span class="txt">1,62</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">30 dias</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">75,19%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelo EBIT por ação. EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas ">?</span><span class="txt">P/EBIT</span></td>
<td class="data w2"><span class="txt">
108,61</span></td>
<td class="label"><span class="help tips" title="Lucro Bruto dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o custo dos produtos/serviços vendidos">?</span><span class="txt">Marg. Bruta</span></td>
<td class="data"><span class="txt">
25,4%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">12 meses</span></td>
<td class="data w1"><span class="oscil"><font color="#F75D59">-76,25%</font></span></td>
<td class="label"><span class="help tips" title="Price Sales Ratio: Preço da ação dividido pela Receita Líquida por ação">?</span><span class="txt">PSR</span></td>
<td class="data"><span class="txt">
0,86</span></td>
<td class="label"><span class="help tips" title="EBIT dividido pela Receita Líquida: Indica a porcentagem de cada R$1 de venda que sobrou após o pagamento dos custos dos produtos/serviços vendidos, das despesas com vendas, gerais e administrativas">?</span><span class="txt">Marg. EBIT</span></td>
<td class="data"><span class="txt">
 0,8%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2022</span></td>
<td class="data w1"><span class="oscil"><font color="#F75D59">-37,40%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelos Ativos totais por ação.">?</span><span class="txt">P/Ativos</span></td>
<td class="data w2"><span class="txt">
0,88</span></td>
<td class="label"><span class="help tips" title="Lucro Líquido dividido pela Receita Líquida">?</span><span class="txt">Marg. Líquida</span></td>
<td class="data"><span class="txt">
-0,2%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2021</span></td>
<td class="data w1"><span class="oscil"><font color="#F75D59">-71,04%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelo capital de giro por ação. Capital de giro é o Ativo Circulante menos Passivo Circulante">?</span><span class="txt">P/Cap. Giro</span></td>
<td class="data w2"><span class="txt">
3,91</span></td>
<td class="label"><span class="help tips" title="EBIT dividido por Ativos totais. EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas">?</span><span class="txt">EBIT / Ativo</span></td>
<td class="data"><span class="txt">0,8%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2020</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">110,08%</font></span></td>
<td class="label w2"><span class="help tips" title="Preço da ação dividido pelos Ativos Circulantes Líquidos por ação. Ativo Circ. Líq. é obtido subtraindo os ativos circulantes pelas dívidas de curto e longo prazo, ou seja, após o pagamento de todas as dívidas, quanto sobraria dos ativos mais líquidos da empresa (caixa, estoque, etc)">?</span><span class="txt">P/Ativ Circ Liq</span></td>
<td class="data w2"><span class="txt">
-8,72</span></td>
<td class="label"><span class="help tips" title="Retorno sobre o Capital Investido: Calculado dividindo-se o EBIT por (Ativos - Fornecedores - Caixa). Informa o retorno que a empresa consegue sobre o capital total aplicado. EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas">?</span><span class="txt">ROIC</span></td>
<td class="data"><span class="txt">
1,1%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2019</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">112,19%</font></span></td>
<td class="label"><span class="help tips" title="Dividend Yield: Dividendo pago por ação dividido pelo preço da ação. É o rendimento gerado para o dono da ação pelo pagamento de dividendos.">?</span><span class="txt">Div. Yield</span></td>
<td class="data"><span class="txt">0,0%</span></td>
<td class="label"><span class="help tips" title="Retorno sobre o Patrimônio Líquido: Lucro líquido dividido pelo Patrimônio Líquido">?</span><span class="txt">ROE</span></td>
<td class="data"><span class="txt">
-0,5%</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2018</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">126,39%</font></span></td>
<td class="label"><span class="help tips" title="Valor da Firma (Enterprise Value dividido pelo EBITDA. EBITDA é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas + Depreciação e Amortização">?</span><span class="txt">EV / EBITDA</span></td>
<td class="data"><span class="txt">
28,33</span></td>
<td class="label"><span class="help tips" title="Ativo Circulante dividido pelo Passivo Circulante: Reflete a capacidade de pagamento da empresa no curto prazo.">?</span><span class="txt">Liquidez Corr</span></td>
<td class="data"><span class="txt">
1,64</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt">2017</span></td>
<td class="data w1"><span class="oscil"><font color="#306EFF">536,59%</font></span></td>
<td class="label"><span class="help tips" title="Valor da Firma (Enterprise Value dividido pelo EBIT. EBIT é uma aproximação do resultado operacional da empresa. O EBIT é calculado através da seguinte fórmula: Lucro Bruto - Despesas com Vendas - Despesas Administrativas">?</span><span class="txt">EV / EBIT</span></td>
<td class="data"><span class="txt">
126,14</span></td>
<td class="label"><span class="help tips" title="Dívida Bruta total (Dívida+Debêntures) dividido pelo Patrimônio Líquido">?</span><span class="txt">Div Br/ Patrim</span></td>
<td class="data"><span class="txt">
0,63</span></td>
</tr>
<tr>
<td class="label w1"><span class="txt"></span></td>
<td class="data w1"><span class="oscil"></span></td>
<td class="label"><span class="help tips" title="Crescimento da Receita Líquida nos últimos 5 anos">?</span><span class="txt">Cres. Rec (5a)</span></td>
<td class="data"><span class="txt">
30,0%</span></td>
<td class="label"><span class="help tips" title="Receita Líquida dividido por Ativos Totais. Indica a eficiência com a qual a empresa usa seus ativos para gerar vendas">?</span><span class="txt">Giro Ativos</span></td>
<td class="data"><span class="txt">
1,02</span></td>
</tr>
</table>
<table class="w728">
<tr>
<td class="nivel1" colspan="4"><span class="txt">Dados Balanço Patrimonial</span></td>
</tr>
<tr>
<td class="label w2"><span class="help tips" title="Todos os bens, direitos e valores a receber de uma entidade">?</span><span class="txt">Ativo</span></td>
<td class="data w3"><span class="txt">34.501.000.000</span></td>
<td class="label w2"><span class="help tips" title="Dívida Bruta é obtida somando-se as dívidas de curto e longo prazo mais as debêntures de curto e longo prazo.">?</span><span class="txt">Dív. Bruta</span></td>
<td class="data w3"><span class="txt">6.846.580.000</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Contas que representam bens numerários (Dinheiro)">?</span><span class="txt">Disponibilidades</span></td>
<td class="data"><span class="txt">1.922.030.000</span></td>
<td class="label"><span class="help tips" title="Dívida Bruta menos Disponibilidades. Se este valor é negativo, significa que a empresa possui caixa líquido positivo.">?</span><span class="txt">Dív. Líquida</span></td>
<td class="data"><span class="txt">4.924.550.000</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Bens ou direitos que podem ser convertido em dinheiro em curto prazo">?</span><span class="txt">Ativo Circulante</span></td>
<td class="data"><span class="txt">20.065.600.000</span></td>
<td class="label"><span class="help tips" title="O patrimônio líquido representa os valores que os sócios ou acionistas têm na empresa em um determinado momento. No balanço patrimonial, a diferença entre o valor dos ativos e dos passivos e resultado de exercícios futuros representa o PL (Patrimônio Líquido), que é o valor contábil devido pela pessoa jurídica aos sócios ou acionistas.">?</span><span class="txt">Patrim. Líq</span></td>
<td class="data"><span class="txt">10.937.800.000</span></td>
</tr>
</table>
<table class="w728">
<tr>
<td class="nivel1" colspan="4"><span class="txt">Dados demonstrativos de resultados</span></td>
</tr>
<tr>
<td class="nivel2 w5" colspan="2"><span class="txt">Últimos 12 meses</span></td>
<td class="nivel2 w5" colspan="2"><span class="txt">Últimos 3 meses</span></td>
</tr>
<tr>
<td class="label w2"><span class="help tips" title="Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.">?</span><span class="txt">Receita Líquida</span></td>
<td class="data w3"><span class="txt">35.336.600.000</span></td>
<td class="label w2"><span class="help tips" title="Receita Líquida é a soma de todas as vendas da empresa em determinado período deduzido de devoluções, descontos e alguns impostos.">?</span><span class="txt">Receita Líquida</span></td>
<td class="data w3"><span class="txt">8.562.390.000</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas">?</span><span class="txt">EBIT</span></td>
<td class="data"><span class="txt">280.867.000</span></td>
<td class="label"><span class="help tips" title="Earnings Before Interest and Taxes - Lucro antes dos impostos e juros: Uma aproximação do lucro operacional da empresa. Fórmula utilizada: Lucro bruto - desp de vendas - desp administrativas">?</span><span class="txt">EBIT</span></td>
<td class="data"><span class="txt">274.562.000</span></td>
</tr>
<tr>
<td class="label"><span class="help tips" title="O que sobra das vendas após a dedução de todas as despesas">?</span><span class="txt">Lucro Líquido</span></td>
<td class="data"><span class="txt">-59.819.000</span></td>
<td class="label"><span class="help tips" title="O que sobra das vendas após a dedução de todas as despesas">?</span><span class="txt">Lucro Líquido</span></td>
<td class="data"><span class="txt">-135.004.000</span></td>
</tr>
</table>
<BR>
</html>
"""

HTML_COLLECTOR_MOCK = {
    'status_code': __STATUS_CODE,
    'content': __FUNDAMENTUS_HTML
}
