# Consolidador de reservas Onfly - ENTREGA

## Defeitos corrigidos

| # | Arquivo | Causa raiz |
|---|---------|-------|
| 1 | `src/onfly_report/__main__.py` | Import absoluto `from cli import main ` não resolve dentro do pacote ao rodar `python -m onfly_report`; o CLI não iniciava. |
| 2 | `src/onfly_report/services/status_policy.py` | `isbillable` usava `status != "CANCELLED"` ,então NO_SHOW entrava em noites, valores,`by_month` e `top_hotels`. |
| 3 | `src/onfly_report/services/stay_calculator.py` | Noites calculadas com `checkout.day - checkin.day` (dia do mês), gerando valores negativos na virada de mês/ano. |
| 4 | `src/onfly_report/services/currency_converter.py` | Conversão dividia pela taxa em vez de multiplicar e passava por `float`, perdendo exatidão. |
| 5 | ` src/onfly_report/services/report_builder.py` | `top_hotels` era ordenado em ordem crescente de valor, exibindo os hotéis de menor gasto. |
| 6 | `src/onfly_report/repositories/csvreservation__repository.py` | Limite fixo de 200 linhas descartava silenciosamente o restante do arquivo (300 reservas). |

---

## Como investiguei

1. Li as regras do README e rodei `pytest -q` visualizando 5 falhas, todas com `ModuleNotFoundError: No module named 'cli'`.
2. Corrigi o import para destravar o diagnóstico, os testes passaram a falhar por motivos de lógica no service
3. Para cada teste falhando, comparei a regra do README com a função correspondente
4. Rodei o CLI na amostra e comparei a tabela do README, que bateu após as correções
5. Rodei no arquivo real e notei que `total_reservations = 200`, mesmo com 300 linhas no csv, com isso encontrei um limite fixo escondido no repositório, que limitava a leitura até 200 linhas
6. Conferi os totais do arquivo completo com um cálculo independente
7. Adicionei testes de regressão para as regras não cobertas

---

## Como corrigi
| # | Arquivo | Correção |
|---|---------|----------|
| 1 | `src/onfly_report/__main__.py` | Substitui o import absoluto `from cli import main ` por um import relativo `from .cli import main` |
| 2 | `src/onfly_report/services/status_policy.py` | Alterei `isbillable`, mudando o status de `status != "CANCELLED"` para `status == "CONFIRMED"` que passa para a faturação somente os confirmados |
| 3 | `src/onfly_report/services/stay_calculator.py` | Alterei as noites calculadas com `checkout.day - checkin.day` (dia do mês) para `(checkout - checkin).days` que passa a considerar a data completa |
| 4 | `src/onfly_report/services/currency_converter.py` | Alterei a conversão deixando somente `return amount * rate` sem alterar o tipo para `float` mantendo a exatidão |
| 5 | ` src/onfly_report/services/report_builder.py` | Alterei o `ranked_hotels` com `item: (-item[1]["amount"], item[0])` fazendo com que o maio valor vire o menor número, o que faz com que que ele venha em primeiro na ordem crescente |
| 6 | `src/onfly_report/repositories/csvreservation__repository.py` | Retirei o trecho de código `if len(rows) == 200: break ` fazendo com que o programa leia todas as linhas do arquivo |

## Como validar

```bash
python3.11 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest -q
PYTHONPATH=src python -m onfly_ report --input data/exemplo-validacao.csv --rates data/taxas_cambio.csv --output output/exemplo.json
PYTHONPATH=src python -m onfly_ report --input data/reservas_hoteis.csv --rates data/taxas_cambio.csv --output output/report.json
```
---

Saída esperada do relatório de exemplo:
`Reservas: 12 | Confirmadas: 9 | Noites: 28 | Total BRL: 7566.00`

---

Saída esperada do relatório completo:
`Reservas: 300 | Confirmadas: 235 | Noites: 1347 | Total BRL: 396170.00`

---

## Resultados do pytest

```
9 passed in 0.62s
```
