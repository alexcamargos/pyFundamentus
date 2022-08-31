#!/usr/bin/env python
# encoding: utf-8

# ------------------------------------------------------------------------------
#  Name: transform_raw_information.py
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

from decimal import Decimal

from fundamentus.contracts.extract_contract import ExtractContract
from fundamentus.contracts.transform_contract import TransformContract
from fundamentus.exceptions.transform_exception import TransformException


#pylint: disable=too-few-public-methods
class TransformRawInformation:

    def transform(self,
                  extract_contract: ExtractContract) -> TransformContract:
        try:
            transform_information = self.__make_transformation(
                extract_contract.raw_information)

            transform_contract = TransformContract(
                transformed_information=transform_information)

            return transform_contract
        except Exception as exception:
            raise TransformException(exception) from exception

    def __remove_new_lines(self, string: str) -> str:
        """Remove all newline from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('\n', '')

    def __remove_all_spaces(self, string: str) -> str:
        """Remove all spaces from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace(' ', '')

    def __remove_dot(self, string: str) -> str:
        """Remove the dot from the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace('.', '')

    def __change_comma_to_dot(self, string: str) -> str:
        """Change the comma to dot in the string.

        :param string: string to be processed.
        :return: processed string.
        """

        return string.replace(',', '.')

    def __string_processing(self, string: str) -> str:
        """
        Process the string.

        :param string: string to be processed.
        :return: processed string.
        """

        # Remove all \n from the string.
        if '\n' in string:
            processing_string = self.__remove_new_lines(string)
        else:
            processing_string = string

        return self.__change_comma_to_dot(
            self.__remove_dot(self.__remove_all_spaces(processing_string)))

    def __to_decimal(self, value: str) -> Decimal:
        """Construct a new Decimal object based from value.

        :param value: value to be processed.
        :return: Decimal object.
        """

        if value.endswith('%'):
            value = value[:-1]

            return Decimal(value) / 100

        return Decimal(value) if value is not None else None

    #pylint: disable=too-many-statements
    def __make_transformation(self, raw_information):

        cotacao = raw_information['cotacao']
        informacoes_basicas = raw_information['informacoes_basicas']
        oscilacoes = raw_information['oscilacoes']
        indicadores_de_valuation = raw_information['indicadores_de_valuation']
        indicadores_de_rentabilidade = raw_information[
            'indicadores_de_rentabilidade']
        indicadores_de_endividamento = raw_information[
            'indicadores_de_endividamento']
        balanco_patrimonial = raw_information['balanco_patrimonial']
        demonstrativo_de_resultados = raw_information[
            'demonstrativo_de_resultados']

        # Processando informações básicas a ação.
        cotacao['cotacao'] = self.__to_decimal(
            self.__string_processing(cotacao['cotacao']))
        cotacao['minino_52_semanas'] = self.__to_decimal(
            self.__string_processing(cotacao['minino_52_semanas']))
        cotacao['maximo_52_semanas'] = self.__to_decimal(
            self.__string_processing(cotacao['maximo_52_semanas']))

        # Processando informações de valor de mercado.
        informacoes_basicas['valor_de_mercado'] = self.__to_decimal(
            self.__string_processing(informacoes_basicas['valor_de_mercado']))
        informacoes_basicas['valor_da_firma'] = self.__to_decimal(
            self.__string_processing(informacoes_basicas['valor_da_firma']))
        informacoes_basicas['numero_de_acoes'] = self.__to_decimal(
            self.__string_processing(informacoes_basicas['numero_de_acoes']))
        informacoes_basicas['volume_negociacoes_2_meses'] = self.__to_decimal(
            self.__string_processing(
                informacoes_basicas['volume_negociacoes_2_meses']))

        # Processando informações das oscilações da contação da ação.
        oscilacoes['dia'] = self.__to_decimal(
            self.__string_processing(oscilacoes['dia']))
        oscilacoes['mes'] = self.__to_decimal(
            self.__string_processing(oscilacoes['mes']))
        oscilacoes['30_dias'] = self.__to_decimal(
            self.__string_processing(oscilacoes['30_dias']))
        oscilacoes['12_meses'] = self.__to_decimal(
            self.__string_processing(oscilacoes['12_meses']))
        oscilacoes['2022'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2022']))
        oscilacoes['2021'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2021']))
        oscilacoes['2020'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2020']))
        oscilacoes['2019'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2019']))
        oscilacoes['2018'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2018']))
        oscilacoes['2017'] = self.__to_decimal(
            self.__string_processing(oscilacoes['2017']))

        # Processando informações dos indicadores fundamentalistas.
        indicadores_de_valuation['preco_sobre_lucro'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['preco_sobre_lucro']))
        indicadores_de_valuation[
            'preco_sobre_valor_patrimonial'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_valuation['preco_sobre_valor_patrimonial']))
        indicadores_de_valuation['preco_sobre_ebit'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['preco_sobre_ebit']))
        indicadores_de_valuation['preco_sobre_ativos'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['preco_sobre_ativos']))
        indicadores_de_valuation[
            'preco_sobre_ativo_circulante_liquido'] = self.__to_decimal(
                self.__string_processing(indicadores_de_valuation[
                    'preco_sobre_ativo_circulante_liquido']))
        indicadores_de_valuation[
            'preco_sobre_capital_giro'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_valuation['preco_sobre_capital_giro']))
        indicadores_de_valuation['lucro_por_acao'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['lucro_por_acao']))
        indicadores_de_valuation[
            'valor_patrimonial_por_acao'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_valuation['valor_patrimonial_por_acao']))
        indicadores_de_valuation['price_sales_ratio'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['price_sales_ratio']))
        indicadores_de_valuation['dividend_yield'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_valuation['dividend_yield']))
        indicadores_de_valuation[
            'enterprise_value_sobre_ebitda'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_valuation['enterprise_value_sobre_ebitda']))
        indicadores_de_valuation[
            'enterprise_value_sobre_ebit'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_valuation['enterprise_value_sobre_ebit']))

        # Processando informações de indicadores de rentabilidade.
        indicadores_de_rentabilidade[
            'return_invested_capital'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_rentabilidade['return_invested_capital']))
        indicadores_de_rentabilidade['return_on_equity'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_rentabilidade['return_on_equity']))
        indicadores_de_rentabilidade[
            'ebit_sobre_ativos_totais'] = self.__to_decimal(
                self.__string_processing(
                    indicadores_de_rentabilidade['ebit_sobre_ativos_totais']))
        indicadores_de_rentabilidade[
            'crescimento_receita_liquida_5_anos'] = self.__to_decimal(
                self.__string_processing(indicadores_de_rentabilidade[
                    'crescimento_receita_liquida_5_anos']))
        indicadores_de_rentabilidade['giro_ativos'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_rentabilidade['giro_ativos']))
        indicadores_de_rentabilidade['margem_bruta'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_rentabilidade['margem_bruta']))
        indicadores_de_rentabilidade['margem_ebit'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_rentabilidade['margem_ebit']))
        indicadores_de_rentabilidade['margem_liquida'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_rentabilidade['margem_liquida']))

        # Processando informações de indicadores de endividamento.
        indicadores_de_endividamento['liquidez_corrente'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_endividamento['liquidez_corrente']))
        indicadores_de_endividamento['divida_bruta_total'] = self.__to_decimal(
            self.__string_processing(
                indicadores_de_endividamento['divida_bruta_total']))

        # Processando informações do balanço patrimonial.
        balanco_patrimonial['ativo'] = self.__to_decimal(
            self.__string_processing(balanco_patrimonial['ativo']))
        balanco_patrimonial['divida_bruta'] = self.__to_decimal(
            self.__string_processing(balanco_patrimonial['divida_bruta']))
        balanco_patrimonial['disponibilidades'] = self.__to_decimal(
            self.__string_processing(balanco_patrimonial['disponibilidades']))
        balanco_patrimonial['divida_líquida'] = self.__to_decimal(
            self.__string_processing(balanco_patrimonial['divida_líquida']))
        balanco_patrimonial['ativo_circulante'] = self.__to_decimal(
            self.__string_processing(balanco_patrimonial['ativo_circulante']))
        balanco_patrimonial['patrimonio_Liquido'] = self.__to_decimal(
            self.__string_processing(
                balanco_patrimonial['patrimonio_Liquido']))

        # Processando informações dos demonstrativos de resultados:
        # Últimos 12 meses.
        demonstrativo_de_resultados_12_meses = demonstrativo_de_resultados[
            '12_meses']
        demonstrativo_de_resultados_12_meses[
            'receita_liquida_ultimos_12_meses'] = self.__to_decimal(
                self.__string_processing(demonstrativo_de_resultados_12_meses[
                    'receita_liquida_ultimos_12_meses']))
        demonstrativo_de_resultados_12_meses[
            'ebit_ultimos_12_meses'] = self.__to_decimal(
                self.__string_processing(demonstrativo_de_resultados_12_meses[
                    'ebit_ultimos_12_meses']))
        demonstrativo_de_resultados_12_meses[
            'lucro_liquido_ultimos_12_meses'] = self.__to_decimal(
                self.__string_processing(demonstrativo_de_resultados_12_meses[
                    'lucro_liquido_ultimos_12_meses']))
        # Últimos 3 meses.
        demonstrativo_de_resultados_3_meses = demonstrativo_de_resultados[
            '3_meses']
        demonstrativo_de_resultados_3_meses[
            'receita_liquida_ultimos_3_meses'] = self.__to_decimal(
                self.__string_processing(demonstrativo_de_resultados_3_meses[
                    'receita_liquida_ultimos_3_meses']))
        demonstrativo_de_resultados_3_meses[
            'ebit_ultimos_3_meses'] = self.__to_decimal(
                self.__string_processing(
                    demonstrativo_de_resultados_3_meses['ebit_ultimos_3_meses']
                ))
        demonstrativo_de_resultados_3_meses[
            'lucro_liquido_ultimos_3_meses'] = self.__to_decimal(
                self.__string_processing(demonstrativo_de_resultados_3_meses[
                    'lucro_liquido_ultimos_3_meses']))

        return {
            'cotacao': cotacao,
            'informacoes_basicas': informacoes_basicas,
            'oscilacoes': oscilacoes,
            'indicadores_de_valuation': indicadores_de_valuation,
            'indicadores_de_rentabilidade': indicadores_de_rentabilidade,
            'indicadores_de_endividamento': indicadores_de_endividamento,
            'balanco_patrimonial': balanco_patrimonial,
            'demonstrativo_de_resultados': demonstrativo_de_resultados
        }
