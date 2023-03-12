from funtions import downloadHTML, isntnullHTML, rqt_Mitula
import pytest
from unittest import mock

def test_downloadHTML():
	assert downloadHTML() == True
def test_isntnullHTML():
	assert isntnullHTML() == True
def test_rqt_Mitula(mocker):
    url = "https://casas.mitula.com.co/searchRE/nivel1-Cundinamarca/nivel2-Bogot%C3%A1/nivel3-Chapinero/orden-0/op-1/m2_min-1/m2_max-200/hab_min-1/ban_min-1/q-bogot%C3%A1?req_sgmt=REVTS1RPUDtVU0VSX1NFQVJDSDtTRVJQOw=="
    mocker.patch("requests.post", return_value=True)
    resu = rqt_Mitula(url, json="Json", header="Headers")
    assert resu
