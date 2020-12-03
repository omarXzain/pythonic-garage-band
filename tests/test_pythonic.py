import pytest
from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import Band,Guitarist,Bassist,Drummer,Musician

def test_version():
    assert __version__ == '0.1.0'

@pytest.fixture
def allData():
    
    bryan = Bassist("bryan","Bassist")
    Yiannis_Chryssomallis = Guitarist("Yiannis_Chryssomallis")
    Charlie_Adams = Drummer("Charlie_Adams")
    George = Band("George X",[bryan,Yiannis_Chryssomallis,Charlie_Adams],"Careless Whisper")
    return {'bryan':bryan, 'Yiannis_Chryssomallis':Yiannis_Chryssomallis, 'Charlie_Adams':Charlie_Adams , 'George': George}

def test_play_solos(allData):
    expected = ['dan dan dan',
    'tram tram tram',
    'bummm bummm']              
    actual = allData['George'].play_solos()
    assert expected == actual

def test_get_instrument(allData):
    expected = 'Guitar'             
    actual = allData['Yiannis_Chryssomallis'].get_instrument()
    assert expected == actual

def test_play_solo(allData):
    expected = 'dan dan dan'             
    actual = allData['bryan'].play_solo()
    assert expected == actual

def test_to_list(allData):
    expected = Band.to_list()             
    actual = allData['George'].to_list()
    assert expected == actual

