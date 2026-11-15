# Consolidador de reservas Onfly

## Defeitos corrigidos

| # | Arquivo | Causa |
| 1 | `src/onfly_report/__main__.py` | Import absoluto `from cli import main ` não resolve dentro do pacote ao rodar `python -m onfly_report`; o CLI não iniciava. |
| 2 | `src/onfly_report/services/status_policy.py` | `isbillable` usava `status != "CANCELLED"` ,então NO_SHOW entrava em noites, valores,`by_month` e `top_hotels`. |
| 3 | `src/onfly_report/services/stay_calculator.py` | Noites calculadas com `checkout.day -checkin.day` (dia do mês), gerando valores negativos na virada de mês/ano. |
| 4 | `src/onfly_report/services/currency_converter.py` | Conversão dividia pela taxa em vez de multiplicar e passava por `float`, perdendo exatidão. |
| 5 | ` src/onfly_report/services/report_builder.py` | `top_hotels` era ordenado em ordem crescente de valor, exibindo os hotéis de menor gasto. |
| 6 | `src/onfly_report/repositories/csvreservation__repository.py` | Limite fixo de 200 linhas descartava silenciosamente o restante do arquivo (300 reservas). |

## Como investiguei

1. Li as regras do README. e rodei `pytest -q` visualizando 5 falhas, todas com `ModuleNotFoundError: No module named 'cli'`.
2. Corrigi o import para destravar o diagnóstico, os testes passaram a falhar por motivos de lógica no service
3. Para cada teste falhando, comparei a regra do README com a função correspondente
4. Rodei o CLI na amostra e comparei a tabela do README, que bateu após as correções
5. Rodei no arquivo real e notei que `total_reservations = 200`, mesmo com 300 linhas no csv, com isso encontrei um limite fixo escondido no repositório, que limitava a leitura até 200 linhas
6. Conferi os totais do arquivo completo com um cálculo independente
7. Adicionei testes de regressão para as regras não cobertas

## Como validar

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
PYTHONPATH=src python -m onfly_ report --input data/exemplo-validacao.csv --rates data/taxas_cambio.csv --output output/exemplo.json
PYTHONPATH=src python -m onfly_ report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json
```

Saída esperada do relatório completo:
`Reservas: 300 | Confirmadas: 235 | Noites: 1347 | Total BRL: 396170.00`

## Resultados do pytest

```
9 passed in 0.62s
```
