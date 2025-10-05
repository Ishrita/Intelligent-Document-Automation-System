from mineru_module import mineru
from invoicenet_module import inference

def process_document(file_path):
    print("MinerU + InvoiceNet demo running...")
    # Later you can add your real pipeline here
    print(f"Processing file: {file_path}")

if __name__ == "__main__":
    process_document("samples/invoice_sample.pdf")

