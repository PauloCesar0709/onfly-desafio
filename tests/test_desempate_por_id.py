""" Teste adicional para verificar se quando ocorre empate no ranking de top_hotels, os hoteis são classificados em ordem crescente de id """

from helpers import PROJECT_ROOT, SRC_DIR, run_cli

def test_empate_no_ranking_desempata_por_hotel_id(tmp_path):
    report = run_cli(
        tmp_path,
        [
           {"reservation_id": "R-1", "hotel_id": "H03", "amount": "500.00"},
           {"reservation_id": "R-2", "hotel_id": "H01", "amount": "500.00"},
           {"reservation_id": "R-3", "hotel_id": "H02", "amount": "900.00"},
        ],
    )
    assert [hotel["hotel_id"] for hotel in report["top_hotels"]] == ["H02", "H01", "H03"]