from dotenv import load_dotenv
import os
load_dotenv()

S3_ACCESS_KEY=os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY=os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")
CDN_URL= os.getenv("CDN_URL")

basepath = os.path.join(os.path.dirname(__file__), "static", "upload")