""" Teste adicional para verificar se o arredondamento ocorre somenre na serialização do programa """

from helpers import PROJECT_ROOT, SRC_DIR, run_cli

def test_soma_exata_e_arredonda_so_na_serializacao(tmp_path):
    report = run_cli(
        tmp_path,
        [{"reservation_id": f"R-{index}", "amount": "0.005"} for index in range(3)],
    )
    assert report["summary"]["total_amount_brl"] == "0.02"