import csv

class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        try:
            with open(self.file_name) as f:
                reader = csv.reader(f)
                lines = [row for row in reader]
            return lines
        except FileNotFoundError:
            # ファイルがない場合の処理
            print("指定されたファイルが見つかりません。")
            raise


