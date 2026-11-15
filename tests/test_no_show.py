""" Teste adicional para verificar se faturamentos NO_SHOW ficam de fora de by_month e top_hotels """

from helpers import PROJECT_ROOT, SRC_DIR, run_cli;

def test_no_show_fora_de_by_month_e_top_hotels(tmp_path):
    report = run_cli(
        tmp_path,
        [
            {"reservation_id": "R-1", "hotel_id": "H01", "status": "CONFIRMED", "amount": "100.00"},
            {"reservation_id": "R-2", "hotel_id": "H02", "status": "NO_SHOW", "amount": "999.99"},
            {"reservation_id": "R-3", "hotel_id": "H03", "status": "CANCELLED", "amount": "999.99"}
        ],
    )
    assert report["by_month"] == [
        {"month": "2025-01", "reservations": 1, "room_nights": 1, "total_brl": "100.00"}
    ]
    assert [hotel["hotel_id"] for hotel in report["top_hotels"]] == ["H01"]