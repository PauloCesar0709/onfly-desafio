""" Teste adicional para verificar se em viradas de ano, o número de dias de reserva é contado corretamente e o mês da reserva é igual ao mês do checkin"""

from helpers import PROJECT_ROOT, SRC_DIR, run_cli

def test_noites_na_virada_de_ano_com_varios_quartos(tmp_path):
    report = run_cli(
        tmp_path,
        [{"checkin_date": "2024-12-30", "checkout_date": "2025-01-02", "rooms": "2"}],
    )
    assert report["summary"]["total_room_nights"] == 6
    assert report["by_month"][0]["month"] == "2024-12"