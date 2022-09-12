#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: companies_list.py
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

__STATUS_CODE = 200

__COMPANIES_LIST = """<!doctype html>
<html lang="pt-BR">

<head>
    <title>Fundamentus - Invista Consciente - Indicadores Financeiros e Fundamentalistas - </title>
</head>

<body class="header-fixed">

    <div class="main">
        <div class="container">
            <div class="row">
                <div class="col col-lg-6">
                    <h3 class="h3">Selecione a Empresa</h3>
                    <div class="table-responsive">
                        <table class="table table-default table-sort table-resultados-trimestrais">
                            <thead>
                                <tr>
                                    <th>Papel</th>
                                    <th>Nome</th>
                                    <th>Razão Social</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><a href="detalhes.php?papel=AALR3 ">AALR3 </a></td>
                                    <td>ALLIAR</td>
                                    <td>CENTRO DE IMAGEM DIAGNOSTICOS S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABCB3">ABCB3</a></td>
                                    <td>ABC Brasil</td>
                                    <td>BANCO ABC BRASIL S/A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABCB4">ABCB4</a></td>
                                    <td>ABC Brasil</td>
                                    <td>BANCO ABC BRASIL S/A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABEV3">ABEV3</a></td>
                                    <td>AMBEV S/A</td>
                                    <td>AMBEV S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABRE3">ABRE3</a></td>
                                    <td>SOMOS EDUCA</td>
                                    <td>SOMOS EDUCAÇÃO S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABYA3">ABYA3</a></td>
                                    <td>ABYARA</td>
                                    <td>ABYARA PLANEJAMENTO IMOBILIARIO S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ACES3">ACES3</a></td>
                                    <td>ARCELORMITTAL INOX BRASIL</td>
                                    <td>ARCELORMITTAL INOX BRASIL S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ACES4">ACES4</a></td>
                                    <td>ARCELORMITTAL INOX BRASIL</td>
                                    <td>ARCELORMITTAL INOX BRASIL S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ADHM3">ADHM3</a></td>
                                    <td>ADVANCED-DH</td>
                                    <td>ADVANCED DIGITAL HEALTH MEDICINA PREVENTIVA S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AEDU11">AEDU11</a></td>
                                    <td>ANHANGUERA EDUCACIONAL PARTICIPAÇÕES SA</td>
                                    <td>ANHANGUERA EDUCACIONAL PARTICIPAÇÕES S.A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AEDU3">AEDU3</a></td>
                                    <td>ANHANGUERA EDUCACIONAL PARTICIPAÇÕES SA</td>
                                    <td>ANHANGUERA EDUCACIONAL PARTICIPAÇÕES S.A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AELP3">AELP3</a></td>
                                    <td>AES ELPA</td>
                                    <td>AES ELPA SA</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AERI3">AERI3</a></td>
                                    <td>AERIS</td>
                                    <td>AERIS IND. E COM. DE EQUIP. GERACAO DE ENERGIA S/A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AESB3">AESB3</a></td>
                                    <td>AES BRASIL</td>
                                    <td>AES BRASIL ENERGIA S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AESL3">AESL3</a></td>
                                    <td>AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.</td>
                                    <td>AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AESL4">AESL4</a></td>
                                    <td>AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.</td>
                                    <td>AES SUL DISTRIB. GAÚCHA DE ENERGIA S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFLT3">AFLT3</a></td>
                                    <td>AFLUENTE T</td>
                                    <td>AFLUENTE TRANSMISSÃO DE ENERGIA ELÉTRICA S/A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFLU3">AFLU3</a></td>
                                    <td>AFLUENTE</td>
                                    <td>AFLUENTE GER.E TRANSM.ENERG.ELETR. S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFLU5">AFLU5</a></td>
                                    <td>AFLUENTE</td>
                                    <td>AFLUENTE GER.E TRANSM.ENERG.ELETR. S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGEI3">AGEI3</a></td>
                                    <td>AGRE EMP IMOB</td>
                                    <td>AGRE EMPREENDIMENTOS IMOBILIÁRIOS S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGEN33">AGEN33</a></td>
                                    <td>Agrenco</td>
                                    <td>AGRENCO LTD. </td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGIN3">AGIN3</a></td>
                                    <td>Agra Incorp</td>
                                    <td>AGRA EMPREENDIMENTOS IMOBILIÁRIOS S/A</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGRO3">AGRO3</a></td>
                                    <td>BRASILAGRO</td>
                                    <td>BRASILAGRO - CIA BRAS DE PROP AGRICOLAS</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGXY3">AGXY3</a></td>
                                    <td>AGROGALAXY</td>
                                    <td>AGROGALAXY PARTICIPAÇÕES S.A.</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AHEB3">AHEB3</a></td>
                                    <td>PARQUE ANHEMBI</td>
                                    <td>SAO PAULO TURISMO S.A.</td>
                                </tr>
                            </tbody>
                        </table>

                    </div>
                </div>

                <div class="col col-lg-6">
                    <h3 class="h3">Selecione o FII</h3>
                    <div class="table-responsive">
                        <table class="table table-default table-sort table-resultados-trimestrais">
                            <thead>
                                <tr>
                                    <th>Papel</th>
                                    <th>Nome</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td><a href="detalhes.php?papel=ABCP11">ABCP11</a></td>
                                    <td>FII GRAND PLAZA SHOPPING</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AEFI11">AEFI11</a></td>
                                    <td>FII RIO BRAVO RENDA EDUCACIONAL- FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFCR11">AFCR11</a></td>
                                    <td>CARTESIA RECEBÍVEIS IMOBILIÁRIOS - FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFHI11">AFHI11</a></td>
                                    <td>AF INVEST CRI FII - RECEBÍVEIS IMOBILIÁRIOS</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AFOF11">AFOF11</a></td>
                                    <td>ALIANZA MULTIESTRATÉGIA FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGCX11">AGCX11</a></td>
                                    <td>FII RIO BRAVO RENDA VAREJO - FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AGRX11">AGRX11</a></td>
                                    <td>FUNDO DE INVESTIMENTO NAS CADEIAS PRODUTIVAS AGROINDUSTRIAIS EXES ARAGUAIA -
                                        FIAGRO - IMOBILIÁRIO</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=AIEC11">AIEC11</a></td>
                                    <td>AUTONOMY EDIFÍCIOS CORPORATIVOS FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ALMI11">ALMI11</a></td>
                                    <td>FII TORRE ALMIRANTE</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ALZR11">ALZR11</a></td>
                                    <td>ALIANZA TRUST RENDA IMOBILIARIA - FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ALZR12">ALZR12</a></td>
                                    <td>ALIANZA TRUST RENDA IMOBILIARIA - FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ANCR11">ANCR11</a></td>
                                    <td>FII ANCAR IC</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=APTO11">APTO11</a></td>
                                    <td>NAVI RESIDENCIAL FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ARCT11">ARCT11</a></td>
                                    <td>RIZA ARCTIUM REAL ESTATE FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ARRI11">ARRI11</a></td>
                                    <td>FUNDO DE INVESTIMENTO ÁTRIO REIT RECEBÍVEIS IMOBILIÁRIOS</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=ATSA11">ATSA11</a></td>
                                    <td>HEDGE ATRIUM SHOPPING SANTO ANDRÉ FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BARI11">BARI11</a></td>
                                    <td>FII BARIGUI RENDIMENTOS IMOBILIÁRIOS I FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBFI11">BBFI11</a></td>
                                    <td>BB FII PROGRESSIVO</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBFO11">BBFO11</a></td>
                                    <td>BB FUNDO DE FUNDOS - FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBGO11">BBGO11</a></td>
                                    <td>BB FUNDO DE INVESTIMENTO DE CRÉDITO FIAGRO-IMOBILIÁRIO</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBPO11">BBPO11</a></td>
                                    <td>BB PROGRESSIVO II FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBRC11">BBRC11</a></td>
                                    <td>BB RENDA CORPORATIVA FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BBVJ11">BBVJ11</a></td>
                                    <td>CIDADE JARDIM CONTINENTAL TOWER FII</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BCFF11">BCFF11</a></td>
                                    <td>FII BTG PACTUAL FUNDO DE FUNDOS</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BCFF12">BCFF12</a></td>
                                    <td>FII BTG PACTUAL FUNDO DE FUNDOS</td>
                                </tr>
                                <tr>
                                    <td><a href="detalhes.php?papel=BCIA11">BCIA11</a></td>
                                    <td>BRADESCO CARTEIRA IMOBILIÁRIA ATIVA - FUNDO DE FII</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>

</html>
"""

COMPANIES_LIST_MOCK = {
    'status_code': __STATUS_CODE,
    'content': __COMPANIES_LIST
}
