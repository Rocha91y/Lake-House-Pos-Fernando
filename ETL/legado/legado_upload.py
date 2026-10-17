import os
import boto3
from botocore.exceptions import ClientError

# CONFIGURAÇÕES (Com seu caminho local correto)
BUCKET_NAME = "engenharia-dados-lakehouse"  # Certifique-se de que este bucket existe na sua conta AWS
S3_PREFIX = "legado"
LOCAL_BASE_PATH = r"C:\Users\FERNANDO\Desktop\AWS\Lake-House-Pos-Fernando"
FILE_NAME = "Base_Dados.xlsx"  # Ou o nome do arquivo que você criou/colocou lá
AWS_PROFILE = "etl_engenharia_dados"  # Perfil configurado no seu ~/.aws/credentials

LOCAL_FILE_PATH = os.path.join(LOCAL_BASE_PATH, FILE_NAME)
S3_KEY = f"{S3_PREFIX}/{FILE_NAME}"

# FUNÇÃO DE UPLOAD
def upload_file_to_s3(local_path, bucket, s3_key):
    session = boto3.Session(profile_name=AWS_PROFILE)
    s3_client = session.client("s3")
    
    try:
        print(f"[INFO] Iniciando upload do arquivo:")
        print(f"       Origem: {local_path}")
        print(f"       Destino: s3://{bucket}/{s3_key}")
        
        s3_client.upload_file(local_path, bucket, s3_key)
        
        print("[SUCCESS] Upload realizado com sucesso!")
        
    except ClientError as e:
        print(f"[ERROR] Erro ao realizar o upload: {e}")

if __name__ == "__main__":
    upload_file_to_s3(LOCAL_FILE_PATH, BUCKET_NAME, S3_KEY)