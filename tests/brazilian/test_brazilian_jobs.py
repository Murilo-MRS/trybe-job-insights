# from src.pre_built.brazilian_jobs import read_brazilian_file
from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    mock_output = [
        {'salary': '2000', 'title': 'Maquinista', 'type': 'trainee'},
    ]

    output = read_brazilian_file("tests/mocks/brazilians_jobs.csv")[0]
    assert "tipo" not in mock_output[0]
    assert "salario" not in mock_output[0]
    assert "titulo" not in mock_output[0]
    assert "title" in mock_output[0]
    assert "salary" in mock_output[0]
    assert "type" in mock_output[0]
    assert output == mock_output[0]
