from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent.parent

# A partir da raiz, o operador "/" (do pathlib, não é divisão) monta o caminho das subpasta
DATA_RAW_DIR = ROOT_DIR / "data" / "raw"
DATA_PROCESSED_DIR = ROOT_DIR / "data" / "processed"
OUTPUTS_DIR = ROOT_DIR / "outputs"

# A chuva continua fixa por nome porque, nesse caso, é sempre UM único arquivo (uma estação). Não há "vários" para descobrir dinamicamente.
CHUVA_CSV = DATA_RAW_DIR / "834017_Chuvas.csv"

# Retorna todos os documentos .csv desde que possua o nome seguindo o padrão ocorrencias-(ano).csv
OCORRENCIAS_DIR = DATA_RAW_DIR / "ocorrencias"


def listar_ocorrencias_csvs() -> list[Path]:
    return sorted(OCORRENCIAS_DIR.glob("ocorrencias-*.csv"))


DATASET_FINAL_PATH = DATA_PROCESSED_DIR / "dataset_treino.csv"

if __name__ == "__main__":
    # Rode `python -m src.utils.paths` para confirmar que os caminhos
    # calculados apontam para os lugares certos antes de usar em outro
    # arquivo.
    print("Raiz do projeto encontrada em:", ROOT_DIR)
    print("Pasta de dados brutos:", DATA_RAW_DIR)
    print("CSV de chuva esperado em:", CHUVA_CSV)
    print("Ocorrências encontradas dinamicamente:")
    for caminho in listar_ocorrencias_csvs():
        print(" -", caminho.name)
